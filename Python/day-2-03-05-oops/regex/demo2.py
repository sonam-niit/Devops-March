import re

text = "Contact me at dev@pw.live.com or admin@pw.org" 
pattern =r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)