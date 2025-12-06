
ch = input("Enter charecter: ").lower()

if(len(ch)!= 1 or ch.isalpha()):
    print("please enetr only one charecter")
else:
    if(ch.lower() in ["a","e","i","o","u"]):
        print("vowel")
    else: print("consonent")
