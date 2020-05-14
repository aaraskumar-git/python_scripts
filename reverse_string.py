import re

text = "Aras lives in Bangalore! Aras likes & wish to"

print(re.split('! |& | ', text))
