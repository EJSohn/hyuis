# -*- coding: utf-8 -*-
# coded by eunjoo sohn. hanyang university

import re, sys, os, random, datetime
import mechanize
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

LOGIN_URL = 'http://www.weehan.com/index.php?mid=main2015_2&act=dispMemberLoginForm'

# my functions
def connectDB(db_path):
    engine = create_engine('sqlite:///'+db_path)
    metadata = MetaData(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, metadata, session

# mechanize settings
br = mechanize.Browser()
br.set_handle_robots(False)
cj = mechanize.CookieJar()
br.set_cookiejar(cj)
br.open(LOGIN_URL)

# ! my settings


# ! user login information
print('위한 userid : ')
userid = sys.stdin.readline()
print('위한 password : ')
pw = sys.stdin.readline()

# db settings
my_location = os.path.dirname(os.path.abspath('static'))
print('what is your db name?')
db_input = sys.stdin.readline()
db_location = os.path.join(my_location, db_input)
print(db_location)

engine, metadata, session = connectDB(db_location)
engine.text_factory = str
conn = engine.connect()
board = Table('board_board', metadata, autoload=True)


# ! search login form in browser source code
for form in br.forms():
    if form.attrs.get('id') == 'fo_member_login':
        br.form = form
        break

# ! login submit
br.form['user_id'] = userid
br.form['password'] = pw
logged_in = br.submit()
logincheck = logged_in.read()

# ! 사.수.다 게시판 입장
br.find_link(url='/free')
req = br.click_link(url='/free')
br.open(req)

for num in range(1, 11):
    # entering page
    url = '/index.php?mid=free&page={0}'.format(num)
    br.find_link(url=url)
    req = br.click_link(url=url)
    br.open(req)

    html_doc = br.response().read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 게시글 url 뽑기
    url_list = list()
    for post in soup.find_all(href=re.compile("document_srl"), limit=35):
        if '#' in post['href']:
            pass
        else :
            url_list.append(post['href'])
            #print(post['href'])

    # 뽑은 url 순회
    for post in url_list :
        db_dic = {}
        br.find_link(url=post)
        req = br.click_link(url=post)
        br.open(req)
        post_html = br.response().read()
        dsoup = BeautifulSoup(post_html, 'html.parser')

        # 제목뽑기
        for title in dsoup.find_all('h1'):
            a = title.a.string
            input_title = a
            print(type(input_title))
            db_dic['title'] = input_title
            print(a)
        # 내용뽑기
        for content in dsoup.find_all('div', attrs={'class': 'rd_body'}):
            input_content = str(content).decode('utf-8')
            print(type(input_content))
            db_dic['content'] = input_content
            print(input_content)
            print('-----------------------------------post-------------')

        # 글쓴 날짜 뽑기
        for date in dsoup.find_all('span', attrs={'class':'date'}, limit=1) :
            d1 = str(date.string)
            d2 = d1.split(' ')
            input_date = d2[0].split('.')
            db_dic['created_date'] = datetime.date(int(input_date[0]),int(input_date[1]),int(input_date[2]))
            print(input_date)

        # sqlalchemy data shoot!
        db_dic['user_id_id'] = 'admin'
        db_dic['category_id_id'] = random.randrange(1, 5)

        ins = board.insert().values(**db_dic)
        result = conn.execute(ins)

        print('dumping success')

        br.back()









