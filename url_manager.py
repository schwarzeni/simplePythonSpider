
# coding: utf-8
# 作者：倪震洋
# 作用：对爬取网页的url进行管理

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    # 添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return

        if url not in self.new_urls and url not in  self.old_urls:
            self.new_urls.add(url)


    #批量添加url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)
    # 是否有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个新的url
    def get_new_url(self):
        # 从待获取的set中获取一个url
        new_url = self.new_urls.pop()
        # 将这个url添加至已访问的url中
        self.old_urls.add(new_url)
        # 返回这个url
        return new_url



