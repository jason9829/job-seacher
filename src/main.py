import scraper
import myGlobal
import jobstreet as jb
import tkinter as tk
from tkinter import ttk


global keywordTyped

win = tk.Tk()
win.title("Job Search by JLXW")
win.iconbitmap(r'.\resources\img\suitcase.ico')

aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)



def buttonClicked():
    keywordTyped = str.get()
    #keywordTyped = "Software"
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


def enterReceived(self):
    buttonClicked()

ttk.Label(win, text="Enter a keyword").grid(column=0, row=0)

str= tk.StringVar()
strTyped = ttk.Entry(win, width=12, textvariable=str)
strTyped.grid(column=0, row=1)
strTyped.focus()  # Focus on the text bar once the GUI open (can directly key in at the search bar without
                  # mouse click on the search bar)

button = ttk.Button(win, text="Search", command=buttonClicked)
button.grid(column=1, row=1)
win.bind('<Return>', enterReceived)
win.mainloop()