"""Music Lover"""
def music():
    """Music Lover"""
    number=int(input())
    con={}
    for _ in range(number):
        queue=input().strip().split("-")
        artist=queue[0]
        song=queue[1]
        if artist in con:
            con[artist].append(song)
        else:
            con[artist]=[song]
    for i,j in con.items():
        print(i)
        for k in j:
            print(k)
music()
