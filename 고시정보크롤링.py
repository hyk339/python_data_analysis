import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
url = 'https://kind.krx.co.kr/disclosure/todaydisclosure.do'
payload = {
    'method': 'searchTodayDisclosureSub',
    'currentPageSize':'15',
    'pageIndex': '1',
    'orderStat': 'D',
    'forward': 'todaydisclosure_sub',
    'chose': 'S',
    'todayFlag': 'Y', 
    'selDate': '2025-05-09'
}

data = rq.post(url, data=payload)
html = BeautifulSoup(data.content, 'html.parser')

html_unicode = html.prettify()
tbl = pd.read_html(StringIO(html.prettify()))
print(tbl[0].head(10))