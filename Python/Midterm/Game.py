"""Game"""
def game():
    """Game"""
    a_score=int(input())
    b_score=int(input())
    if a_score%3 == b_score%3:
        print(a_score%3)
    else:
        print("Error")
game()
