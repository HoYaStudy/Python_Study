import requests
from bs4 import BeautifulSoup

LIMIT = 50


def get_last_page(url, job):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    last_page = pages[-1]

    return last_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})
    company_link = company.find("a")
    if company_link is not None:
        company = company_link.string
    else:
        company = company.string

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    job_id = html["data-jk"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}",
    }


def get_jobs(url, last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scraping page from indeed: {page + 1} / {last_page}")
        result = requests.get(f"{url}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        divs = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for div in divs:
            jobs.append(extract_job(div))
    return jobs


def get_indeed_jobs(job):
    url = f"https://www.indeed.com/jobs?q={job}&limit={LIMIT}"
    last_page = get_last_page(url, job)
    jobs = get_jobs(url, last_page)
    return jobs