def run_timing():
    run_times = []
    while True:
        user_input = input(f'Enter a run time: ')
        if (user_input):
            run_times.append(int(user_input))
        else:
            break
    print(f'Average run time is {sum(run_times)/len(run_times)} over {len(run_times)} runs.')

run_timing()