"""B - Fully pair?"""
def pair():
    """B - Fully pair?"""
    text=input()
    count=""
    full=""
    for i in text:
        if count.count(i)<1:
            count+=i
    for j in count:
        if text.count(j)%2:
            full+=j
    if not full:
        print("fully paired")
    else:
        print(full)
pair()
