"""Socks"""
def socks():
    """Socks"""
    socks_lst = []
    socks_color = []
    socks_lst.extend(input())
    for color in socks_lst:
        if color not in socks_color:
            socks_color.append(color)
    socks_color.sort()
    result = []
    total_pairs = 0
    for i in socks_color:
        count = socks_lst.count(i)
        pairs = count // 2
        if pairs:
            result.extend([i * 2] * pairs)
            total_pairs += pairs
    if result:
        print(" ".join(result))
    else:
        print("None")
    print(total_pairs)
socks()
