from lxml import html
import requests
from lxml import etree
from io import StringIO, BytesIO

link = 'https://ted.europa.eu/udl?uri=TED:NOTICE:325361-2018:TEXT:HU:HTML&src=0'
notice_page = requests.get(link)
tree = html.fromstring(notice_page.content)

notice_attributes = {}
notice_main_names = tree.xpath('//span[@class="timark"]/text()')

notice_page = (notice_page.content).decode('utf-8')

for notice_main_name in notice_main_names:
    
    #print(notice_main_name)
    
    length_name_start = notice_page.find(notice_main_name)
    #print(length_name_start)
    length_name_end = notice_page[length_name_start:].find('class="timark"')
    #print(length_name_end)
    tree_name_string = notice_page[length_name_start-59:length_name_start+length_name_end-6]
    #print(tree_name_string)
    
    #tree_name_etree= etree.fromstring(tree_name_string)
    
    parser = etree.HTMLParser()
    tree   = etree.parse(StringIO(tree_name_string), parser)
    
    notice_main_values = tree.xpath('//div[@class="txtmark"]/text()')
    #print(notice_main_values)
    notice_attributes[notice_main_name] =  notice_main_values
    
    #Elnevezés:
    if notice_main_name == 'Elnevezés:':
    
        notice_attributes[notice_main_name]
        length_name_start = notice_page.find(notice_main_name)
        length_name_end = notice_page[length_name_start:].find('class="timark"')
        tree_name_string = notice_page[length_name_start-59:length_name_start+length_name_end-6]
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(tree_name_string), parser)
    
        notice_main_values = tree.xpath('//div[@class="txtmark"]/p/text()')
        notice_attributes[notice_main_name] =  notice_main_values
    
    #CPVkód:
    if notice_main_name == 'Fő CPV-kód':
      
        notice_main_values = tree.xpath('//div[@class="txtmark"]/span/text()')
        notice_attributes[notice_main_name] =  notice_main_values[0]
        notice_main_values = tree.xpath('//div[@class="txtmark"]/span/@title')
        notice_attributes["Fő CPV-kód szöveges"] =  notice_main_values[0]
print(notice_attributes)
