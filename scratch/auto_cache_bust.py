import re
import time
import os

readme_path = "README.md"
if not os.path.exists(readme_path):
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Current timestamp as cache buster
ts = int(time.time())

# Update local asset SVGs: e.g. assets/hero-banner.svg?v=143 -> assets/hero-banner.svg?v={ts}
content = re.sub(r'(assets/[a-zA-Z0-9_-]+\.svg\?v=)\d+', rf'\g<1>{ts}', content)

# Function to add or update &v=... query parameter on stats URLs
def add_or_update_v(match):
    url = match.group(0)
    pattern = r'((?:&amp;|[&?])v=)\d+'
    if re.search(pattern, url):
        return re.sub(pattern, rf'\g<1>{ts}', url)
    else:
        separator = '&amp;' if '?' in url else '?'
        return f"{url}{separator}v={ts}"

# Update Vercel stats API URLs
content = re.sub(r'https://github-stats-extended\.vercel\.app/api[a-zA-Z0-9/?=&;_.-]+', add_or_update_v, content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully busted cache in README.md with version v={ts}")
