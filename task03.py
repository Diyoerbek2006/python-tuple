words = ("apple", "banana", "strawberry", "kiwi")
eng_uzun = words[0]   
for soz in words:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz
print(eng_uzun)
