
# coding: utf-8
#作者：倪震洋
#作用：对相应url的html页面的源代码进行下载

import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()