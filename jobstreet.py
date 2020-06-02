import url

TOTAL_NUMBER_OF_JOBS_LOCATION = 4
MAX_NUMBER_OF_JOBS_PER_PAGE = 20

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


# Desc: Get number of pages for job searched
# Param: Job soup
# Retval: Number of pages in int
def getJobPostPages(soup):
    temp = soup.findAll("span", {"class": "pull-right pagination-result-count"})
    temp = temp[0].contents[0].split(" ")
    noOfJobStr = temp[TOTAL_NUMBER_OF_JOBS_LOCATION]
    noOfJobPages = int(noOfJobStr)/MAX_NUMBER_OF_JOBS_PER_PAGE
    if isinstance(noOfJobPages, float):   # Float means extra pages
        return int(noOfJobPages) + 1
    else:
        return int(noOfJobPages)


# Desc: Change the URL of the job search to next page
# Param: Job soup and current page
# Retval: Url for next page
def getNextPageUrl(soup, currentPage):
    numOfJobPages = getJobPostPages(soup)
    temp = soup.findAll("a", {"id": "page_next"})
    if currentPage < numOfJobPages:  # If larger means it's error, if same means it's the last page
        return url.changeUrlQueryValue(temp[0].attrs['href'], 'pg', currentPage + 1)
    else:
        raise ValueError('getNextPageUrl(): Invalid pages received!')