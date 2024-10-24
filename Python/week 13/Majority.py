"""Majority"""
def major():
    """Majority"""
    _=input()
    vote_num=int(input())
    candidate={}
    for _ in range(vote_num):
        vote=int(input())
        candidate[vote]=candidate.get(vote,0)+1
    most=max(candidate.values())
    index=list(candidate.values()).index(most)
    name=list(candidate.keys())[index]
    if most>vote_num/2:
        print(f"{name} {most}")
    else:
        print(f"0 {most}")
major()
