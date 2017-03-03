# LearnScrapy

# Python 网络数据采集

# 第一部分　创建爬虫

# 第1章　初见网络爬虫
## 1.1　网络连接
from urllib.request import urlopen
## 1.2　BeautifulSoup简介
pip install beautifulsoup4

# 第2章　复杂HTML解析
## 2.1　不是一直都要用锤子
* 寻找“打印此页”的链接，或者看看网站有没有HTML 样式更友好的移动版
* 寻找隐藏在JavaScript 文件里的信息
* 虽然网页标题经常会用到，但是这个信息也许可以从网页的URL 链接里获取
* 如果不只限于这个网站，那么你可以找找其他数据源。有没有其他网站也显示了同样的数据？网站上显示的数据是不是从其他网站上抓取后攒出来的？
## 2.2　再端一碗BeautifulSoup
CSS 的发明却是网络爬虫的福音
### 2.2.1　BeautifulSoup的find()和findAll()
### 2.2.2　其他BeautifulSoup对象
* BeautifulSoup 对象
* 标签Tag 对象
* NavigableString 对象
* Comment 对象* 
### 2.2.3　导航树
1. 处理子标签和其他后代标签
2. 处理兄弟标签
3. 父标签处理
## 2.4　正则表达式和BeautifulSoup
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
## 2.5　获取属性
myTag.attrs
myImgTag.attrs["src"]
## 2.6　Lambda表达式
soup.findAll(lambda tag: len(tag.attrs) == 2)
## 2.7　超越BeautifulSoup
* `lxml`
这个库（http://lxml.de/）可以用来解析HTML 和XML 文档，以非常底层的实现而闻名于世，大部分源代码是用C 语言写的。
虽然学习它需要花一些时间（其实学习曲线越陡峭，表明你可以越快地学会它），
但它在处理绝大多数HTML 文档时速度都非常快
* HTML parser
这是Python 自带的解析库（https://docs.python.org/3/library/html.parser.html）。
因为它不用安装（只要装了Python 就有），所以可以很方便地使用

