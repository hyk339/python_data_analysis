import requests as rq
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
quote = rq.get(url)

#print(quote)
#print(quote.content[:1000])

quote_html = BeautifulSoup(quote.content, 'html.parser')

## find 함수를 활용한 크롤링

#quote_div = quote_html.find_all('div', class_='quote')
#quote_span = quote_div[0].find_all('span', class_='text')
#print(quote_span[0].text)

# 리스트 컴프리헨션 : 값을 수집할때 쓰는게 일반적이다.
#[print(i.find_all('span', class_='text')[0].text) for i in quote_div]

## select 함수를 이용한 크롤링

# 명언 크롤링

quote_text = quote_html.select('div.quote > span.text')
quote_text_list = [i.text for i in quote_text]
#print(quote_text_list)

# 명언을 말한 사람 크롤링

quote_author=quote_html.select('div.quote > span > small.author')
quote_author_list = [i.text for i in quote_author]
#print(quote_author_list)

# 말한 사람에 대한 정보 링크 추출

quote_link = quote_html.select('div.quote > span > a')

[print('https://quotes.toscrape.com'+i['href']) for i in quote_link]







