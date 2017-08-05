import scrapy
from scrapy import Spider
from edulist.items import EdulistItem
from bs4 import BeautifulSoup

base_url = 'http://www.ruyile.com/xuexiao/'

class schoolSpider(Spider):
    name = 'edulist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request(base_url, headers=self.headers)

    def parse(self, response):

        req = []

        soup = BeautifulSoup(response.text, 'lxml')
        next_url = soup.find('a', text='下一页')
        print(next_url)

        if next_url:
            print(next_url['href'])
            r = scrapy.Request(next_url['href'], headers=self.headers, callback=self.parse)
            req.append(r)

        schools = soup.findAll('div', {"class": 'sk'})
        for school in schools:
            print(school)
            url = school.find('a')['href']
            print("school url" + url)
            r = scrapy.Request(url, callback=self.parse_item, headers=self.headers)
            req.append(r)

        return req

    def parse_item(self, response):

        item = EdulistItem()
        soup = BeautifulSoup(response.text, 'lxml')

        infos = soup.find('div', {'class': 'xxsx'}).children

        item["name"] = soup.find('div', {'class': 'stk'}).get_text().replace("\n", "")
        item['desc'] = soup.find('div', {'class': 'jj'}).get_text()
        item['area'] = ''
        item['property'] = ''
        item['professional'] = ''
        item['belong_to'] = ''
        item['is_211'] = ''
        item['is_985'] = ''
        item['is_keypoint'] = ''
        item['is_independent'] = ''
        item['is_direct'] = ''
        item['is_graduate'] = ''
        item['level'] = ''
        item['category'] = ''
        item['phone'] = ''
        item['email'] = ''
        item['website'] = ''
        item['address'] = ''
        item['postcode'] = ''

        for info in infos:
            tag = info.find('strong').get_text()
            if tag == "所属地区":
                item['area'] = info.get_text().replace('所属地区：', '')

            if tag == "学校性质":
                item['property'] = info.get_text().replace('学校性质：', '')

            if tag == "专业类型":
                item['professional'] = info.get_text().replace('专业类型：', '')

            if tag == "隶属于":
                item['belong_to'] = info.get_text().replace('隶属于：', '')

            if tag == "211工程":
                item['is_211'] = info.get_text().replace('211工程：', '')

            if tag == "985工程":
                item['is_985'] = info.get_text().replace('985工程：', '')

            if tag == "国家重点学科":
                item['is_keypoint'] = info.get_text().replace('国家重点学科：', '')

            if tag == "独立学院":
                item['is_independent'] = info.get_text().replace('独立学院：', '')

            if tag == "教育部直属":
                item['is_direct'] = info.get_text().replace('教育部直属：', '')

            if tag == "开设研究生院":
                item['is_graduate'] = info.get_text().replace('开设研究生院：', '')

            if tag == "学校级别":
                item['level'] = info.get_text().replace('学校级别：', '')

            if tag == "学校类型":
                item['category'] = info.get_text().replace('学校类型：', '')

            if tag == "招生电话":
                item['phone'] = info.get_text().replace('招生电话：', '')

            if tag == "学校网址":
                item['website'] = info.get_text().replace('学校网址：', '')

            if tag == "学校邮箱":
                item['email'] = info.get_text().replace('学校邮箱：', '')

            if tag == "学校地址":
                item['address'] = info.get_text().replace('学校地址：', '')

            if tag == "邮政编码":
                item['postcode'] = info.get_text().replace('邮政编码：', '')

        yield item