# Reference: https://www.edureka.co/blog/web-scraping-with-python/

import scraper
import myGlobal
import jobstreet as jb

while True:
    userInput = input("Please enter the key word to search")
    #userInput = "Manager"
    soup = scraper.getBeautifulSoupInHtml(jb.getJobStreetUrl(userInput))
    data = jb.getJobSoupFromJobStreet(soup)
    #print(data)

    i = 0
    temp = len(data.jobTitle)
    while temp != 0:
        print('\nJob Title: ' + data.jobTitle[i].contents[0])
        print('Company Name: ' + data.companyName[i].text.replace('\n', ''))
        print('Job Link: ' + data.jobLink[i].attrs['href'])
        print('Job Location: ' + data.jobLocation[i].next.getText())
        print('Job Posted: ' + data.jobPost[i].contents[0].lstrip())
        iterationNum = myGlobal.getIterationValue(i)
        i = i + iterationNum
        temp = temp - iterationNum
