"""Olympic"""
def get_value(item):
    """sort_function"""  # sort by values then alpha
    return (-int(item[1]), -int(item[2]), -int(item[3]), item[0])

def main(n):
    """main"""
    lst_data = []
    for _ in range(n):
        data = input().split()  # Create list of data
        lst_data.append(data)
    lst_data.sort(key=get_value)  # Sort the data

    rank = 1
    result_rank = 1
    prev_medals = None  # Keep track of previous medals

    for i, country_data in enumerate(lst_data):
        current_medals = (int(country_data[1]), int(country_data[2]), int(country_data[3]))
        # Use generator expression in sum
        total = sum(int(country_data[j]) for j in range(1, 4))

        if i > 0 and current_medals == prev_medals:
            print(
                f"{result_rank} {country_data[0]} {country_data[1]} {country_data[2]} "
                f"{country_data[3]} {total}"
            )
        else:
            print(
                f"{rank} {country_data[0]} {country_data[1]} {country_data[2]} "
                f"{country_data[3]} {total}"
            )
            result_rank = rank
        prev_medals = current_medals
        rank += 1
main(int(input()))
