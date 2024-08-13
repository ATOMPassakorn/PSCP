"""Nearer"""
def icecream():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    icetim = int(input())
    distance_a= abs(icetim-alice)
    distance_b=abs(icetim-bob)
    if distance_a==distance_b:
        print(f"Sundaes {distance_b}")
    elif distance_a>distance_b:
        print(f"Bob {distance_b}")
    elif distance_b>distance_a:
        print(f"Alice {distance_a}")
icecream()
