import re

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the AI Status Dashboard block and replace it with the new animated SVG reference
pattern = r"<!-- AI Status Dashboard -->.*?</blockquote>"
new_svg = """<!-- AI Status Dashboard -->
<p align="center">
  <img src="https://raw.githubusercontent.com/shahanwajkhan/shahanwajkhan/main/assets/status-dashboard.svg?v=1" width="100%" alt="AI System Status" />
</p>"""

content, count = re.subn(pattern, new_svg, content, flags=re.DOTALL)

with open(r"c:\Users\shaha\shahanwajkhan\README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Replaced {count} matches successfully in README.md!")
