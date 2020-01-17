import re

str = "Ram lives in pune. Ram likes linux. Ram likes python"
new_str = str.split('. ')
new_str = ','.join(new_str)
for match in re.finditer('Ram', new_str):
  print(match.start(), match.end())