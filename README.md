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

#第8 章  自然语言处理

##8.1　概括数据

##8.2　马尔可夫模型

马尔可夫文字生成器（Markov text generator）

**维基百科六度分割：终结篇**

##8.3　自然语言工具包

自然语言工具包（Natural Language Toolkit，NLTK）就是这样一个Python 库，用于识别和标记英语文本中各个词的词性（parts of speech）。

###8.3.1　安装与设置

###8.3.2　用NLTK做统计分析

###8.3.3　用NLTK做词性分析

##8.4　其他资源

通过机器处理、分析和理解自然语言是计算机科学中最难的任务之一，

在这个领域中有数不清的专著和学术论文

#第9 章  穿越网页表单与登录窗口进行采集

##9.1　Python Requests库

##9.2　提交一个基本表单

大多数主流网站都会在它们的robots.txt 文件里注明禁止爬虫接入登录表单

##9.3　单选按钮、复选框和其他输入

无论表单的字段看起来多么复杂，仍然只有两件事是需要关注的：`字段名称`和`值`。

* 字段名称可以通过查看源代码寻找name 属性轻易获得。

* 而字段的值有时会比较复杂，有可能是在表单提交之前通过JavaScript 生成的。

取色器就是一个比较奇怪的表单字段，它可能会用类似#F03030 这样的值。

##9.4　提交文件和图像

表单字段uploadFile 的值

##9.5　处理登录和cookie

虽然cookie 为网络开发者解决了大问题，但同时却为网络爬虫带来了大问题。

你可以一整天只提交一次登录表单，但是如果你没有一直关注表单后来回传给你的那个cookie，

那么一段时间以后再次访问新页面时，你的登录状态就会丢失，需要重新登录

**HTTP基本接入认证**

##9.6　其他表单问题

验证码（CAPTCHA）

蜜罐（honey pot）、隐含字段（hidden field），以及其他保护网页表单的安全措施

#第10 章  采集JavaScript

通常，你在网上遇到的客户端语言只有两种：ActionScript（开发Flash 应用的语言）和JavaScript。

```javascript
<script>
    alert("This creates a pop-up using JavaScript");
</script>
```

##10.1  JavaScript简介

```javascript
<script>
function fibonacci(a, b){
    var nextNum = a + b;
    console.log(nextNum+" is in the Fibonacci sequence");
    if(nextNum < 100){
        fibonacci(b, nextNum);
    }
}
fibonacci(1, 1);
</script>
```

```javascript
<script>
var fibonacci = function() {
    var a = 1;
    var b = 1;
    return function() {
        var temp = b;
        b = a + b;
        a = temp;
        return b;
    }
}
var fibInstance = fibonacci();
console.log(fibInstance()+" is in the Fibonacci sequence");
console.log(fibInstance()+" is in the Fibonacci sequence");
console.log(fibInstance()+" is in the Fibonacci sequence");
</script>
```

**常用JavaScript库**

用Python 执行JavaScript 代码的效率非常低，既费时又费力，尤其是在处理规模较大的JavaScript 代码时。

如果有绕过JavaScript 并直接解析它的方法（不需要执行它就可以获得信息）会非常实用，可以帮你避开一大堆JavaScript 的麻烦事。

1. jQuery

一个网站使用jQuery 的特征，就是源代码里包含了jQuery 入口，比如：

```javascript
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
```

2. Google Analytics

```javascript
<!-- Google Analytics -->

<script type="text/javascript">

,,,,,,
```


如果一个网站使用了Google Analytics 或其他类似的网络分析系统，

而你不想让网站知道你在采集数据，就要确保把那些分析工具的cookie 或者所有cookie 都关掉

3. Google地图

##10.2　Ajax和动态HTML

如果提交表单之后，或从服务器获取信息之后，网站的页面不需要重新刷新，

那么你访问的网站就在用Ajax 技术

Ajax 全称是Asynchronous JavaScript and XML（异步JavaScript 和XML），

网站不需要使用单独的页面请求就可以和网络服务器进行交互

动态HTML（dynamic HTML，DHTML）也是一系列用于解决网络问题的技术集合。

DHTML 是用客户端语言改变页面的HTML 元素（HTML、CSS，或者二者皆被改变）。

那些使用了Ajax 或DHTML 技术改变/ 加载内容的页面，可能有一些采集手段，

但是用Python 解决这个问题只有两种途径：

* 直接从JavaScript 代码里采集内容，

* 或者用Python 的第三方库运行JavaScript，直接采集你在浏览器里看到的页面

**在Python中用Selenium执行JavaScript**

一个强大的网络数据采集工具，其最初是为网站自动化测试而开发的

PhantomJS 是一个“无头”（headless）浏览器。

它会把网站加载到内存并执行页面上的JavaScript，但是它不会向用户展示网页的图形界面

微软的XPath 语法页面（https://msdn.microsoft.com/en-us/enus/library/ms256471）

##10.3　处理重定向

服务器端重定向一般都可以轻松地通过Python 的urllib 库解决

客户端重定向却不能这样处理，除非你有工具可以执行JavaScript。

Selenium 可以执行这种JavaScript 重定向，

#第11 章  图像识别与文字处理

利用这种人类用户可以正常读取但是大多数机器人都没法读取的图片， 验证码（CAPTCHA）就出现了

将图像翻译成文字一般被称为光学文字识别（Optical Character Recognition，OCR）

##11.1　OCR库概述

###11.1.1　Pillow

尽管Pillow 算不上是图像处理功能最全的库，但是它拥有你需要使用的全部功能，除非你要用Python 重写一个Photoshop 或进行更加复杂的研究。

它也是一个文档健全且十分易用的库。

###11.1.2　Tesseract

Tesseract 是一个OCR 库，目前由Google 赞助（Google 也是一家以OCR 和机器学习技术闻名于世的公司）。

Tesseract 是目前公认最优秀、最精确的开源OCR 系统

###11.1.3　NumPy

NumPy 是一个非常强大的库，具有大量线性代数以及大规模科学计算的方法

NumPy 可以用数学方法把图片表示成巨大的像素数组，所以它可以流畅地配合Tesseract 完成任务

##11.2　处理格式规范的文字

利用Pillow 库，我们可以创建一个阈值过滤器来去掉渐变的背景色，只把文字留下来，

从而让图片更加清晰，便于Tesseract读取

Tesseract 最大的缺点是对渐变背景色的处理

**从网站图片中抓取文字**

通过给Tesseract 提供大量已知的文字与图片映射集，

经过训练Tesseract就可以“学会”识别同一种字体，而且可以达到极高的精确率和准确率，甚至可以忽略图片中文字的背景色和相对位置等问题。

##11.3　读取验证码与训练Tesseract

CAPTCHA（Completely Automated Public Turing test to tell Computers and Humans Apart）。

全自动区分计算机和人类的图灵测试

流行的PHP 内容管理系统Drupal 有一个著名的验证码模块（https://www.drupal.org/project/captcha），可以生成不同难度的验证码

**训练Tesseract**

##11.4　获取验证码提交答案¸

#第12 章  避开采集陷阱

##12.1　道德规范

* 在采集那些不想被采集的网站时，其实存在一些非常符合道德和法律规范的理由

* 指出每一种网络数据采集技术的缺点，你可以利用这些缺点保护自己的网站

* 和大多数程序员一样，我从来不相信禁止某一类信息的传播就可以让世界变得更和谐

##12.2　让网络机器人看起来像人类用户

###12.2.1　修改请求头

真正重要的参数就是User-Agent

###12.2.2　处理cookie

有一些浏览器插件可以为你显示访问网站和离开网站时cookie 是如何设置的。

EditThisCookie（http://www.editthiscookie.com/）就是我最喜欢的Chrome 浏览器插件之一

###12.2.3　时间就是一切

如果条件允许，尽量为每个页面访问增加一点儿时间间隔

##12.3　常见表单安全措施

###12.3.1　隐含输入字段值

用隐含字段阻止网络数据采集的方式主要有两种:

第一种是表单页面上的一个字段可以用服务器生成的随机变量表示。
如果提交时这个值不在表单处理页面上，服务器就有理由认为这个提交不是从原始表单页面上提交的，而是由一个网络机器人直接提交到表单处理页面的。
绕开这个问题的最佳方法就是，首先采集表单所在页面上生成的随机变量，然后再提交到表单处理页面

第二种方式是“蜜罐”（honey pot）。如果表单里包含一个具有普通名称的隐含字段（设置蜜罐圈套），
比如“用户名”（username）或“邮箱地址”（email address），设计不太好的网络机器人往往不管这个字段是不是对用户可见，直接填写这个字段并向服务器提交，这样就会中服务器的蜜罐圈套。
服务器会把所有隐含字段的真实值（或者与表单提交页面的默认值不同的值）都忽略，而且填写隐含字段的访问用户也可能被网站封杀。

总之，有时检查表单所在的页面十分必要，看看有没有遗漏或弄错一些服务器预先设定好的隐含字段（蜜罐圈套）。

如果你看到一些隐含字段，通常带有较大的随机字符串变量，那么很可能网络服务器会在表单提交的时候检查它们。

另外，还有其他一些检查，用来保证这些当前生成的表单变量只被使用一次或是最近生成的（这样可以避免变量被简单地存储到一个程序中反复使用）。

###12.3.2　避免蜜罐

因为Selenium 可以获取访问页面的内容，所以它可以区分页面上的可见元素与隐含元素。

通过is_displayed() 可以判断元素在页面上是否可见

##12.4　问题检查表

* 页面是空白的，缺少信息, JavaScript执行有问题。

* 提交表单或发出POST 请求，记得检查一下页面的内容

* “登录状态”异常，请检查你的cookie

* HTTP 错误，尤其是403 禁止访问错误，这可能说明网站已经把你的IP 当作机器人了

1. 速度不是特别快。快速采集是一种恶习

2. 修改你的请求头

3. 确认你没有点击或访问任何人类用户通常不能点击或接入的信息

4. 如果你用了一大堆复杂的手段才接入网站，考虑联系一下网管吧，告诉他们你的目的。

试试发邮件到webmaster@< 域名> 或admin@< 域名>，请求网管允许你使用爬虫采集数据。管理员也是人嘛！

#第13 章  用爬虫测试网站

##13.1　测试简介

**什么是单元测试**

每个单元测试用于测试一个零件（component）功能的一个方面

每个单元测试都可以完全独立地运行，一个单元测试需要的所有启动（setup）和卸载（teardown）都必须通过这个单元测试本身去处理。
单元测试不能对其他测试造成干扰，而且不论按何种顺序排列，它们都必须能够正常地运行。

每个单元测试通常至少包含一个断言（assertion）。

单元测试与生产代码是分离的。虽然它们需要导入然后在待测试的代码中使用，但是它们一般被保留在独立的类和目录中。

##13.2　Python单元测试

Python 的单元测试模块unittest

* 为每个单元测试的开始和结束提供setUp 和tearDown 函数
* 提供不同类型的“断言”语句让测试成功或失败
* 把所有以test_ 开头的函数当作单元测试运行，忽略不带test_ 的函数

**测试维基百科**

##13.3　Selenium单元测试

**与网站进行交互**

1. 鼠标拖放动作

2. 截屏

##13.4　Python单元测试与Selenium单元测试的选择

Python 的单元测试语法严谨冗长，更适合为大多数大型项目写测试，

而Selenium 的测试方式灵活且功能强大，可以成为一些网站功能测试的首选。

那么应该使用哪个呢？
答案是：不需要选择。

Selenium 可以轻易地获取网站的信息，而单元测试可以评估这些信息是否满足通过测试的条件。

因此，你没有理由拒绝把Selenium 导入Python 的单元测试，两者组合是最佳拍档。

#第14 章  远程采集

##14.1　为什么要用远程服务器

###14.1.1　避免IP地址被封杀

###14.1.2　移植性与扩展性

##14.2　Tor代理服务器

洋葱路由（The Onion Router）网络，常用缩写为Tor，是一种IP 地址匿名手段。

**PySocks**

PySocks 是一个非常简单的Python 代理服务器通信模块，它可以和Tor 配合使用

##14.3　远程主机

###14.3.1　从网站主机运行

大多数小型网络主机都会提供一个软件叫cPanel，提供网站管理和后台服务的基本管理功能和信息

如果你接入了cPanel，就可以设置Python 在服务器上运行

，，，

通过浏览器找到程序上传的位置（也可以写一个爬虫来自动做这件事情）就可以执行程序

###14.3.2　从云主机运行

##14.4　其他资源

Google Compute Engine

Python and AWS Cookbook

##14.5　勇往直前

**互联网其实就是一个用户界面不太友好的超级API**
