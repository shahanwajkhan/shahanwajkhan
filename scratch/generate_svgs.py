import os

# Ensure assets dir exists
os.makedirs(r"c:\Users\shaha\shahanwajkhan\assets", exist_ok=True)

# CSS styles mapping for badge colors - default colorful and animated
BADGE_COLORS_CSS = """
    /* Staggered Badge Wave Animation */
    .badge-item {
      transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease;
    }
    .card:hover .badge-1 { transform: translateY(-3px); }
    .card:hover .badge-2 { transform: translateY(-3px); transition-delay: 0.04s; }
    .card:hover .badge-3 { transform: translateY(-3px); transition-delay: 0.08s; }
    .card:hover .badge-4 { transform: translateY(-3px); transition-delay: 0.12s; }
    .card:hover .badge-5 { transform: translateY(-3px); transition-delay: 0.16s; }

    /* Default badge style */
    .badge-bg {
      stroke-width: 1;
      transition: all 0.3s ease;
    }
    .badge-text {
      font-family: 'Fira Code', 'Courier New', Courier, monospace;
      font-size: 11px;
      transition: all 0.3s ease;
    }

    /* Brand Colors - Default State and Hover State */
    
    /* React */
    .bg-react { fill: #0E1A24; stroke: rgba(97, 218, 251, 0.35); }
    .txt-react { fill: #61DAFB; }
    .card:hover .bg-react { fill: #14232C; stroke: #61DAFB; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(97, 218, 251, 0.5)); }
    .card:hover .txt-react { fill: #61DAFB; }
    
    /* Node */
    .bg-node { fill: #0E1B12; stroke: rgba(51, 153, 51, 0.35); }
    .txt-node { fill: #339933; }
    .card:hover .bg-node { fill: #142517; stroke: #339933; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(51, 153, 51, 0.5)); }
    .card:hover .txt-node { fill: #339933; }
    
    /* Express */
    .bg-express { fill: #131314; stroke: rgba(255, 255, 255, 0.2); }
    .txt-express { fill: #C9D1D9; }
    .card:hover .bg-express { fill: #1A1A1A; stroke: #FFFFFF; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.3)); }
    .card:hover .txt-express { fill: #FFFFFF; }
    
    /* MongoDB */
    .bg-mongodb { fill: #0E1B12; stroke: rgba(71, 162, 72, 0.35); }
    .txt-mongodb { fill: #47A248; }
    .card:hover .bg-mongodb { fill: #112516; stroke: #47A248; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(71, 162, 72, 0.5)); }
    .card:hover .txt-mongodb { fill: #47A248; }
    
    /* Tailwind */
    .bg-tailwind { fill: #0E1A24; stroke: rgba(6, 182, 212, 0.35); }
    .txt-tailwind { fill: #06B6D4; }
    .card:hover .bg-tailwind { fill: #11252C; stroke: #06B6D4; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(6, 182, 212, 0.5)); }
    .card:hover .txt-tailwind { fill: #06B6D4; }
    
    /* Socket.io */
    .bg-socket { fill: #131314; stroke: rgba(255, 255, 255, 0.2); }
    .txt-socket { fill: #C9D1D9; }
    .card:hover .bg-socket { fill: #1A1A1A; stroke: #FFFFFF; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.3)); }
    .card:hover .txt-socket { fill: #FFFFFF; }
    
    /* Django */
    .bg-django { fill: #0E1B15; stroke: rgba(68, 183, 139, 0.35); }
    .txt-django { fill: #44B78B; }
    .card:hover .bg-django { fill: #0B251B; stroke: #44B78B; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(68, 183, 139, 0.5)); }
    .card:hover .txt-django { fill: #44B78B; }
    
    /* SQLite */
    .bg-sqlite { fill: #0E1724; stroke: rgba(64, 166, 242, 0.35); }
    .txt-sqlite { fill: #40A6F2; }
    .card:hover .bg-sqlite { fill: #111F2C; stroke: #40A6F2; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(64, 166, 242, 0.5)); }
    .card:hover .txt-sqlite { fill: #40A6F2; }
    
    /* HTML */
    .bg-html { fill: #1B120E; stroke: rgba(227, 79, 38, 0.35); }
    .txt-html { fill: #E34F26; }
    .card:hover .bg-html { fill: #2C1A14; stroke: #E34F26; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(227, 79, 38, 0.5)); }
    .card:hover .txt-html { fill: #E34F26; }
    
    /* CSS */
    .bg-css { fill: #0E1724; stroke: rgba(21, 114, 182, 0.35); }
    .txt-css { fill: #1572B6; }
    .card:hover .bg-css { fill: #111F2C; stroke: #1572B6; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(21, 114, 182, 0.5)); }
    .card:hover .txt-css { fill: #1572B6; }
    
    /* Bootstrap */
    .bg-bootstrap { fill: #170E24; stroke: rgba(155, 114, 211, 0.35); }
    .txt-bootstrap { fill: #9B72D3; }
    .card:hover .bg-bootstrap { fill: #20142C; stroke: #9B72D3; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(155, 114, 211, 0.5)); }
    .card:hover .txt-bootstrap { fill: #9B72D3; }
    
    /* Laravel */
    .bg-laravel { fill: #1B0E0F; stroke: rgba(255, 45, 32, 0.35); }
    .txt-laravel { fill: #FF2D20; }
    .card:hover .bg-laravel { fill: #2C1415; stroke: #FF2D20; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(255, 45, 32, 0.5)); }
    .card:hover .txt-laravel { fill: #FF2D20; }
    
    /* GIS */
    .bg-gis { fill: #0E1B15; stroke: rgba(16, 185, 129, 0.35); }
    .txt-gis { fill: #10B981; }
    .card:hover .bg-gis { fill: #142820; stroke: #10B981; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(16, 185, 129, 0.5)); }
    .card:hover .txt-gis { fill: #10B981; }
    
    /* Python */
    .bg-python { fill: #0E1724; stroke: rgba(55, 118, 171, 0.37); }
    .txt-python { fill: #40A6F2; }
    .card:hover .bg-python { fill: #111F2C; stroke: #3776AB; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(55, 118, 171, 0.5)); }
    .card:hover .txt-python { fill: #FFD43B; }
    
    /* Flask */
    .bg-flask { fill: #131314; stroke: rgba(255, 255, 255, 0.2); }
    .txt-flask { fill: #C9D1D9; }
    .card:hover .bg-flask { fill: #1A1A1A; stroke: #FFFFFF; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.3)); }
    .card:hover .txt-flask { fill: #FFFFFF; }
    
    /* OTP */
    .bg-otp { fill: #1B150E; stroke: rgba(245, 158, 11, 0.35); }
    .txt-otp { fill: #F59E0B; }
    .card:hover .bg-otp { fill: #2C1F11; stroke: #F59E0B; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(245, 158, 11, 0.5)); }
    .card:hover .txt-otp { fill: #F59E0B; }
    
    /* Recharts */
    .bg-recharts { fill: #0E1A24; stroke: rgba(49, 130, 206, 0.35); }
    .txt-recharts { fill: #3182CE; }
    .card:hover .bg-recharts { fill: #112525; stroke: #3182CE; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(49, 130, 206, 0.5)); }
    .card:hover .txt-recharts { fill: #3182CE; }
    
    /* Storage */
    .bg-storage { fill: #13171C; stroke: rgba(113, 128, 150, 0.35); }
    .txt-storage { fill: #A0AEC0; }
    .card:hover .bg-storage { fill: #1A222C; stroke: #718096; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(113, 128, 150, 0.5)); }
    .card:hover .txt-storage { fill: #A0AEC0; }
    
    /* Gemini */
    .bg-gemini { fill: #0E1724; stroke: rgba(21, 195, 255, 0.35); }
    .txt-gemini { fill: #15C3FF; }
    .card:hover .bg-gemini { fill: #14202F; stroke: #15C3FF; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(21, 195, 255, 0.5)); }
    .card:hover .txt-gemini { fill: #15C3FF; }
    
    /* C++ */
    .bg-cpp { fill: #0E1724; stroke: rgba(0, 89, 156, 0.35); }
    .txt-cpp { fill: #40A6F2; }
    .card:hover .bg-cpp { fill: #111F2C; stroke: #00599C; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(0, 89, 156, 0.5)); }
    .card:hover .txt-cpp { fill: #00599C; }
    
    /* Java */
    .bg-java { fill: #1B150E; stroke: rgba(237, 139, 0, 0.35); }
    .txt-java { fill: #ED8B00; }
    .card:hover .bg-java { fill: #2C1E11; stroke: #ED8B00; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(237, 139, 0, 0.5)); }
    .card:hover .txt-java { fill: #ED8B00; }
    
    /* Files */
    .bg-files { fill: #0E1B15; stroke: rgba(16, 185, 129, 0.35); }
    .txt-files { fill: #10B981; }
    .card:hover .bg-files { fill: #1C2420; stroke: #10B981; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(16, 185, 129, 0.5)); }
    .card:hover .txt-files { fill: #10B981; }
    
    /* Framer */
    .bg-framer { fill: #1B0E16; stroke: rgba(241, 7, 163, 0.35); }
    .txt-framer { fill: #F107A3; }
    .card:hover .bg-framer { fill: #2C1122; stroke: #F107A3; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(241, 7, 163, 0.5)); }
    .card:hover .txt-framer { fill: #F107A3; }
    
    /* JS */
    .bg-js { fill: #1B1A0E; stroke: rgba(247, 223, 30, 0.35); }
    .txt-js { fill: #F7DF1E; }
    .card:hover .bg-js { fill: #2C2B11; stroke: #F7DF1E; stroke-width: 1.5; filter: drop-shadow(0 0 2px rgba(247, 223, 30, 0.5)); }
    .card:hover .txt-js { fill: #F7DF1E; }
"""

projects = [
    {
        "filename": "project-skillguard.svg",
        "title": "🛡️ SkillGuard AI",
        "desc": "AI-powered skill assessment and recruitment platform analyzing candidate test performances.",
        "badges": [
            {"text": "Python", "class": "python", "width": 75},
            {"text": "Django", "class": "django", "width": 75},
            {"text": "SQLite", "class": "sqlite", "width": 70},
            {"text": "Django Admin", "class": "django", "width": 110},
            {"text": "HTML5", "class": "html", "width": 70}
        ],
        "accent": "#58A6FF",
        "gradient": ("#58A6FF", "#00F2FE"),
        "icon_paths": [
            '<path class="icon-draw" d="M30 62 L30 68 Q30 76 40 82 Q50 76 50 68 L50 62 L40 58 Z" />',
            '<path class="icon-draw" d="M35 70 L39 74 L46 66" />'
        ],
        "rotation": 15
    },
    {
        "filename": "project-cricket.svg",
        "title": "🏏 Cricket Management System",
        "desc": "Sports coordination platform featuring team analytics, match scheduling, and live chat.",
        "badges": [
            {"text": "React.js", "class": "react", "width": 75},
            {"text": "Node.js", "class": "node", "width": 75},
            {"text": "Express", "class": "express", "width": 75},
            {"text": "MongoDB", "class": "mongodb", "width": 80},
            {"text": "Socket.io", "class": "socket", "width": 85}
        ],
        "accent": "#FF7B72",
        "gradient": ("#FF7B72", "#FFA657"),
        "icon_paths": [
            '<path class="icon-draw" d="M32 60 L48 60 L46 72 Q46 76 40 78 Q34 76 34 72 Z" />',
            '<path class="icon-draw" d="M40 78 L40 82 M35 82 L45 82" />',
            '<path class="icon-draw" d="M32 63 C29 63 29 69 32 69" />',
            '<path class="icon-draw" d="M48 63 C51 63 51 69 48 69" />'
        ],
        "rotation": -15
    },
    {
        "filename": "project-university.svg",
        "title": "🎓 University Management System",
        "desc": "A role-based digital campus platform managing students, faculty, courses, and attendance.",
        "badges": [
            {"text": "Django", "class": "django", "width": 75},
            {"text": "SQLite", "class": "sqlite", "width": 70},
            {"text": "HTML5", "class": "html", "width": 70},
            {"text": "CSS3", "class": "css", "width": 70},
            {"text": "Bootstrap", "class": "bootstrap", "width": 85}
        ],
        "accent": "#38B2AC",
        "gradient": ("#38B2AC", "#3182CE"),
        "icon_paths": [
            '<path class="icon-draw" d="M30 63 L40 58 L50 63 L40 68 Z" />',
            '<path class="icon-draw" d="M34 65 L34 71 Q34 76 40 76 Q46 76 46 71 L46 65" />',
            '<path class="icon-draw" d="M47 64 L47 75 C47 77 48 77 49 77" />'
        ],
        "rotation": 0
    },
    {
        "filename": "project-farmtech.svg",
        "title": "🌾 FarmTech MIS",
        "desc": "A smart agriculture platform with crop advisories, GIS mapping, marketplace, and inventory.",
        "badges": [
            {"text": "Laravel", "class": "laravel", "width": 75},
            {"text": "Tailwind CSS", "class": "tailwind", "width": 100},
            {"text": "MongoDB", "class": "mongodb", "width": 80},
            {"text": "GIS APIs", "class": "gis", "width": 75}
        ],
        "accent": "#10B981",
        "gradient": ("#10B981", "#84CC16"),
        "icon_paths": [
            '<path class="icon-draw" d="M40 82 L40 68" />',
            '<path class="icon-draw" d="M40 68 Q46 60 46 54 Q38 54 40 68 Z" fill="#112A20" />',
            '<path class="icon-draw" d="M40 73 Q32 70 30 62 Q38 62 40 73 Z" fill="#112A20" />'
        ],
        "rotation": 10
    },
    {
        "filename": "project-saree-palace.svg",
        "title": "🛍️ Saree Palace Boutique",
        "desc": "A luxury e-commerce boutique storefront with a Patron Loyalty Portal and OTP verification.",
        "badges": [
            {"text": "HTML5", "class": "html", "width": 70},
            {"text": "CSS3", "class": "css", "width": 70},
            {"text": "ES6 JS", "class": "js", "width": 75},
            {"text": "OTP Auth", "class": "otp", "width": 90}
        ],
        "accent": "#EC4899",
        "gradient": ("#EC4899", "#F59E0B"),
        "icon_paths": [
            '<path class="icon-draw" d="M32 63 L32 79 L48 79 L48 63 Z" />',
            '<path class="icon-draw" d="M36 63 C36 57 44 57 44 63" />'
        ],
        "rotation": -10
    },
    {
        "filename": "project-devorbit.svg",
        "title": "🤖 DevOrbit AI Assistant",
        "desc": "Intelligent study aid supporting course generation, dynamic quiz creation, and syllabus maps.",
        "badges": [
            {"text": "Flask", "class": "flask", "width": 70},
            {"text": "Python", "class": "python", "width": 75},
            {"text": "Gemini API", "class": "gemini", "width": 95},
            {"text": "Node.js", "class": "node", "width": 85}
        ],
        "accent": "#BA55D3",
        "gradient": ("#BA55D3", "#58A6FF"),
        "icon_paths": [
            '<circle class="icon-draw" cx="40" cy="70" r="8" fill="#27142A" />',
            '<ellipse class="icon-draw" cx="40" cy="70" rx="15" ry="5" transform="rotate(-30, 40, 70)" />'
        ],
        "rotation": 45
    },
    {
        "filename": "project-tutorhub.svg",
        "title": "🧠 AI Tutor Hub Chatbot",
        "desc": "Intelligent web tutoring bot enabling interactive concept queries and study support.",
        "badges": [
            {"text": "Python", "class": "python", "width": 75},
            {"text": "Flask", "class": "flask", "width": 70},
            {"text": "Django", "class": "django", "width": 70},
            {"text": "JS ES6", "class": "js", "width": 70}
        ],
        "accent": "#8B5CF6",
        "gradient": ("#8B5CF6", "#EC4899"),
        "icon_paths": [
            '<rect class="icon-draw" x="30" y="60" width="20" height="15" rx="2" />',
            '<circle cx="36" cy="67" r="1.5" fill="#a78bfa" />',
            '<circle cx="44" cy="67" r="1.5" fill="#a78bfa" />',
            '<path class="icon-draw" d="M35 71 L45 71 M40 60 L40 56 M38 56 L42 56" />'
        ],
        "rotation": 12
    },
    {
        "filename": "project-finsight.svg",
        "title": "📊 FinSight Dashboard",
        "desc": "A finance manager dashboard tracking incomes, expenses, and transactions with data analytics.",
        "badges": [
            {"text": "React.js", "class": "react", "width": 75},
            {"text": "Tailwind CSS", "class": "tailwind", "width": 100},
            {"text": "Recharts", "class": "recharts", "width": 75},
            {"text": "Local Storage", "class": "storage", "width": 95}
        ],
        "accent": "#F59E0B",
        "gradient": ("#F59E0B", "#10B981"),
        "icon_paths": [
            '<path class="icon-draw" d="M30 76 L30 62 M36 76 L36 55 M42 76 L42 66 M48 76 L48 50" />',
            '<path class="icon-draw" d="M26 76 L54 76" />'
        ],
        "rotation": 0
    },
    {
        "filename": "project-flashcard.svg",
        "title": "⚡ AI Flashcard Generator",
        "desc": "Automated learning assistant generating spaced-repetition study flashcards using AI.",
        "badges": [
            {"text": "React.js", "class": "react", "width": 75},
            {"text": "Node.js", "class": "node", "width": 75},
            {"text": "Express", "class": "express", "width": 75},
            {"text": "GenAI API", "class": "gemini", "width": 95}
        ],
        "accent": "#F97316",
        "gradient": ("#F97316", "#EAB308"),
        "icon_paths": [
            '<rect class="icon-draw" x="31" y="60" width="14" height="18" rx="1" transform="rotate(-15, 38, 69)" />',
            '<rect class="icon-draw" x="35" y="61" width="14" height="18" rx="1" transform="rotate(10, 42, 70)" />'
        ],
        "rotation": 15
    },
    {
        "filename": "project-traffic.svg",
        "title": "🚦 Traffic Management System",
        "desc": "A web dashboard interface enabling visual traffic updates, alerts, and routing services.",
        "badges": [
            {"text": "HTML5", "class": "html", "width": 70},
            {"text": "CSS3", "class": "css", "width": 70},
            {"text": "JavaScript", "class": "js", "width": 95}
        ],
        "accent": "#22C55E",
        "gradient": ("#EF4444", "#22C55E"),
        "icon_paths": [
            '<rect class="icon-draw" x="35" y="58" width="10" height="24" rx="2" />',
            '<circle cx="40" cy="63" r="2" fill="#EF4444" />',
            '<circle cx="40" cy="70" r="2" fill="#F59E0B" />',
            '<circle cx="40" cy="77" r="2" fill="#10B981" />'
        ],
        "rotation": 0
    },
    {
        "filename": "project-reportcard.svg",
        "title": "📝 Student Report Card System",
        "desc": "A console/web-based student management system for persistency records and automated grading.",
        "badges": [
            {"text": "C++", "class": "cpp", "width": 60},
            {"text": "Java", "class": "java", "width": 65},
            {"text": "Python", "class": "python", "width": 75},
            {"text": "Files I/O", "class": "files", "width": 90}
        ],
        "accent": "#6366F1",
        "gradient": ("#6366F1", "#3B82F6"),
        "icon_paths": [
            '<path class="icon-draw" d="M32 58 L44 58 L48 62 L48 82 L32 82 Z" />',
            '<path class="icon-draw" d="M44 58 L44 62 L48 62" />',
            '<path class="icon-draw" d="M36 66 L44 66 M36 72 L44 72 M36 78 L40 78" />'
        ],
        "rotation": -10
    },
    {
        "filename": "project-portfolio.svg",
        "title": "💻 Modern Developer Portfolio",
        "desc": "A fast, fully responsive portfolio showcasing skills, projects, and cloud certifications.",
        "badges": [
            {"text": "React.js", "class": "react", "width": 75},
            {"text": "Tailwind CSS", "class": "tailwind", "width": 100},
            {"text": "Framer Motion", "class": "framer", "width": 105}
        ],
        "accent": "#8B5CF6",
        "gradient": ("#8B5CF6", "#06B6D4"),
        "icon_paths": [
            '<rect class="icon-draw" x="30" y="60" width="20" height="15" rx="1" />',
            '<path class="icon-draw" d="M35 75 L33 80 L47 80 L45 75 Z" />',
            '<line class="icon-draw" x1="32" y1="71" x2="48" y2="71" />'
        ],
        "rotation": 0
    }
]

template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 140" width="100%" height="140">
  <style>
    /* Clean fallback fonts so no external imports are needed */
    .card {{
      fill: #0D1117;
      stroke: #21262D;
      stroke-width: 1.5;
      transition: all 0.3s ease;
    }}
    .card:hover {{
      fill: #161B22;
      stroke: url(#glow-grad);
      filter: drop-shadow(0 0 10px rgba({glow_rgb}, 0.25));
    }}
    .title {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
      font-weight: 700;
      font-size: 19px;
      fill: #C9D1D9;
      transition: fill 0.3s ease;
    }}
    .card:hover .title {{
      fill: {accent};
    }}
    .desc {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-size: 13px;
      fill: #8B949E;
    }}
    .btn {{
      fill: #21262D;
      stroke: #30363D;
      stroke-width: 1;
      transition: all 0.3s ease;
    }}
    .btn-text {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      font-weight: 600;
      font-size: 12px;
      fill: #8B949E;
      transition: all 0.3s ease;
    }}
    .card:hover .btn {{
      fill: {accent};
      stroke: {accent};
    }}
    .card:hover .btn-text {{
      fill: #0D1117;
    }}
    .icon-container {{
      transition: transform 0.5s ease;
      transform-origin: 40px 70px;
    }}
    .card:hover .icon-container {{
      transform: scale(1.15) {rotate_str};
    }}
    .icon-draw {{
      fill: none;
      stroke: {accent};
      stroke-width: 2;
      stroke-linejoin: round;
      stroke-linecap: round;
      transition: stroke 0.3s ease;
    }}
    .card:hover .icon-draw {{
      stroke: {accent};
      filter: drop-shadow(0 0 3px {accent});
    }}
    {badge_css}
  </style>
  <defs>
    <linearGradient id="glow-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{grad0}" />
      <stop offset="100%" stop-color="{grad1}" />
    </linearGradient>
  </defs>
  
  <rect class="card" x="2" y="2" width="796" height="136" rx="8" />
  
  <!-- Icon Wrapper -->
  <g class="icon-container">
    <circle cx="40" cy="70" r="22" fill="#161B22" stroke="#30363D" stroke-width="1" />
    {icon_svg}
  </g>
  
  <!-- Content -->
  <text x="80" y="42" class="title">{title}</text>
  <text x="80" y="65" class="desc">{desc}</text>
  
  <!-- Tech Stack Badges -->
  <g transform="translate(80, 85)">
    {badges_svg}
  </g>
  
  <!-- Button "View Project" -->
  <rect x="670" y="50" width="100" height="36" rx="18" class="btn" />
  <text x="720" y="72" text-anchor="middle" class="btn-text">View Project ↗</text>
</svg>
"""

# Convert hex color to RGB string for box-shadow effect
def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return f"{int(hex_str[0:2], 16)}, {int(hex_str[2:4], 16)}, {int(hex_str[4:6], 16)}"

for p in projects:
    glow_rgb = hex_to_rgb(p["accent"])
    rotate_str = f"rotate({p['rotation']}deg)" if p["rotation"] != 0 else ""
    
    icon_svg = "\n    ".join(p["icon_paths"])
    
    badges_svg_list = []
    current_x = 0
    for idx, b in enumerate(p["badges"]):
        b_x = current_x
        b_w = b["width"]
        b_class_num = f"badge-{idx+1}"
        
        badge_xml = f"""<g class="badge-item {b_class_num}" transform="translate({b_x}, 0)">
      <rect x="0" y="0" width="{b_w}" height="22" rx="4" class="badge-bg bg-{b["class"]}" />
      <text x="{b_w/2}" y="15" text-anchor="middle" class="badge-text txt-{b["class"]}">{b["text"]}</text>
    </g>"""
        badges_svg_list.append(badge_xml)
        current_x += b_w + 8  # Add space between badges
        
    badges_svg = "\n    ".join(badges_svg_list)
    
    file_content = template.format(
        glow_rgb=glow_rgb,
        accent=p["accent"],
        rotate_str=rotate_str,
        icon_svg=icon_svg,
        title=p["title"],
        desc=p["desc"],
        badges_svg=badges_svg,
        grad0=p["gradient"][0],
        grad1=p["gradient"][1],
        badge_css=BADGE_COLORS_CSS
    )
    
    file_path = os.path.join(r"c:\Users\shaha\shahanwajkhan\assets", p["filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)

print("SVGs successfully regenerated without Google Fonts import!")
