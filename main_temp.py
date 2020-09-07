# This file is used to test/ prototype functions
import scraper
import myGlobal
import jobstreet as jb

#keywordTyped = input()
keywordTyped = "Software"
soup = scraper.getBeautifulSoupInHtml(jb.getJobStreetUrl(keywordTyped))
data = jb.getJobSoupFromJobStreet(soup)
#  print('\nTotal Pages: ' + str(jb.getJobPostPages(soup)))
# print(jb.getNextPageUrl(soup, 2))
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