# -*- coding: gb2312   -*-
# jianSpider http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/jas/
# yuanfu created on 2018.9.26

import scrapy
import datetime
import smtplib
from email.mime.text import MIMEText

# to = ['yy18770711861@163.com']
to = ['450061754@qq.com']
host = "smtp.163.com"  # smtp服务器
user = "yy18770711861"  # 用户名
password = "######"  # 密码
postfix = "163.com"  # 后缀

class jianSp(scrapy.Spider):
    name = 'jianSp'
    allowed_domains = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/jas/']
    start_urls = [r'http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/jas/']
    extend_url = ['http://www.japrtc.gov.cn/jyxx/zfcg/dyby/jas/']
    extend_url2 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgs/jas/']
    extend_url3 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/jax/']
    extend_url4 = ['http://www.japrtc.gov.cn/jyxx/zfcg/dyby/jax/']
    extend_url5 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgs/jax/']
    extend_url6 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/thx/']
    extend_url7 = ['http://www.japrtc.gov.cn/jyxx/zfcg/dyby/thx/']
    extend_url8 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgs/thx/']
    extend_url9 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/jsx/']
    extend_url10 = ['http://www.japrtc.gov.cn/jyxx/zfcg/dyby/jsx/']
    extend_url11 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgs/jsx/']
    extend_url12 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgg/wax/']
    extend_url13 = ['http://www.japrtc.gov.cn/jyxx/zfcg/dyby/wax/']
    extend_url14 = ['http://www.japrtc.gov.cn/jyxx/zfcg/zbgs/wax/']
    start_urls.extend(extend_url)
    start_urls.extend(extend_url2)
    start_urls.extend(extend_url3)
    start_urls.extend(extend_url4)
    start_urls.extend(extend_url5)
    start_urls.extend(extend_url6)
    start_urls.extend(extend_url7)
    start_urls.extend(extend_url8)
    start_urls.extend(extend_url9)
    start_urls.extend(extend_url10)
    start_urls.extend(extend_url11)
    start_urls.extend(extend_url12)
    start_urls.extend(extend_url13)
    start_urls.extend(extend_url14)

    def parse(self, response):
        url = response.xpath('//div[@class="pagingList"]/ul/li/a/@href').extract()
        for url_f in url:
            # print response.url+ url_f[2:]
            yield scrapy.Request(response.url + url_f[2:], callback=self.parseContent, dont_filter=True)
    def parseContent(self, response):
        cTitle = ','.join(response.xpath('//div[@class="text-title"]/text()').extract()).strip()
        cTime = response.url[52:][:8]
        cContent = '\n'.join(response.xpath('//div[@class="text-main"]//text()').extract()).strip().replace('u3000','').replace('\n','').encode("GBK", 'ignore')
        date = datetime.datetime.now().date()
        detester = date.strftime('%Y-%m-%d').replace('-','')
        if cTime == detester and ('泰和' in cTitle or '万安' in cTitle or '吉水' in cTitle
                                  or '复合肥' in cTitle or '种子' in cTitle or '农业' in cTitle
                                  ):
        # if ('体育' in cTitle or '万安' in cTitle or '吉水' in cTitle
        #                           or '复合肥' in cTitle or '种子' in cTitle or '农业' in cTitle):
            titie = '吉安市公共资源交易网'
            message = cTitle + '\n\n'+ cContent

            def send_mail(to_list, sub, content):
                me = "xiaohuihui" + "<" + user + "@" + postfix + ">"
                msg = MIMEText(content, _subtype='plain', _charset='gb2312')
                msg['Subject'] = sub
                msg['From'] = me
                msg['To'] = ";".join(to_list)
                try:
                    server = smtplib.SMTP()
                    server.connect(host)
                    server.login(user, password)
                    server.sendmail(me, to_list, msg.as_string())
                    server.close()
                    return True
                except Exception, e:
                    print str(e)
                    return False

            if send_mail(to, titie , message):
                print "Suceed!"
            else:
                print "Failed!"



