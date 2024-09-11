"""Stair"""
def main():
    """Stair"""
    can = int(input())
    stair = int(input())
    steps = 0
    up = 0
    for _ in range(stair):
        h = int(input())
        if up + h > can:
            steps += 1
            up = h
            if up > can:
                print("NO")
                return
        else:
            up += h
    if up >= 0:
        steps += 1
    print(steps)
main()