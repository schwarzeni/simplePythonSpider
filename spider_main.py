# coding: utf-8

# 作者：倪震洋
# 作用：网页爬虫总入口

import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # html下载器
        self.downloader = html_downloader.HtmlDownloader()
        # html解析器
        self.parser = html_parser.HtmlParser()
        # 结果输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加新的url至url管理器
        self.urls.add_new_url(root_url)
        # 当url管理器中有带获取的url的时候
        while self.urls.has_new_url():

            try:

                # 获取这个url
                new_url = self.urls.get_new_url()
                # 打印获取第几个url
                print 'craw %d: %s' % (count, new_url)
                # 存储至下载器中
                html_cont = self.downloader.download(new_url)
                # 对已下载的url进行解析，获取数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将新获取的url们添加至url管理器, 批量添加
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                if count == 50:
                    break
                count = count + 1

            except:
                print 'craw failed'


        # 输出已收集的数据
        self.outputer.output_html()


if __name__ == "__main__":
    # 入口url
    root_url = "http://baike.baidu.com/item/Python?sefr=cr"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
