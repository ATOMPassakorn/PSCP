"""Bus Seat"""
def bus():
    """Bus Seat"""
    seat=int(input())
    row=int(input())
    select=int(input())
    count=0
    check=seat
    for i in range(1,seat+1):
        if count==2:
            print()
            count=0
        for _ in range(row):
            if check == select:
                print('XX',end=" ")
            else:
                print(f'{check:02}',end=" ")
            check += seat
        if i < seat:
            print()
        check = seat
        check -= i
        count += 1
bus()
