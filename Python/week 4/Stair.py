"""Stair"""
def stair():
    """Stair"""
    height=int(input())
    steps=int(input())
    count=0
    current_height=0
    for _ in range(steps):
        stair_height=int(input())
        if current_height+stair_height>height:
            count+=1
            current_height=stair_height
            if current_height>height:
                print("NO")
                return
        else:
            current_height+=stair_height
    if current_height>=0:
        count+=1
    print(count)
stair()
