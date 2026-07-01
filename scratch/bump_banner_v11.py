with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("hero-banner.svg?v=10", "hero-banner.svg?v=11")

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Bumped banner version in README to v11!")
