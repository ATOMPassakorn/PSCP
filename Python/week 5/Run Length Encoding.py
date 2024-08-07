"""Run Length Encoding"""
def encoding():
    """Run Length Encoding"""
    text=input()
    count=1
    encode=""
    for i in range(1,len(text)):
        if text[i]==text[i-1]:
            count+=1
        else:
            encode+=str(count)+text[i-1]
            count=1
    encode+=str(count)+text[-1]
    print(encode)
encoding()
