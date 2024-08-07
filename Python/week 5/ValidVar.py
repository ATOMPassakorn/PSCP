"""ValidVar"""
def valid():
    """ValidVar"""
    num=int(input())
    for _ in range(num):
        text=input()
        if text in ("if" ,"else", "elif", "while","for","True","False","continue","break" ,"None"):
            print("Invalid")
        elif text in ("return" ,"is" ,"in" ,"and" ,"or" ,"from" ,"as" ,"pass" ,"not" ,"def"):
            print("Invalid")
        elif not text.isidentifier():
            print("Invalid")
        elif text.isidentifier() or "_" in text:
            print("Valid")
valid()
