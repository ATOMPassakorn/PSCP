"""safe"""
def main():
    """cal"""
    text=input()
    password=input()
    count=0
    length=len(text)
    for i in range(length):
        diff=abs(ord(password[i])-ord(text[i]))
        if diff > 13:
            diff = 26-diff
        count+=diff
    print(count)
main()
