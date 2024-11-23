# Busy Time Scheduling with Unlimited Capacity Machine

## Project Overview

This project implements a dynamic programming solution for the Busy Time Scheduling with an Unlimited Capacity Machine problem. The objective is to schedule a set of flexible jobs on a machine to minimize the total busy time, that is, the time the machine is actively running. The machine can process multiple jobs at the same time, and the goal is to optimize its usage based on the given constraints.

Each job is characterized by:

- **Release Time (r)**: The earliest time the job can start.
- **Deadline (d)**: The time by which the job must be completed.
- **Processing Time (p)**: The amount of time required to complete the job.

The program takes a set of jobs as input and outputs the start time for each job, ensuring that all constraints are satisfied.

## Algorithm Used

The solution utilizes a `dynamic programming algorithm` combined with a `greedy` approach to minimize the machine's busy time. The jobs are sorted by their release times, and the algorithm iteratively finds feasible start times while trying to maximize the overlap of jobs to reduce the total active time of the machine. The greedy component helps in choosing the optimal start time for each job to ensure the machine is busy for the least amount of time.

## Pseudocode and Running Time Analysis
```
function minimizeBusyTime(jobs):
    # Sort jobs by release time
    sort(jobs, by release time)
    n = length(jobs)
    start_times = array of size n, initialized to 0
    active_intervals = empty list

    for i from 0 to n - 1:
        (r, d, p) = jobs[i]
        start_time = r

        # Check active intervals to find the earliest available start time
        for each (end_time, job_index) in active_intervals:
            if end_time <= r:
                start_time = max(start_time, end_time)
                remove (end_time, job_index) from active_intervals

        # Update the start time for the job
        start_times[i] = start_time
        add (start_time + p, i) to active_intervals
        sort(active_intervals, by end time)

    return start_times

```
* Sorting the jobs initially takes **O(n logn)** time, where n is the number of jobs.
* Iterating over n jobs takes  **O(n)** time
* In the worst case, maintaining and sorting the active intervals can take O(n log n) time, since we need to insert and remove elements while keeping the list sorted.
* Overall time complexity: **O(n logn)**

## Folder Structure

The project folder contains the following structure:

- `main.py`: The main script to run the scheduling program.
- `sample/`: Contains two subfolders:
  - `instances/`: Folder where input files are stored. Input files are named `instanceXX.txt` (e.g., `instance00.txt`, `instance01.txt`, etc.).
  - `solutions/`: Folder where solution files are stored. Output files are named `solutionXX.txt` (e.g., `solution00.txt`, `solution01.txt`, etc.).

## Input and Output Format

- **Input Files**: Each input file contains:
  1. An integer `n` representing the number of jobs.
  2. `n` lines, each containing three integers: `r` (release time), `d` (deadline), and `p` (processing time).

  Example (`instance00.txt`):
<br>
5 
<br>
1 9 3<br> 
1 2 1<br>
4 8 2<br>
2 7 2<br>
5 9 2<br>


- **Output Files**: Each output file contains `n` lines, each with one integer representing the start time for each job.

    Example (`solution00.txt`):
<br>4<br> 1<br> 4<br> 4<br> 5


## How to Run the Project

### Prerequisites

- `Python 3.x`
- The required folders (`sample/instances` and `sample/solutions`) should exist.

### Running the Program

1. **Prepare Input Files**: Place the input files (`instanceXX.txt`) in the `sample/instances` folder.
2. **Run the Program**:
 ```
 python main.py
 ```

This command will read all input files from the sample/instances folder, process them, and store the output files in the sample/solutions folder.


3. **Run a Test with Example Input**:
 You can run a test with a specific instance file using the --test flag:
```
python main.py --test
```

This will use instance00.txt from the sample/instances folder to generate a solution.

## Example Usage

- Place your input files in the `simple/instances` folder.

- Run the program using `python main.py`.

- The solution files will be created in the `simple/solutions` folder with the corresponding start times for each job.

##  Notes

* The `solutions` folder should be empty before running the program to avoid outdated results.

* The correct output may not be unique; any output that satisfies the constraints will be considered correct.
