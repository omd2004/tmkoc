def job_scheduling(jobs):
    # Sort jobs by profit in decreasing order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find the maximum deadline
    max_deadline = max(job[0] for job in jobs)

    # Initialize the schedule (slots)
    schedule = [-1] * max_deadline  # -1 means slot is empty
    total_profit = 0

    # Assign jobs to slots
    for job in jobs:
        deadline, profit = job
        # Find a slot for this job (latest slot before its deadline)
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[i] == -1:
                schedule[i] = profit  # Assign job's profit to this slot
                total_profit += profit
                break

    return schedule, total_profit


# Example input: List of (deadline, profit) for each job
jobs = [(4, 20), (1, 10), (1, 40), (1, 30)]  # Format: (deadline, profit)

# Get the schedule and total profit
schedule, total_profit = job_scheduling(jobs)

print("Job Schedule (profit in each slot):", schedule)
print("Total Profit:", total_profit)
