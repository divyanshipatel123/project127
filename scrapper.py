from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import pandas as pd
import requests
# find td in every tr tag and if the td tag has the anchor tag then do the else if part
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

def scrap():
    templist_arr = []
    
    page = requests.get(start_url)
    soup = BeautifulSoup(page.text, "html.parser")
    star_table = soup.find("table")
    tr_tags = star_table.find_all("tr")  
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all("td")
        row = [i.text.rstrip() for i in td_tags]
        templist_arr.append(row)
                            
    star_name = []
    distance = [] 
    mass = []
    radius = []
    lum = []
    for i in range(1,len(templist_arr)):
        star_name.append(templist_arr[i][1])
        distance.append(templist_arr[i][3])
        mass.append(templist_arr[i][5])
        radius.append(templist_arr[i][6])
        lum.append(templist_arr[i][7])      

    df = pd.DataFrame(list(zip(star_name , distance , mass , radius , lum)) , columns = ["Star_Nmae" , "Distance" , "Star_Mass" , "Star_Radius" , "Star_luminosity"])
    df.to_csv("Brightest_star.csv")
scrap()