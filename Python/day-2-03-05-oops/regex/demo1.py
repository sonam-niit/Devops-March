import re

pattern = r"\d{3}-\d{2}-\d{4}" #SSN Pattern
text = "Sonam SSN is 123-45-6789"

match = re.search(pattern, text)

if match:
    print("Match Found", match.group())