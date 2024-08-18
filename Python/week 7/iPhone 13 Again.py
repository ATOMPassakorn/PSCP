"""iPhone 13 Again"""
def iphone(serie,size):
    """iphone"""
    if serie=="iPhone 13 mini":
        print(mini(serie,size))
    elif serie=="iPhone 13":
        print(normal(serie,size))
    elif serie=="iPhone 13 Pro":
        print(pro(serie,size))
    elif serie=="iPhone 13 Pro Max":
        print(pro_max(serie,size))
    else:
        print("Not Available")

def mini(serie,size):
    """mini"""
    if serie=="iPhone 13 mini":
        if size=="128 GB":
            return 25900
        if size=="256 GB":
            return 29900
        if size=="512 GB":
            return 37900
    return "Not Available"

def normal(serie,size):
    """normal"""
    if serie=="iPhone 13":
        if size=="128 GB":
            return 29900
        if size=="256 GB":
            return 33900
        if size=="512 GB":
            return 41900
    return "Not Available"

def pro(serie,size):
    """normal"""
    if serie=="iPhone 13 Pro":
        if size=="128 GB":
            return 38900
        if size=="256 GB":
            return 42900
        if size=="512 GB":
            return 50900
        if size=="1 TB":
            return 58900
    return "Not Available"

def pro_max(serie,size):
    """normal"""
    if serie=="iPhone 13 Pro Max":
        if size=="128 GB":
            return 42900
        if size=="256 GB":
            return 46900
        if size=="512 GB":
            return 54900
        if size=="1 TB":
            return 62900
    return "Not Available"
iphone(input(),input())
