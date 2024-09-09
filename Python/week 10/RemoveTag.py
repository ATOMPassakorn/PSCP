"""RemoveTag"""
def tag():
    """RemoveTag"""
    text=input()
    while "<" in text or ">" in text:
        start=text.index("<")
        stop=text.index(">")+1
        text=text.replace(text[start:stop]," ")
    print(text.split())
tag()
