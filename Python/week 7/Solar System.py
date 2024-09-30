"""Solar System"""
def solar(orbit):
    """Finding the hottest and coolest planets"""
    orbit = " " + orbit + " "
    coolest = ""
    hottest = ""
    sun_index = orbit.find(" Sun ")
    left_spaces = 0
    right_spaces = 0
    for index, letter in enumerate(orbit):
        if index in (0, len(orbit)-1):
            continue
        if index <= sun_index and letter == " ":
            left_spaces += 1
        elif index > sun_index and letter == " ":
            right_spaces += 1
    if left_spaces > right_spaces:
        coolest += orbit[1:orbit.find(" ", 1)]
    elif right_spaces > left_spaces:
        coolest += orbit[orbit.rfind(" ", 0, -2)+1:-1]
    else:
        coolest += orbit[1:orbit.find(" ", 1)] + " " + orbit[orbit.rfind(" ", 0, -2)+1:-1]
    if sun_index:
        space = orbit.rfind(" ", 0, sun_index)
        hottest += orbit[space+1:sun_index] + " "
    space = orbit.find(" ", sun_index+5)
    hottest += orbit[sun_index+5:space]
    print(f"Hot: {hottest}")
    print(f"Cool: {coolest}")
solar(input())
