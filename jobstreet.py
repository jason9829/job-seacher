

# Desc: Create the url for the specific search term for Job Street
# Param: Search term (job)
# Retval: Url with the search term
def getJobStreetUrl(searchTerm):
    searchTerm = searchTerm.replace(" ", "+")
    return "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?ojs=10&key=" + searchTerm