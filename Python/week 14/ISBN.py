"""ISBN"""
def isbn():
    """ISBN"""
    passcode=input()
    passcode=passcode.replace("X","10").split("-")
    code=[]
    for i in passcode:
        if len(i)>2:
            code.extend(list(i))
        else:
            code.append(i)
    total = 0
    for i in range(9):
        total+=int(code[i])*(10-i)
    total*=-1
    total%=11
    if total==int(code[9]):
        print("Yes")
    else:
        if total==10:
            total="X"
        print(f"No {total}")
isbn()
