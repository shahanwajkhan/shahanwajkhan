with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("hero-banner.svg?v=13", "hero-banner.svg?v=100")

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Banner version bumped to v100 in README.md!")
