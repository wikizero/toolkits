# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
import time, datetime
import convertFunc
from models import *


class WorldSpider(scrapy.Spider):
    name = "world"
    # allowed_domains = ["https://www.jiaoyimao.com/g5043/"]
    start_urls = ['https://www.jiaoyimao.com/g5043/']

    def parse(self, response):
        content = response.css('.specialList li[name=goodsItem]')
        for i in content:
            link = i.css('.is-account a::attr(href)').extract_first(default='').strip()
            if link:
                yield Request(link, callback=self.parse_good, dont_filter=True)
                
        # 每5分钟抓取一次，只需抓取最新一页数据即可(2018/1/20)
        return False
        
        # 下一页 页面捉取
        for i in response.css('.page-btn'):
            text = i.xpath('text()').extract_first(default='').strip()
            link = i.xpath('@href').extract_first(default='').strip()
            if text == u'下一页>' and link:
                time.sleep(0.5)  # 睡眠0.5秒
                yield Request(link, callback=self.parse)

    def parse_good(self, response):
        url = response.url  # url varchar
        time_str = url.split('/')[-1].replace('.html', '')  # varchar int
        time_stamp = time_str[0:10]+'.'+time_str[10:]
        st = time.localtime(float(time_stamp))
        release_time = time.strftime('%Y-%m-%d %H:%M:%S', st)  # release_time datetime
        
        good_details = response.css('.goods-detail')
        title = good_details.css('.hd h1::text').extract_first(default='').strip()  # title varchar
        price = good_details.css('.bd .row .price::text').extract_first(default='').strip()
        price = float(price.replace(u'¥', ''))  # price float
        sell_times = good_details.css('.bd .buy-info .num::text').extract_first(default=0)  # sold_times int

        goods_info = response.css('.goods-intro')
        account_type = goods_info.css('.goods-properties .row:nth-child(2) a:last-child::text').extract_first(
            default='').strip()  # account_type  varchar
        level_info = goods_info.css('.goods-properties .row:nth-child(3) span')
        level = level_info.xpath('following::text()').extract_first(default='').strip()  # level int
        bind_info = goods_info.css('.goods-properties .row:nth-child(4) span')
        bind = bind_info.xpath('following::text()').extract_first(default='').strip()  # bind_info varchar
        description_info = goods_info.css('.goods-properties .row:nth-child(5) span')
        desc = description_info.xpath('following::text()').extract_first(default='').strip()  # desc varchar
 
        # 小于20级忽略掉(2018/1/20)
        if int(level) <= 20:
            return False  

        # img info
        images = response.css('.slider-items li')
        for i in images:
            img_link = i.css('a::attr(data-url)').extract_first(default='').strip()

        soul_num = convertFunc.func(title + desc)
        if not soul_num:  # 如果无法提取到魂数量 设置为0
            soul_num = 0
        cost_performance = soul_num / price  # cost_performance varchar

        # 判断商品状态
        if len(response.css('.btn-buy')) > 0:
            status = 'on-sale'  # 正在出售
        else:
            status_info = response.css('.btn-buy-dis::text').extract_first(default='').strip()
            if status_info == u'商品已下架':
                status = 'remove'
            elif status_info == u'商品已售完':
                status = 'sold-out'
            else:
                status = 'unknow'

        # create info
        # print time_str, sell_times, account_type, level, bind, desc, soul_num
        info = Info.select().where(Info.info_id == time_str)
        if info:
            Info.update(title=title, price=price, level=int(level), desc=desc, soul_num=soul_num, cost_performance=cost_performance,
                status=status, sold_date=datetime.datetime.now()).where(Info.info_id == time_stamp).execute()
        else:
            Info.create(info_id=time_str, url=url, release_date=release_time, title=title, price=price, sold_times=sell_times,
                        account_type=account_type, level=int(level), bind_info=bind, desc=desc, soul_num=soul_num,
                        cost_performance=cost_performance, status=status, sold_date=datetime.datetime.now())

        # status: on-sale  sold-out  remove  

        # if cost_performance >= 450:
        #     print release_time
        #     print title+desc, 'Price:', price, 'Level:', level
        #     print u'魂:', convertFunc.func(title+desc)
        #     print u'性价比:', convertFunc.func(title+desc)/price
        #     print url
        #     print '-'*100
