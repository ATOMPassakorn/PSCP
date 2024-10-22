"""Bad Keyboard"""
def bad():
    """Bad Keyboard"""
    text=input()
    length=len(text)
    ans=""
    for i in range(length):
        if text[i]=="i":
            ans+="o"
        elif text[i]=="o":
            ans+="i"
        elif text[i]=="I":
            ans+="O"
        elif text[i]=="O":
            ans+="I"
        else:
            ans+=text[i]
    print(ans)
bad()
