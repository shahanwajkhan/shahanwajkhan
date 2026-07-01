with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace any previous hero banner version with v14
content = content.replace("hero-banner.svg?v=13", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=12", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=11", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=10", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=9", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=8", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=7", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=6", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=5", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=4", "hero-banner.svg?v=14")
content = content.replace("hero-banner.svg?v=3", "hero-banner.svg?v=14")

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Banner version bumped to v14 in README.md!")
