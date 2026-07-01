with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the paused stats host with the active mirror host
content = content.replace("github-readme-stats.vercel.app", "github-stats-extended.vercel.app")

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Stats host updated successfully to github-stats-extended.vercel.app in README.md!")
