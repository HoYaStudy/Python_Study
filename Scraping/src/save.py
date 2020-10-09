import csv


def save_to_file(jobs):
    with open("jobs.csv", mode="w") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "company", "location", "link"])
        for job in jobs:
            writer.writerow(list(job.values()))