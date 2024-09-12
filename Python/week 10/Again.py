"""Again"""
def again():
    """Again"""
    vowel="aeiou"
    text=input().replace(".","")
    text=text.split(" ")
    count=0
    ans=[]
    for i in text:
        count=0
        for j in i:
            if j in vowel:
                count+=1
                if count==2:
                    ans.append(i)
    if ans:
        ans.sort()
        for i in ans:
            print(i)
    else:
        print("Nope")
again()
