
import datetime
import urllib.request
from bs4 import BeautifulSoup

def title_from_url(url):
    page = urllib.request.urlopen(url)
    html = BeautifulSoup(page.read(), "html.parser")
    title = html.title.string[:-10]
    return title

#create class that has a date, link (and eventually title)
class Video:
    def __init__(self, url, date_string):
        #convert datestring to date
        self.url = url
        self.date_string = date_string
        self.date = datetime.datetime.strptime(date_string, "%b %d, %Y, %I:%M:%S %p %Z ")
        self.freq = 1

global url_to_object
url_to_object = {}

def populate_url_to_object():
    f = open("link_and_date.txt", "r")
    last_line = ''
    for line in f:
        if "watch" in last_line and "AEDT" in line:        
            url = last_line.rstrip()
            date_string = line

            date = datetime.datetime.strptime(date_string, "%b %d, %Y, %I:%M:%S %p %Z ")
            
            #check if exists in dict
            if url in url_to_object:
                url_to_object[url].freq += 1

            #if not, add
            else:
                curr_vid = Video(url, date_string)
                url_to_object[url] = curr_vid
            
        last_line = line

def get_dict_for_month_and_year(month, year):
    f = open("link_and_date.txt", "r")
    last_line = ''
    d = {}
    for line in f:
        if "watch" in last_line and "AEDT" in line:        
            url = last_line.rstrip()
            date_string = line

            date = datetime.datetime.strptime(date_string, "%b %d, %Y, %I:%M:%S %p %Z ")
            
            if date.month == month and date.year == year:
                #check if exists in dict
                if url in d:
                    d[url].freq += 1

                #if not, add
                else:
                    curr_vid = Video(url, date_string)
                    d[url] = curr_vid
            
        last_line = line

    return d
def get_dict_for_year(year):
    f = open("link_and_date.txt", "r")
    last_line = ''
    d = {}
    for line in f:
        if "watch" in last_line and "AEDT" in line:        
            url = last_line.rstrip()
            date_string = line

            date = datetime.datetime.strptime(date_string, "%b %d, %Y, %I:%M:%S %p %Z ")
            
            if date.year == year:
                #check if exists in dict
                if url in d:
                    d[url].freq += 1

                #if not, add
                else:
                    curr_vid = Video(url, date_string)
                    d[url] = curr_vid
            
        last_line = line

    return d

def print_url_object(vid):
#    print("url:   ", vid.url)
    print("title: ", title_from_url(vid.url))
    print("freq:  ", vid.freq)

def print_vid_dict(d, num):
    counter = 0;
    sorted_d = sorted(d.items(), key=lambda x:x[1].freq, reverse=True)
    for obj_tuple in sorted_d:
        vid = obj_tuple[1]
        if  counter < num:
            print_url_object(vid)
        counter += 1

def print_vid_list(l):
    for vid in l:
        print_url_object(vid)


def print_top_3_from_each_month():
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    years = [2019, 2020]
    num_to_month = "january feburary march april may june july august september october november december".split(" ")
    for year in years:
        print("   ~~~{}~~~".format(year))
        for month in months:
            print("   ~~~{}~~~".format(num_to_month[month-1]))
            top_vids = get_dict_for_month_and_year(month,year)
            print_vid_dict(top_vids, 3)

#print top 5 songs from whole year?
def youtube_wrapped(year):
    print("TOP 5 SONGS FROM WHOLE YEAR")
    vids_from_year = get_dict_for_year(year)
    print_vid_dict(vids_from_year,5)
    
    


populate_url_to_object()

print_top_3_from_each_month()
#youtube_wrapped(2020)

#print(url_freq)

#date_string = "Nov 24, 2020, 11:32:30 PM AEDT"

