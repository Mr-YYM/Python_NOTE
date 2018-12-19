import re
import requests
import bs4

title_compile = re.compile("title='(.*)'\s?>(.*)(<\/a>)$")

res = requests.get('http://www.shuichan.cc/article_list-144-663.html')
res.encoding = 'gb2312'

with open('source.html', 'w') as f:
    f.write(res.text)

match_tables = title_compile.findall(res.text)
print('length:', len(match_tables))

for i, each in enumerate(match_tables):
    print("%d:\n %s"% (i, each[1]))
