import csv
import json
import chardet
import requests
from lxml import etree
url = "http://www.ceic.ac.cn/ajax/speedsearch?num=6&&page=1"
def download(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    }
    response=requests.get(url,headers=headers)
    encoding=chardet.detect(response.content)['encoding']
    html=response.content.decode(encoding)
    if response.status_code==200:
        return html

def parse_html(html):
    html=html['shuju']
    for item in html:
        yield {
            'CATA_ID':item['CATA_ID'],
            '震级(M)':item['M'],
            '发震时刻(UTF+8)':item['O_TIME'],
            '纬度':item['EPI_LAT'],
            '经度':item['EPI_LON'],
            '深度(千米)':item['EPI_DEPTH'],
            '参考位置':item['LOCATION_C'],
            '具体链接':f'http://news.ceic.ac.cn/{item["CATA_ID"]}.html'
        }
def save_to_csv(item):
    with open('最近一年的地震情况.csv','a',encoding='utf_8_sig',newline='') as f:
        fieldnames=['CATA_ID','震级(M)','发震时刻(UTF+8)','纬度','经度','深度(千米)','参考位置','具体链接']

        writer=csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(item)
def main(page):
    url=f'http://www.ceic.ac.cn/ajax/speedsearch?num=6&&page={page}'
    html=download(url)[1:-1]
    html=json.loads(html)
    for item in parse_html(html):
        save_to_csv(item)
if __name__=='__main__':
    for page in range(63):
        main(page)




# 解析页面源代码
# html_element = etree.HTML(response.text)
# texts = html_element.xpath('//*[@id="speedquery"]//td//text()')
# print(texts)
#

# 使用XPath查询获取文本内容