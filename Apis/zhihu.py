#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliang
@license: Apache Licence 
@contact: liangliangyy@gmail.com
@site: http://www.lylinux.org
@software: PyCharm
@file: zhihu.py
@time: 2015/10/11 0:15
"""

from bs4 import BeautifulSoup
import urllib2
import urllib
import cookielib
import re

from ebooklib import epub

"""

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    'Host':'www.zhihu.com',
    'Origin':'http://www.zhihu.com',
    'Connection':'keep-alive',
    'CSP':'active',
    'X-Requested-With':'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Referer':'http://www.zhihu.com/people/zihaolucky/followers',
    'Content-Type':'application/x-www-form-urlencoded',
    }

postdata={
  '_xsrf':  '',
  'email':  'liangliangyy@gmail.com',
  'password': 'cll19900714',
  'rememberme':'y'
}

loginurl='http://www.zhihu.com/login'

class MyZhiHu():
    def __init__(self):
        self.__cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(self.__cj)
        opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def __UserAgent(self,url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/',
                     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                     }
        req = urllib2.Request(url)
        html = urllib2.urlopen(req).read()
        return html
    def __getxsrf__(self):
        html=self.__UserAgent('http://www.zhihu.com/#signin')
        soup=BeautifulSoup(html,"lxml")
        xsrf=soup.find(type='hidden')['value']
        return xsrf
    def LogIn(self):




    def test(self):
        xsrf=self.__getxsrf__()
        postdata['_xsrf']=xsrf
        print(xsrf)


if __name__=='__main__':
    zh=MyZhiHu()
    zh.test()"""



# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liangliang'

from bs4 import BeautifulSoup
import urllib2
import urllib
import cookielib
import re

from ebooklib import epub

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'http://www.zhihu.com',
    'Referer': 'http://www.zhihu.com/',
    'Connection': 'keep-alive',
    'Host': 'www.zhihu.com'
}

postdata = {
    '_xsrf': '',
    'email': 'liangliangyy@gmail.com',
    'password': 'cll19900714',
    'remember_me': 'true',
    'captcha': '98sx'

}

loginurl = 'http://www.zhihu.com/login/email'


class MyZhiHu():
    def __init__(self):

        self.headers = headers
        self.postdatastr = urllib.urlencode(postdata)
        self.loginurl = loginurl
        self.cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(self.cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        self.book = epub.EpubBook()
        # set metadata
        # book.set_identifier('id123456')
        self.book.set_title('Sample book')
        self.book.set_language('cn')

        self.book.add_author('Author Authorowski')
        self.book.add_author('Danko Bananko', file_as='Gospodin Danko Bananko', role='ill', uid='coauthor')
        xsrf = self.__getxsrf()

        postdata['_xsrf'] = xsrf
        print(postdata['_xsrf'])

    def __getxsrf(self):

        requrl = 'http://www.zhihu.com/#signin'
        html = urllib2.urlopen(requrl).read()
        reg = r'name="_xsrf" value="(.*)"/>'
        pattern = re.compile(reg)
        result = pattern.findall(html)
        xsrf = result[0]
        return xsrf

    def __getcheckcode(self, thehtml):
        soup = BeautifulSoup(thehtml,"lxml")
        div = soup.find('div', {'class': 'js-captcha captcha-wrap'})
        if div is not None:
            imgsrc = div.find('img')
            imglink = imgsrc.get('src')
            if imglink is not None:
                imglink = 'http://www.zhihu.com' + imglink
                imgcontent = urllib2.urlopen(imglink).read()
                with open('checkcode.gif', 'wb') as code:
                    code.write(imgcontent)
                return True
            else:
                return False
        return False

    def __loginzhihu(self):

        # h = urllib2.urlopen(loginurl)
        request = urllib2.Request(loginurl, self.postdatastr, self.headers)
        response = urllib2.urlopen(request)
        txt = response.read()
        if self.__getcheckcode(txt):
            checkcode = raw_input('input checkcode:')
            self.postdata['captcha'] = checkcode
            self.__loginzhihu()
        else:
            # self.__loginzhihu()
            print('login ok')

    def __useragent(self, url):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://baidu.com/'}
        req = urllib2.Request(url, headers=i_headers)
        html = urllib2.urlopen(req).read()
        return html

    def login(self):

        self.__loginzhihu()

    def EnterQuestion(self, url):
        html = self.__useragent(url)
        soup = BeautifulSoup(html,"lxml")
        questiontitle = soup.title.string
        print(questiontitle)
        i = 0
        for div in soup.findAll('div', {'class': ' zm-editable-content clearfix'}):
            i += 1
            filename = 'chap_' + str(i) + '.xhtml'
            print(filename)
            c1 = epub.EpubHtml(title=filename, file_name=filename, lang='zh')
            c1.content = div
            self.book.add_item(c1)
            self.book.toc = (epub.Link(filename, filename, 'intro'),
                             (epub.Section('Simple book'),
                              (c1,))
                             )

        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())
        self.book.spine = ['nav', c1]

    def __resetimg(self,div):
        pass



    def GetCollection(self):
        html = self.__useragent('http://www.zhihu.com/collections')
        soup = BeautifulSoup(html,"lxml")
        print(soup.title.string)
        self.EnterQuestion('http://www.zhihu.com/question/28636966')
        epub.write_epub('test1.epub', self.book, {})
    def DealAnswers(self,url):

        book = epub.EpubBook()

        # add metadata
        book.set_identifier('sample123456')
        book.set_title('Sample book')
        book.set_language('zh')

        book.add_author('Aleksandar Erkalovic')

        img=urllib2.urlopen('https://pic2.zhimg.com/fcf92348d_l.jpg').read()
    # add cover image
        book.set_cover("image.jpg", img)

    # intro chapter
        c1 = epub.EpubHtml(title='Introduction', file_name='intro.xhtml', lang='hr')
        c1.content=u'<html><head></head><body><h1>Introduction</h1><p>Introduction paragraph where i explain what is happening.</p></body></html>'

    # about chapter
        c2 = epub.EpubHtml(title='About this book', file_name='about.xhtml')
        c2.content='<h1>About this book</h1><p>Helou, this is my book! There are many books, but this one is mine.</p><p><img src="https://pic3.zhimg.com/1487556ad3285d29eadbf62acd19cd96_b.jpg" alt="Cover Image"/><img src="https://pic3.zhimg.com/1487556ad3285d29eadbf62acd19cd96_b.jpg" alt="Cover Image"/></p>'

    # add chapters to the book
        book.add_item(c1)
        book.add_item(c2)



        html=self.__useragent(url)
        soup=BeautifulSoup(html,"lxml")
        questiontitle = soup.title.string
        questiontext=soup.find(attrs={"id" : "zh-question-detail"}).find(attrs={"class" : "zm-editable-content"})

        question=epub.EpubHtml(title=questiontitle,file_name='question.xhtml',lang='zh');
        question.content=questiontext
        book.add_item(question)


        print(questiontext)

        answerdiv=soup.find(attrs={"id" : "zh-question-answer-wrap"})

        itemlist=['nav']
        itemlist.append(c1)
        itemlist.append(c2)
        i=0
        for div in answerdiv.findAll(attrs={"class" : "zm-editable-content clearfix"}):
            i+=1
            print div
            item=epub.EpubHtml(title=str(i)+'title',file_name=str(i)+'answer.xhtml',lang='zh')
            item.content='<html><head></head><body>'+str(div)+'</body></html>'
            book.add_item(item)
            itemlist.append(item)


        itemtuple=tuple(itemlist)

        book.toc = (epub.Link('question.xhtml', 'Introduction', 'intro'),
                 (epub.Section('Languages'),
                 itemtuple)
                )

        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        book.spine=itemlist
        epub.write_epub('test.epub', book, {})
if __name__ == '__main__':
    zh = MyZhiHu()
    zh.login()
    url='http://www.zhihu.com/question/26584441'
    zh.DealAnswers(url)

