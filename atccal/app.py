import requests as rq
from bs4 import BeautifulSoup as  bs
import re
from google_api import api



def time_catch(diff):
    #url指定：Atcoderのurl
    url  =  'https://atcoder.jp/?lang=ja'
    res = rq.get(url)
    soup = bs(res.text,"html.parser")
    elems = soup.find_all("a")
    I = 0
  
    for i in range(len(elems)-1):
        if elems[i].has_attr("href"):
            if diff in elems[i].attrs['href']:
                I = i-1
                break

    tmp = elems[I].contents[0].contents[0]
    time_data_str  = re.split('[-: ]',tmp)
    time_data_str.pop(5)
    time_data_int = [int(s) for s in  time_data_str]
    return  time_data_int
 

    


if  __name__ == '__main__':
    time  = time_catch('abc')
    api(time)




