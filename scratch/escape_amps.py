with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace raw ampersands with HTML entity escaped versions in the specific lines
replacements = {
    # Typing SVG
    "readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=500&lines=Full+Stack+Developer;AI+Engineer;Cloud+Practitioner;Building+intelligent+solutions":
    "readme-typing-svg.demolab.com?font=Fira+Code&amp;size=20&amp;duration=3000&amp;pause=1000&amp;color=58A6FF&amp;center=true&amp;vCenter=true&amp;width=500&amp;lines=Full+Stack+Developer;AI+Engineer;Cloud+Practitioner;Building+intelligent+solutions",
    
    # GitHub Stats
    "github-readme-stats.vercel.app/api?username=shahanwajkhan&show_icons=true&theme=tokyonight&hide_border=true&count_private=true":
    "github-readme-stats.vercel.app/api?username=shahanwajkhan&amp;show_icons=true&amp;theme=tokyonight&amp;hide_border=true&amp;count_private=true",
    
    # Top Languages
    "github-readme-stats.vercel.app/api/top-langs/?username=shahanwajkhan&layout=compact&theme=tokyonight&hide_border=true":
    "github-readme-stats.vercel.app/api/top-langs/?username=shahanwajkhan&amp;layout=compact&amp;theme=tokyonight&amp;hide_border=true",
    
    # Shields.io Social Badges
    "Email-D14836?style=for-the-badge&logo=gmail&logoColor=white":
    "Email-D14836?style=for-the-badge&amp;logo=gmail&amp;logoColor=white",
    
    "LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white":
    "LinkedIn-0077B5?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white",
    
    "Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white":
    "Portfolio-000000?style=for-the-badge&amp;logo=About.me&amp;logoColor=white",
    
    "GitHub-181717?style=for-the-badge&logo=github&logoColor=white":
    "GitHub-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white",
    
    "Resume-58A6FF?style=for-the-badge&logo=Read-the-Docs&logoColor=white":
    "Resume-58A6FF?style=for-the-badge&amp;logo=Read-the-Docs&amp;logoColor=white"
}

for raw, escaped in replacements.items():
    content = content.replace(raw, escaped)

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Ampersands escaped successfully in README.md!")
