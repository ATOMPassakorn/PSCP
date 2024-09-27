"""Roman"""
def romannum():
    """Roman"""
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,\
             'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    number=input()
    lenght=len(number)
    ans=0
    for i in range(lenght):
        if i+1<len(number) and roman[number[i]]<roman[number[i+1]]:
            ans-=roman[number[i]]
        else:
            ans+=roman[number[i]]
    print(ans)
romannum()
