# Given string, change all the characters into caps
str = "aRaS"
upd_str = ""
for index, ech in enumerate(str):
    if ord(ech) >= 97:
        upd_str = upd_str + chr(ord(ech)-32)
    else:
        upd_str = upd_str + ech
print(upd_str)