"""
数据定义类
"""
class Record:
    def __init__(self, xg, yg, zg, aox, aoy, aoz):

        self.xg = xg            #x轴加速度
        self.yg = yg            #y轴加速度
        self.zg = zg            #z轴加速度
        self.aox = aox          #x轴角度
        self.aoy = aoy          #y轴角度
        self.aoz = aoz          #z轴角度

    def __str__(self):
        return f'{self.xg},{self.yg},{self.zg},{self.aox},{self.aoy},{self.aoz}'
