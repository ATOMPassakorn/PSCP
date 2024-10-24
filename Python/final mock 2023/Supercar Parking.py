"""Supercar Parking"""
def supercar(num):
    """Supercar Parking"""
    count = 0
    check = 0
    current = num[0]
    while True:
        if check+1 < len(num):
            if not check:
                if num[check+1] == '0' and current == '0':
                    count += 1
                    check += 2
                else:
                    check += 1
            elif num[check+1] == '0' and num[check-1] == '0':
                if current == '0':
                    count += 1
                    check += 2
                else:
                    check += 1
            else:
                check += 1
        elif check+1 == len(num):
            if num[check-1] == '0' and current == '0':
                count += 1
                check += 2
            break
        if check >= len(num):
            break
        current = num[check]
    print(count)
supercar(input())
