import string
letters = string.ascii_lowercase

for i in range(len(letters)):
    if i==0 or i==20:
        ordinal = "st"
    elif i==1 or i==21:
        ordinal = "nd"
    elif i==2 or i==22:
        ordinal = "rd"
    else:
        ordinal = "th"
        
    print(f"{letters[i]} is the {i+1}{ordinal} letter of english alphabet")