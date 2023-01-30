"""
读取维特智能上位机保存的txt文本
通过PyEcharts进行图形绘制
"""

from file_reader import FileReader, TextFileReader
from pyecharts.charts import Line

textFileReader = TextFileReader("E:/123.txt")       #文件路径
record_list = textFileReader.read_data()            #只读取了三轴加速度和角度，可额外添加
xg = []
yg = []
zg = []
aox = []
aoy = []
aoz = []
i = 0               #读取数据个数
s = 200             #数据读取频率/Hz
for record in record_list:
    i += 1
    xg.append(record.xg)
    yg.append(record.yg)
    zg.append(record.zg)
    aox.append(record.aox)
    aoy.append(record.aoy)
    aoz.append(record.aoz)

line = Line()
a = list(range(1, (1000//s)*i, 1000//s))
x = [str(x) for x in a]

line.add_xaxis(x)
line.add_yaxis("x轴角度", aox)
line.add_yaxis("y轴角度", aoy)
line.add_yaxis("z轴角度", aoz)

line.render()
