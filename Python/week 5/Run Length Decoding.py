"""Run Length Decoding"""
def decoding():
    """Run Length Decoding"""
    text=input()
    decode=""
    num=""
    lenght=len(text)
    for i in range(lenght):
        if text[i].isnumeric():
            num+=text[i]
        else:
            decode+=text[i]*int(num)
            num=""
    print(decode)
decoding()
