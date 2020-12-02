import os
from main import *
from selenium import webdriver
#TO RUN THIS FILE YOU NEED SELENIUM, BEAUTIFULSOUP, PANDAS, DATETIME, REGEX, AND OS
#JUST GO TO THE COMMAND LINE AND
#SET WORKING DIRECTORY TO THE DIRECTORY WITH BOTH MEDIUM_SCRAPER.PY AND SCRAPE_MASTER.PY
#THEN ENTER COMMAND "$python scrape_master.py"

driver = webdriver.Chrome("C:/Users/Faye/Downloads/chromedriver_win32/chromedriver")
#ADD THE TAGS TO SCRAPE HERE
tags = ["data-science"]


#ADD THE DATES TO SCRAPE HERE
yearstart=2015
monthstart=1
yearstop=2018
monthstop=12

#LOOPS THROUGH ALL LISTED-TAGS AND SCRAPES DATA OFF OF MEDIUM/TAG/archive
#SAVES THE FILES TO /TAG_SCRAPES/ IN CSV FORMAT
for tag in tags:
    scrape_tag(tag, yearstart, monthstart, yearstop, monthstop)
    print("Done with tag: ", tag)
print("done")
