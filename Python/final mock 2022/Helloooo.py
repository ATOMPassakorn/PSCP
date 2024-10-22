"""Helloooo"""
def eng():
    """Helloooo"""
    text=input()
    vowel=["a","e","i","o","u"]
    found=0
    ans=""
    for i in text[::-1]:
        if i in vowel and not found:
            found+=1
            ans+=i*4
        else:
            ans+=i
    print(ans[::-1])
eng()
