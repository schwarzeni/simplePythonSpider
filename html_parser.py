
# coding: utf-8
# 作者：倪震洋
# 作用：对爬取的html页面进行分析
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):

    def _get_new_urls(self,page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = "http://baike.baidu.com" + new_url
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        # 创建一个字典用于存储信息
        res_data = {}

        res_data['url'] = page_url

        res_data['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()

        res_data['summary'] = soup.find('div', class_='lemma-summary').get_text()

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data