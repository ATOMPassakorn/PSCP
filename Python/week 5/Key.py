"""Key"""
def key():
    """Key"""
    num=input()
    som=0
    for i in num:
        som+=int(i)
    three=int(num[-3]+num[-2]+num[-1])
    password=som+three*10
    if password<1000:
        password+=1000
    print(str(password)[-4:])
key()
