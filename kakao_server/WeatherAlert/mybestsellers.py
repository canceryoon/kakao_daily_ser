import requests
import datetime
import json
from bs4 import BeautifulSoup

def getListType():
    return ({
            'message':  { 'text': 'Choose a List Type.' },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['신간', '주목할 만한 신간', '편집자 추천', '베스트셀러']
            } 
           })

def getBestSellers(listType):
    bookHdr = {'Content-Type': 'application/json; charset=utf-8', 'user-agent' : 'my-book-aladin'}
    bookUrl = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    bkey = 'ttbphoto96091009001'
    bookList = ["신간", "주목할 만한 신간", "편집자 추천", "베스트셀러"]
    bookListQT = ["ItemNewAll", "ItemNewSpecial", "ItemEditorChoice", "Bestseller"]
    queryType = bookListQT[bookList.index(listType)]

    bparams = {"ttbkey": bkey, "SearchTarget": "Book", "QueryType": queryType, "output": "JS", "Version": "20131101", "MaxResults": "5"}
    req = requests.get(bookUrl, headers=bookHdr, params=bparams).json()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    answer = now + '\n'

    for book in req["item"]:
        answer += "\n" + book["title"] + "\nauthor: " + book["author"] + "\nPrice(STD): " + str(book["priceStandard"]) + " won\nPrice(Sales): " + str(book["priceSales"]) + " won\n"

    return answer
