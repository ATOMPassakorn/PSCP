"""Digit v2"""
def digit():
    """Digit v2"""
    num_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000
    }
    text_num=input().split()
    ans=0
    sigma=0
    for i in text_num:
        if i in num_dict:
            if num_dict[i]==100:
                sigma*=100
            elif num_dict[i]==1000:
                sigma*=1000
                ans+=sigma
                sigma=0
            else:
                sigma+=num_dict[i]
    ans+=sigma
    print(len(str(ans)))
digit()
