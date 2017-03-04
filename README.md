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
* Comment 对象

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

# 第3章　开始采集

## 3.1　遍历单个域名

## 3.2　采集整个网站
深网（deep Web）、暗网（dark Web）或隐藏网络（hidden Web）
遍历整个网站的网络数据采集有许多好处:
* 生成网站地图
* 收集数据

## 3.3　通过互联网采集

图3-1：从互联网上不同的网站采集外链的程序流程图

图3-2：收集内链和外链的程序流程图

## 3.4　用Scrapy采集

$scrapy startproject wikiSpider

#第4章　使用API
尽管目前不同的软件应用都有各自不同的API，但“API”经常被看成“网络应用API”。
一般情况下，程序员可以用HTTP 协议向API 发起请求以获取某种信息，API 会用XML
（eXtensible Markup Language， 可扩展标记语言） 或JSON（JavaScript Object Notation，
JavaScript 对象表示）格式返回服务器响应的信息
##4.1　API概述
https://console.developers.google.com/
http://freegeoip.net/json/50.78.253.58
{"ip":"50.78.253.58","country_code":"US","country_name":"美国","region_
code":"MA","region_name":"Massachusetts","city":"Chelmsford","zipcode":"01824",
"latitude":42.5879,"longitude":-71.3498,"metro_code":"506","area_code":"978"}
##4.2　API通用规则
###4.2.1　方法
利用HTTP 从网络服务获取信息有四种方式：
* GET
* POST
* PUT
* DELETE

GET 就是你在浏览器中输入网址浏览网站所做的事情

POST 基本就是当你填写表单或提交信息到网络服务器的后端程序时所做的事情

PUT 在网站交互过程中不常用，但是在API 里面有时会用到。PUT 请求用来更新一个对象或信息

DELETE 用于删除一个对象

###4.2.2　验证
```python
token = "<your api key>"
webRequest = urllib.request.Request("http://myapi.com", headers={"token":token})
html = urlopen(webRequest)
```
##4.3　服务器响应
大多数反馈的数据格式都是XML 和JSON
这几年，JSON 比XML 更受欢迎，主要有两个原因:
首先，JSON 文件比完整的XML `格式小`。
JSON 格式比XML 更受欢迎的另一个原因是网络技术的改变。
过去，服务器端用PHP和.NET 这些程序作为API 的接收端。
现在，服务器端也会用一些 `JavaScript` 框架作为API的发送和接收端

**API调用**

当使用GET 请求获取数据时，用URL 路径描述你要获取的数据范围，查询参数可以作为过滤器或附加请求使用

http://socialmediasite.com/users/1234/posts?from=08012014&to=08312014

有许多API 会通过文件路径（path）的形式指定API 版本、数据格式和其他属性

http://socialmediasite.com/api/v4/json/users/1234/posts?from=08012014&to=08312014

还有一些API 会通过请求参数（request parameter）的形式指定数据格式和API 版本
http://socialmediasite.com/users/1234/posts?format=json&from=08012014&to=08312014

##4.4　Echo Nest
The Echo Nest 音乐数据网站3 是一个用网络爬虫建立的超级给力的企业级案例

它的API 可以经非商业用途免费使用。

使用API 得有一个key，你可以在The Echo Nest 的注册

**几个示例**

##4.5　Twitter API
Twitter 的API 请求限制有两种方法：

每15 分钟15 次和每15 分钟180 次，由请求类型决定。

比如你可以1 分钟获取12 次（每15 分钟180 次的平均数）Twitter 用户基本信息，

但是1 分钟只能获取1 次（每15 分钟15 次的平均数）这些用户的关注者（follower）

###4.5.1　开始
注册
###4.5.2　几个示例
Python Twitter 库
##4.6　Google API
查看Google API 有两种方式。

一种方式是通过产品页面（https://developers.google.com/products/）

另一种方式是API 控制台（https://console.developers.google.com/）

###4.6.1　开始
建立自己的账号

如果你不限制允许使用API 的IP 地址——任何使用你的API key 调用你的API 都算成是你的消费，即使你并不知情。

###4.6.2　几个示例
##4.7　解析JSON数据
##4.8　回到主题
真正有意思的事情，是把多个数据源组合成新的形式，
或者把API 作为一种工具，从全新的视角对采集到的数据进行解释。
##4.9　再说一点API
API 具有“许多不同的软件都可以通过相同的API 分享数据”的特点

# 第5章  存储数据
数据库, 文件流（file stream）, 邮件

##5.1　媒体文件
* 只获取文件URL 链接，
* 或者直接把源文件下载下来。

##5.2　把数据存储到CSV
CSV（Comma-Separated Values，逗号分隔值）是存储表格数据的常用文件格式 

CSV 里留白（whitespace）也是很重要的：

每一行都用一个换行符分隔，

列与列之间用逗号分隔（因此也叫“逗号分隔值”）。

CSV 文件还可以用Tab 字符或其他字符分隔行，但是不太常见，用得不多

网络数据采集的一个常用功能就是获取HTML 表格并写入CSV 文件。

##5.3　MySQL

###5.3.1　安装MySQL

Mac OS X 的包管理器Homebrew

用默认选项安装MySQL 就可以，

不过有一个地方要注意：在Setup Type（类型设置）页面，

建议你选择“Server Only”（只选服务器）选项，这可以避免安装一堆微软的软件和库文件

###5.3.2　基本命令

习惯上写MySQL 语句的时候所有的MySQL 关键词都用大写

###5.3.3　与Python整合

最有名的一个库就是PyMySQL（https://github.com/PyMySQL/PyMySQL）。

###5.3.4　数据库技术与最佳实践

###5.3.5　MySQL里的“六度空间游戏”

##5.4　Email

#第6章　读取文档
互联网最基本的特征：作为不同类型文件的传输媒介
##6.1　文档编码
文档编码的方式通常可以根据文件的扩展名进行判断，虽然文件扩展名并不是由编码确定的，而是由开发者确定的
##6.2　纯文本
所以BeautifulSoup 库就没用了
**文本编码和全球互联网**
1. 编码类型简介
在UTF-8 设计过程中，设计师决定利用ASCII 文档里的“填充位”，
让所有以“0”开头的字节表示这个字符只用1 个字节，从而把ASCII 和UTF-8 编码完美地结合在一起
2. 编码进行时
<meta charset="utf-8" />
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
##6.3　CSV
Python 有一个超赞的标准库（https://docs.python.org/3.4/library/csv.html）可以读写CSV 文件
##6.4　PDF
PDFMiner3K 就是一个非常好用的库（是PDFMiner 的Python 3.x 移植版）
##6.5　微软Word和.docx
Word 文件从未打算让人频繁传递
.doc 文件格式。这种二进制格式很难读取，而且能够读取word 格式的软件很少
为了跟上时代，让自己的软件能够符合主流软件的标准，
微软决定使用Open Office 的类XML 格式标准，
此后新版Word 文件才与其他文字处理软件兼容，这个格式就是.docx。

# 第二部分  高级数据采集

#第7 章  数据清洗

##7.1　编写代码清洗数据

##7.2　数据存储后再清洗

“写个脚本”

第三方工具，像OpenRefine，不仅可以快速简单地清理数据，还可以让非编程人员轻松地看见和使用你的数据

1. 安装

OpenRefine 的独特之处在于虽然它的界面是一个浏览器，但实际上是一个桌面应用，必须下载并安装。

要使用OpenRefine，你得把数据转换成CSV 文件

2. 使用OpenRefine
