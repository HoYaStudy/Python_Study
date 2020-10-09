from indeed import get_indeed_jobs
from stackoverflow import get_stackoverflow_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
stackoverflow_jobs = get_stackoverflow_jobs()

save_to_file(indeed_jobs + stackoverflow_jobs)