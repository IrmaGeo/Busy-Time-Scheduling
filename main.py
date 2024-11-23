import os

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        jobs = []
        for _ in range(n):
            r, d, p = map(int, file.readline().split())
            jobs.append((r, d, p))
    return jobs

def write_output(filename, start_times):
    with open(filename, 'w') as file:
        for s in start_times:
            file.write(f"{s}\n")

def minimize_busy_time(jobs):
    # Sort jobs by release time
    jobs.sort(key=lambda x: x[0])
    n = len(jobs)
    start_times = [0] * n

    # keep track of active intervals and minimize the total busy time
    active_intervals = []  # list of (end_time, job_index)

    for i, (r, d, p) in enumerate(jobs):
        # Find a slot to schedule the job starting at or after its release time
        start_time = r
        for end_time, job_index in active_intervals:
            if end_time <= r:
                start_time = max(start_time, end_time)
                active_intervals.remove((end_time, job_index))

        # Update the start time and active intervals
        start_times[i] = start_time
        active_intervals.append((start_time + p, i))
        active_intervals.sort()  # Keep the active intervals sorted by end time

    return start_times

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Busy Time Scheduling with Unlimited Capacity Machine")
    parser.add_argument('--input_folder', type=str, default='sample/instances', help='Folder containing input files')
    parser.add_argument('--output_folder', type=str, default='sample/solutions', help='Folder to store output files')
    parser.add_argument('--test', action='store_true', help='Run a test with example input')
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if args.test:
        # Example test run
        test_instance_file = os.path.join(input_folder, 'instance00.txt')
        test_solution_file = os.path.join(output_folder, 'solution00.txt')
        if os.path.exists(test_instance_file):
            jobs = read_input(test_instance_file)
            start_times = minimize_busy_time(jobs)
            write_output(test_solution_file, start_times)
            print(f"Test completed. Output written to {test_solution_file}")
        else:
            print(f"Test instance file {test_instance_file} not found.")
    else:
        # Iterate over all instances in the input folder
        for i in range(100):
            instance_file = os.path.join(input_folder, f"instance{i:02d}.txt")
            solution_file = os.path.join(output_folder, f"solution{i:02d}.txt")
            if os.path.exists(instance_file):
                jobs = read_input(instance_file)
                start_times = minimize_busy_time(jobs)
                write_output(solution_file, start_times)
                print(f"Processed {instance_file} -> {solution_file}")

if __name__ == "__main__":
    main()
