with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace relative paths with absolute raw paths
raw_prefix = "https://raw.githubusercontent.com/shahanwajkhan/shahanwajkhan/main/assets/"

# We will replace relative paths with raw absolute paths
content = content.replace("src=\"assets/hero-banner.svg?v=3\"", f"src=\"{raw_prefix}hero-banner.svg?v=3\"")
content = content.replace("src=\"assets/animated-divider.svg?v=3\"", f"src=\"{raw_prefix}animated-divider.svg?v=3\"")

# Replace all projects
projects = [
    "project-skillguard.svg",
    "project-cricket.svg",
    "project-university.svg",
    "project-farmtech.svg",
    "project-saree-palace.svg",
    "project-devorbit.svg",
    "project-tutorhub.svg",
    "project-finsight.svg",
    "project-flashcard.svg",
    "project-traffic.svg",
    "project-reportcard.svg",
    "project-portfolio.svg"
]

for p in projects:
    content = content.replace(f"src=\"assets/{p}?v=3\"", f"src=\"{raw_prefix}{p}?v=3\"")

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Paths updated to absolute raw.githubusercontent.com URLs!")
