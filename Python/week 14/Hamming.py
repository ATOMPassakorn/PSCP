"""Hamming"""
def ham():
    """Hamming"""
    text1=input()
    text2=input()
    count=0
    for i,text in enumerate(text1):
        if text!=text2[i]:
            count+=1
    print(count)
ham()
