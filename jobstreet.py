
class JobStreetToken:
    def __init__(self):
        self.jobTitle = None
        self.companyName = None
        self.jobLocation = None
        self.jobLink = None
        self.jobPost = None


# Desc: Create the URL for the specific search term for Job Street
# Param: Search term (job)
# Retval: URL with the search term
def getJobStreetUrl(searchTerm):
    searchTerm = searchTerm.replace(" ", "+")
    return "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?ojs=10&key=" + searchTerm


# Desc: Get beautiful soup structures for Job Street data (one page)
# Param: Scraped Beautiful Soup
# Retval: Job Street data
def getJobSoupFromJobStreet(soup):
    soupList = JobStreetToken()
    soupList.jobTitle = soup.find_all('h2')
    soupList.companyName = soup.find_all('h3')
    soupList.jobLink = soup.findAll("a", {"class": "position-title-link"})
    soupList.jobLocation = soup.findAll("i", {"class": "icon icon-location"})
    soupList.jobPost = soup.findAll("span", {"class": "job-date-text text-muted"})
    return soupList
