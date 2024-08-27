"""US Interstate Number System"""
def us():
    """US Interstate Number System"""
    road=int(input())
    if 5 <= road <= 95:
        if not road%10:
            print("Horizontal Major Interstate")
            print(f"I-{road}")
        elif not road%5:
            print("Vertical Major Interstate")
            print(f"I-{road}")
        else:
            print("Others")
    elif 100 <= road <= 999:
        new=road%100
        if 5<= new<= 95:
            if not road//100%2 and (not new%5 or not new%10):
                print("Even Minor Interstate")
                print(f"I-{new}")
            elif road//100%2 and (not new%5 or not new%10):
                print("Odd Minor Interstate")
                print(f"I-{new}")
            else:
                print("Others")
        else:
            print("Others")
    else:
        print("Others")
us()
