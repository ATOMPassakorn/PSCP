"""Runner"""
def runner_place(path_size, n):
    """Find the best runner"""
    def time_used(runner: list):
        """Sorting by their time used and the more velocity"""
        speed, init_point = runner[0], (path_size - runner[1])
        return (init_point/speed), -speed
    runner_list = []
    for _ in range(n):
        runner_data = input()
        runner_data = tuple(map(int, runner_data.split()))
        runner_list.append(runner_data)
    best_runner = sorted(runner_list, key=time_used)[0]
    print(runner_list.index(best_runner) + 1)
runner_place(int(input()), int(input()))
