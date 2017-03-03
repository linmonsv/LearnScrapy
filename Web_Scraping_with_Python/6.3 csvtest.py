from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)

""""
csvReader = csv.reader(dataFile)
for row in csvReader:
    #print(row)
    print("The album \"" + row[0] + "\" was released in " + str(row[1]))
"""

#csv.DictReader 会返回把CSV 文件每一行转换成Python 的字典对象返回，而不是列表对象，
#并把字段列表保存在变量dictReader.fieldnames 里，字段列表同时作为字典对象的键：
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
    print(row)

