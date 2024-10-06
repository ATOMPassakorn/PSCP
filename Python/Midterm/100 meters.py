"""100 meters"""
import math
def main():
    """finding gold, silver and bronze medal"""
    first = float(input())
    second = float(input())
    third = float(input())
    fourth = float(input())
    fifth = float(input())
    sixth = float(input())
    seventh = float(input())
    eighth = float(input())
    runners = (first, second, third, fourth, fifth, sixth, seventh, eighth)
    gold = 0
    silver = 0
    bronze = 0
    # """gold medal"""
    least = math.inf
    for place, runner in enumerate(runners, 1):
        if runner < least:
            least = runner
            gold = place
    # """silver medal"""
    least = math.inf
    for place, runner in enumerate(runners, 1):
        if place == gold:
            continue
        if runner < least:
            least = runner
            silver = place
    # """bronze medal"""
    least = math.inf
    for place, runner in enumerate(runners, 1):
        if place in (gold, silver):
            continue
        if runner < least:
            least = runner
            bronze = place
    print(gold, silver, bronze, sep=" ")
main()
