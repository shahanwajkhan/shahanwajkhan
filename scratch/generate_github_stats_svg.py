import os
import re
import json
import urllib.request
import urllib.error

# Config
USERNAME = "shahanwajkhan"
# Resolve path dynamically relative to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "assets", "github-analytics.svg"))

# Default baseline stats if API fails or is unauthenticated
stats = {
    "commits": 125,
    "stars": 0,
    "prs": 0,
    "issues": 0,
    "languages": [
        {"name": "JavaScript", "pct": 42.25, "color": "#f1e05a"},
        {"name": "HTML", "pct": 18.16, "color": "#e34c26"},
        {"name": "Blade", "pct": 17.04, "color": "#f7523f"},
        {"name": "CSS", "pct": 11.60, "color": "#563d7c"},
        {"name": "Python", "pct": 6.95, "color": "#3572A5"},
        {"name": "PHP", "pct": 4.00, "color": "#4F5D95"}
    ]
}

token = os.environ.get("GITHUB_TOKEN")

def fetch_graphql(token):
    query = """
    query($username: String!) {
      user(login: $username) {
        contributionsCollection {
          totalCommitContributions
          restrictedContributionsCount
        }
        pullRequests(first: 1) {
          totalCount
        }
        issues(first: 1) {
          totalCount
        }
        repositories(first: 100, ownerAffiliations: OWNER) {
          nodes {
            stargazerCount
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                size
                node {
                  name
                  color
                }
              }
            }
          }
        }
      }
    }
    """
    req_data = json.dumps({"query": query, "variables": {"username": USERNAME}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=req_data,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Python-urllib"
        },
        method="POST"
    )
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))

def fetch_rest_repos():
    # Public REST API fallback to count stars and languages
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Python-urllib"}
    )
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))

# 1. Try fetching data
if token:
    try:
        print("Attempting to query GitHub GraphQL API...")
        data = fetch_graphql(token)
        if "data" in data and data["data"]["user"]:
            user_data = data["data"]["user"]
            
            # Commits
            contribs = user_data["contributionsCollection"]
            stats["commits"] = contribs["totalCommitContributions"] + contribs["restrictedContributionsCount"]
            
            # PRs and Issues
            stats["prs"] = user_data["pullRequests"]["totalCount"]
            stats["issues"] = user_data["issues"]["totalCount"]
            
            # Stars & Languages
            repos = user_data["repositories"]["nodes"]
            total_stars = 0
            lang_sizes = {}
            for r in repos:
                total_stars += r["stargazerCount"]
                for edge in r["languages"]["edges"]:
                    name = edge["node"]["name"]
                    color = edge["node"]["color"] or "#85ea2d"
                    size = edge["size"]
                    if name not in lang_sizes:
                        lang_sizes[name] = {"size": 0, "color": color}
                    lang_sizes[name]["size"] += size
            
            stats["stars"] = total_stars
            
            # Compute top languages percentages
            total_lang_size = sum(item["size"] for item in lang_sizes.values())
            if total_lang_size > 0:
                sorted_langs = sorted(lang_sizes.items(), key=lambda x: x[1]["size"], reverse=True)[:6]
                stats["languages"] = [
                    {
                        "name": name,
                        "pct": round((info["size"] / total_lang_size) * 100, 2),
                        "color": info["color"]
                    }
                    for name, info in sorted_langs
                ]
            print("Successfully retrieved statistics from GraphQL API!")
    except Exception as e:
        print(f"GraphQL Query failed: {e}. Falling back to default stats/REST API.")

# Try fetching public stars and repos language stats using REST API if GraphQL failed or token wasn't used
if stats["stars"] == 0:
    try:
        print("Fetching repositories via public REST API for fallback...")
        repos = fetch_rest_repos()
        total_stars = 0
        lang_sizes = {}
        for r in repos:
            if not r.get("fork"):
                total_stars += r.get("stargazers_count", 0)
                lang = r.get("language")
                if lang:
                    # Generic colors mapping for popular languages if colors not present
                    color_map = {
                        "JavaScript": "#f1e05a", "HTML": "#e34c26", "CSS": "#563d7c",
                        "Python": "#3572A5", "PHP": "#4F5D95", "Java": "#b07219",
                        "C++": "#f34b7d", "TypeScript": "#3178c6", "Blade": "#f7523f"
                    }
                    color = color_map.get(lang, "#85ea2d")
                    # Increment count as proxy of size in REST API fallback
                    if lang not in lang_sizes:
                        lang_sizes[lang] = {"size": 0, "color": color}
                    lang_sizes[lang]["size"] += 1
                    
        stats["stars"] = total_stars
        if lang_sizes:
            total_size = sum(item["size"] for item in lang_sizes.values())
            sorted_langs = sorted(lang_sizes.items(), key=lambda x: x[1]["size"], reverse=True)[:6]
            stats["languages"] = [
                {
                    "name": name,
                    "pct": round((info["size"] / total_size) * 100, 2),
                    "color": info["color"]
                }
                for name, info in sorted_langs
            ]
        print(f"REST API Fallback Complete. Stars: {total_stars}")
    except Exception as e:
        print(f"REST API Fallback failed: {e}. Using baseline fallback.")

# 2. Calculate Grade/Rank
# Commits: 1pt, Stars: 10pts, PRs: 5pts, Issues: 2pts
score = stats["commits"] + (stats["stars"] * 10) + (stats["prs"] * 5) + (stats["issues"] * 2)
if score >= 600:
    rank = "S+"
elif score >= 400:
    rank = "S"
elif score >= 200:
    rank = "A+"
elif score >= 100:
    rank = "A"
elif score >= 50:
    rank = "B"
else:
    rank = "C"

# 3. Generate the SVG content
language_rows = ""
for i, lang in enumerate(stats["languages"][:5]): # Show top 5
    pct = lang["pct"]
    color = lang["color"]
    name = lang["name"]
    # width limit is 310
    bar_width = round(310 * (pct / 100.0), 1)
    
    language_rows += f"""    <g class="lang-row stagger-{i+1}" transform="translate(0, {22 + i * 21})" style="--lang-color: {color};">
      <circle cx="6" cy="6" r="4.5" fill="{color}" />
      <text x="18" y="10" font-family="'Inter', -apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#a097ba">{name}</text>
      <text x="330" y="10" font-family="'Inter', -apple-system, sans-serif" font-size="10" font-weight="700" fill="#ffffff" text-anchor="end">{pct}%</text>
      <rect x="18" y="15" width="312" height="4" rx="2" fill="#1b1530" />
      <rect x="18" y="15" width="{bar_width}" height="4" rx="2" fill="{color}" class="progress-fill" />
    </g>
"""

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 210" width="100%" height="210">
  <defs>
    <!-- Background gradients -->
    <radialGradient id="bg-grad" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#100c1e" />
      <stop offset="60%" stop-color="#080510" />
      <stop offset="100%" stop-color="#030206" />
    </radialGradient>

    <!-- Aurora Gradients -->
    <radialGradient id="aurora-cyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#00f2fe" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="aurora-purple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7b2cbf" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#7b2cbf" stop-opacity="0" />
    </radialGradient>

    <!-- Glass border -->
    <linearGradient id="glass-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#7b2cbf" stop-opacity="0.05" />
    </linearGradient>

    <!-- Glow filters -->
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .title {{
      font-family: 'Inter', system-ui, sans-serif;
      font-weight: 800;
      font-size: 13px;
      fill: #ffffff;
      letter-spacing: 2px;
      text-transform: uppercase;
    }}
    .panel-title {{
      font-family: 'Inter', system-ui, sans-serif;
      font-weight: 700;
      font-size: 10px;
      fill: #8e81ac;
      letter-spacing: 1.5px;
      text-transform: uppercase;
    }}
    .label {{
      font-family: 'Inter', system-ui, sans-serif;
      font-weight: 600;
      font-size: 11px;
      fill: #a097ba;
    }}
    .value {{
      font-family: 'Inter', system-ui, sans-serif;
      font-weight: 700;
      font-size: 12px;
      fill: #ffffff;
    }}
    .rank-text {{
      font-family: 'Inter', system-ui, sans-serif;
      font-weight: 900;
      font-size: 32px;
      fill: #00f2fe;
      text-anchor: middle;
      filter: drop-shadow(0 0 6px rgba(0, 242, 254, 0.6));
    }}
    
    /* Hover effects and keyframes */
    @keyframes rotate-outer {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    .rotating-ring {{
      animation: rotate-outer 25s linear infinite;
      transform-origin: 310px 118px;
    }}
    @keyframes pulse-glow {{
      0%, 100% {{ filter: drop-shadow(0 0 2px rgba(0, 242, 254, 0.3)); }}
      50% {{ filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.8)); }}
    }}
    .rank-pulse {{
      animation: pulse-glow 2s ease-in-out infinite;
    }}
    
    /* Progress bar animations */
    @keyframes grow-bar {{
      from {{ width: 0; }}
    }}
    .progress-fill {{
      animation: grow-bar 1.5s cubic-bezier(0.1, 1, 0.1, 1) forwards;
    }}

    /* Staggered load for rows */
    @keyframes fade-in {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    .stagger-1 {{ animation: fade-in 0.5s ease forwards; }}
    .stagger-2 {{ animation: fade-in 0.5s ease 0.1s forwards; }}
    .stagger-3 {{ animation: fade-in 0.5s ease 0.2s forwards; }}
    .stagger-4 {{ animation: fade-in 0.5s ease 0.3s forwards; }}
    .stagger-5 {{ animation: fade-in 0.5s ease 0.4s forwards; }}
    
    /* Interactive Hover Classes */
    .metric-row {{
      opacity: 0;
      transition: transform 0.2s ease, opacity 0.3s ease;
      cursor: pointer;
    }}
    .metric-row:hover {{
      transform: translateX(3px);
    }}
    .metric-row:hover .label {{
      fill: #ffffff;
    }}
    .lang-row {{
      opacity: 0;
      transition: transform 0.2s ease, opacity 0.3s ease;
      cursor: pointer;
    }}
    .lang-row:hover {{
      transform: translateX(4px);
    }}
    .lang-row:hover .progress-fill {{
      filter: drop-shadow(0 0 5px var(--lang-color));
    }}
    .lang-row:hover text {{
      fill: #ffffff;
    }}
  </style>

  <rect width="100%" height="100%" fill="url(#bg-grad)" rx="10" />
  <circle cx="150" cy="100" r="120" fill="url(#aurora-cyan)" opacity="0.3" />
  <circle cx="650" cy="110" r="130" fill="url(#aurora-purple)" opacity="0.3" />

  <!-- Outer Glass Frame -->
  <rect x="12" y="12" width="776" height="186" rx="12" fill="#0d0a1b" fill-opacity="0.5" stroke="url(#glass-border)" stroke-width="1.2" />

  <!-- Header -->
  <text x="32" y="32" class="title">AI WORKSPACE // COGNITIVE DIAGNOSTICS</text>
  <line x1="12" y1="42" x2="788" y2="42" stroke="#251a3d" stroke-width="1" />

  <!-- LEFT PANEL: Core Stats & Rank -->
  <rect x="25" y="52" width="365" height="136" rx="10" fill="#080612" fill-opacity="0.75" stroke="url(#glass-border)" stroke-width="1" />
  
  <g transform="translate(40, 60)">
    <text x="0" y="10" class="panel-title">COGNITIVE CORES</text>
    
    <!-- Commits -->
    <g class="metric-row stagger-1" transform="translate(0, 22)">
      <circle cx="8" cy="8" r="4" fill="#00f2fe" opacity="0.8" />
      <text x="24" y="12" class="label">Synaptic Commits</text>
      <text x="210" y="12" class="value">{stats["commits"]}</text>
    </g>
    
    <!-- Stars -->
    <g class="metric-row stagger-2" transform="translate(0, 46)">
      <circle cx="8" cy="8" r="4" fill="#ffb703" opacity="0.8" />
      <text x="24" y="12" class="label">Stellar Stars</text>
      <text x="210" y="12" class="value">{stats["stars"]}</text>
    </g>
    
    <!-- PRs -->
    <g class="metric-row stagger-3" transform="translate(0, 70)">
      <circle cx="8" cy="8" r="4" fill="#a2d2ff" opacity="0.8" />
      <text x="24" y="12" class="label">System Merges (PRs)</text>
      <text x="210" y="12" class="value">{stats["prs"]}</text>
    </g>
    
    <!-- Issues -->
    <g class="metric-row stagger-4" transform="translate(0, 94)">
      <circle cx="8" cy="8" r="4" fill="#ff4d6d" opacity="0.8" />
      <text x="24" y="12" class="label">Diagnostic Alerts (Issues)</text>
      <text x="210" y="12" class="value">{stats["issues"]}</text>
    </g>
  </g>
  
  <!-- Rank circular index (inside left panel) -->
  <g transform="translate(310, 118)">
    <!-- Rotating outer dashed circle -->
    <circle r="40" fill="none" stroke="#251a3d" stroke-width="1" />
    <circle r="40" fill="none" stroke="#00f2fe" stroke-width="1.5" stroke-dasharray="8 6" class="rotating-ring" opacity="0.6" />
    <!-- Pulse outer circle -->
    <circle r="34" fill="none" stroke="#7b2cbf" stroke-width="1" opacity="0.4" />
    <!-- Core glow -->
    <circle r="28" fill="#100c1e" stroke="url(#glass-border)" stroke-width="1" class="rank-pulse" />
    <text y="10" class="rank-text">{rank}</text>
    <text y="50" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#8e81ac" text-anchor="middle" letter-spacing="1">CORE LEVEL</text>
  </g>

  <!-- RIGHT PANEL: Language Spectrum -->
  <rect x="410" y="52" width="365" height="136" rx="10" fill="#080612" fill-opacity="0.75" stroke="url(#glass-border)" stroke-width="1" />
  
  <g transform="translate(425, 60)">
    <text x="0" y="10" class="panel-title">TECH STACK SPECTRUM</text>
    
    <!-- Language rows dynamic -->
{language_rows}  </g>
</svg>
"""

# Ensure assets directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Write output
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Successfully generated GitHub Stats SVG at {OUTPUT_PATH}")
