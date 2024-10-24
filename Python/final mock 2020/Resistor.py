"""Resistor"""
def bandone(band1):
    """12"""
    color_values = {
        "Black": 0,
        "Brown": 1,
        "Red": 2,
        "Orange": 3,
        "Yellow": 4,
        "Green": 5,
        "Blue": 6,
        "Purple": 7,
        "Grey": 8,
        "White": 9,
    }
    return color_values.get(band1)

def bandtwo(band2):
    """12"""
    return bandone(band2)

def multi(band3):
    """multi"""
    multiplier_values = {
        "Black": 1,
        "Brown": 10,
        "Red": 100,
        "Orange": 1000,
        "Yellow": 10000,
        "Green": 100000,
        "Blue": 1000000,
        "Purple": 10000000,
        "Gold": 0.1,
        "Silver": 0.01,
    }
    return multiplier_values.get(band3)

def tol(band4):
    """tolerance"""
    tolerance_values = {
        "Brown": 0.01,
        "Red": 0.02,
        "Green": 0.005,
        "Blue": 0.0025,
        "Purple": 0.001,
        "Grey": 0.0005,
        "Gold": 0.05,
        "Silver": 0.1,
    }
    return tolerance_values.get(band4)

def main(band11, band22, band33, band44):
    """main"""
    band1 = bandone(band11)
    band2 = bandtwo(band22)
    band3 = multi(band33)
    band4 = tol(band44)
    if band1 is None or band2 is None or band3 is None or band4 is None:
        print("Error")
    else:
        ohm = (band1 * 10 + band2) * band3
        lower_bound = ohm * (1 - band4)
        upper_bound = ohm * (1 + band4)
        print(f"{lower_bound:.4f}\n{upper_bound:.4f}")
main(input(), input(), input(), input())
