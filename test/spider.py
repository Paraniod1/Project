import requests
from lxml import etree
import time

if __name__ == '__main__':
    t1 = time.time()
    url = 'http://www.netbian.com/meinv/'
    resp = requests.get(url)
    resp.encoding = 'gbk'
    with open('index.html', 'wb') as f:
        f.write(resp.content)
    tree = etree.HTML(resp.content)

    node_list = tree.xpath('/html/body/div[2]/div[2]/div[3]/ul/li')

    sub_url_list = []
    for node in node_list:
        if len(node.xpath('./a/@href')) > 0:
            sub_url = node.xpath('./a/@href')[0]
        if len(node.xpath('./a/@href')) > 0:
            title = node.xpath('./a/b/text()')[0]
            sub_url_list.append((sub_url, title))
    #
    base_url = 'http://www.netbian.com/'
    for sub_url, title in sub_url_list:
        s_page = base_url + sub_url
        s_resp = requests.get(s_page)
        s_tree = etree.HTML(s_resp.content)
        img = s_tree.xpath('/html/body/div[2]/div[2]/div[3]/div/p/a/img/@src')[0]
        suffix = img.split('.')[-1]
        img_content = requests.get(img).content
        with open(f'./image/{title}.{suffix}', 'wb') as f:
            f.write(img_content)
            f.close()
    t2 = time.time()
    print(t2 - t1)
