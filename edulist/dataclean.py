from edulist.items import EdulistModel
from peewee import *
from peewee import SelectQuery
import re
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote, urlencode
import string
import sys
from multiprocessing import Pool

totalCount = 0

def dataClean():

    if EdulistModel.table_exists() == False:
        EdulistModel.create_table()

    schools = SelectQuery(EdulistModel).select().where(EdulistModel.postcode == '')
    print(schools.count())
    for school in schools:
        # category = school.category
        print(school.postcode)
        # category = category.replace(' ', '')
        # category = category.replace('\t', '')
        # category = category.replace('\n', '')
        # category = category.replace('\r', '、')
        # print(category)
        # school.category = category
        # school.save()

def updatePostCode(school):
    print(school.id)
    postcode_url = 'http://opendata.baidu.com/post/s?wd='
    address = quote(school.address.encode('gbk'))
    url = postcode_url + address + '&p=mini&rn=1'

    response = request.urlopen(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    results = soup.findAll('td')
    if len(results) > 0:
        postcode = results[0].get_text()
        if len(postcode) == 6:
            print(postcode)
            school.postcode = postcode
            school.save()

def fixData():
    # p = Pool(100)
    schools = SelectQuery(EdulistModel).select().where(EdulistModel.postcode == '')
    print(schools.count())
    # for school in schools:
    #     p.apply_async(updatePostCode, args=(school,))
    #
    # p.close()
    # p.join()

# dataClean()

fixData()