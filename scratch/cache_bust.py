with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace paths with cache-buster versions
content = content.replace("assets/hero-banner.svg", "assets/hero-banner.svg?v=3")
content = content.replace("assets/animated-divider.svg", "assets/animated-divider.svg?v=3")
content = content.replace("assets/project-skillguard.svg", "assets/project-skillguard.svg?v=3")
content = content.replace("assets/project-cricket.svg", "assets/project-cricket.svg?v=3")
content = content.replace("assets/project-university.svg", "assets/project-university.svg?v=3")
content = content.replace("assets/project-farmtech.svg", "assets/project-farmtech.svg?v=3")
content = content.replace("assets/project-saree-palace.svg", "assets/project-saree-palace.svg?v=3")
content = content.replace("assets/project-devorbit.svg", "assets/project-devorbit.svg?v=3")
content = content.replace("assets/project-tutorhub.svg", "assets/project-tutorhub.svg?v=3")
content = content.replace("assets/project-finsight.svg", "assets/project-finsight.svg?v=3")
content = content.replace("assets/project-flashcard.svg", "assets/project-flashcard.svg?v=3")
content = content.replace("assets/project-traffic.svg", "assets/project-traffic.svg?v=3")
content = content.replace("assets/project-reportcard.svg", "assets/project-reportcard.svg?v=3")
content = content.replace("assets/project-portfolio.svg", "assets/project-portfolio.svg?v=3")

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Cache busting parameters added successfully!")
