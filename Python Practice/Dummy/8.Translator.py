def translate (a):
    t=""
    for letter in a:
        if letter in "AEIOUaeiou":
            if letter.islower():
                t=t+"g"
            else:
                t=t+"G"
        else:
            t=t+letter
    return t
a=input("Enter the value: ")
print(translate(a))
