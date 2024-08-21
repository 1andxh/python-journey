from urllib import request
from bs4 import BeautifulSoup
import json
import csv

# sample url
site_url = 'https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0CRDCXRK2/ref=sr_1_1?dib=eyJ2IjoiMSJ9.SqYVDwllc6ujKR9mC9TCwSi4N3K0tfpnqP6TEtar2QAyFu7RJBZgFrMdZhMPu8vWIPyb1MONN8DVVA0jh7-whgX5W-M2IyUayr5i36eVnMLv2rzVwndr0x3vciVOtySgQhSoqERoWPXnlxqo9puqRlerE9_4DfqRGfoo9jzF_vISDX_J4QIHuDknIgfb581gl7ko3rd7KnehZhhI-dxNzO9csIlKPdRwZ9Zvol16UDY.7ueFhKIvzMhnkpFdtCXnXvHrxV5r5c7JYMW_2Rp9mpU&dib_tag=se&keywords=gaming+laptops&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=YY4YFND3BR7VK5J92H2B&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1723126113&sr=8-1'

# open page
page = request.urlopen(site_url)

# beautiful soup object
soup = BeautifulSoup(page, 'html.parser')

# isolate the  main content block
content = soup.article

# create an empty list for dictionary items
links_list = []

for link in content.soup.find_all('div'):
# try to get the href ,image url and text
    try:
        url = link.get('href')
        img = link.img.get('img')
        text = link.span.text
        links_list.append({'url': url, 'img': img, 'text': text})
    except AttributeError:
        pass

# save as json
with open('links.json', 'w', encoding='utf-8') as links_file:
    json.dump(links_list, links_file, ensure_ascii=False)

# save as csv 
with open('links.csv', 'w', newline= ' ') as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerow(['url', 'img', 'text'])
    for row in links_list:
        csv_writer.writerow([str(row['url']),str(row['img']),str(row['text'])])

print(content.prettify())
print('done!')