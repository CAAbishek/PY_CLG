def great(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

result= great(1000, 500 ,  200)
print(result)
