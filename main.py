# Reference: https://www.edureka.co/blog/web-scraping-with-python/

import scraper
import myGlobal
import jobstreet as jb

while True:
    userInput = input("Please enter the key word to search")
    soup = scraper.getBeautifulSoupInHtml(jb.getJobStreetUrl(userInput))

    jobTitle = soup.find_all('h2')
    companyTitle = soup.find_all('h3')
    jobLink = soup.findAll("a", {"class": "position-title-link"})
    jobLocation = soup.findAll("i", {"class": "icon icon-location"})
    jobPostTime = soup.findAll("span", {"class": "job-date-text text-muted"})
    i = 0
    temp = len(jobTitle)
    while temp != 0:
        print('\nJob Title: ' + jobTitle[i].contents[0])
        print('Company Title: ' + companyTitle[i].text.replace('\n', ''))
        print('Job Link: ' + jobLink[i].attrs['href'])
        print('Job Location: ' + jobLocation[i].next.getText())
        print('Post time: ' + jobPostTime[i].contents[0].lstrip())
        iterationNum = myGlobal.getIterationValue(i)
        i = i + iterationNum
        temp = temp - iterationNum
