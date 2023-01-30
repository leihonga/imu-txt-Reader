"""
文件读取类定义
"""
from data_reader import Record


class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据并转换为Record对象，将其封装到list中返回"""
        pass


class TextFileReader(FileReader):
    # 读取维特智能上位机保存的txt文本
    def __init__(self, path):
        self.path = path  # 文本路径

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        line_num = 0
        record_list: list[Record] = []
        for line in f.readlines():
            line_num += 1  # 跳过第一行
            if line_num != 1:
                line = line.strip()
                data_list = line.split("\t")
                record = Record(float(data_list[2]), float(data_list[3]), float(data_list[4]), float(data_list[8]),
                                float(data_list[9]), float(data_list[10]))
                record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    textFileReader = TextFileReader("E:/IMU资料/维特智能上位机-1666838274113/Record/BWT901BLECL5.0_1675026918200.txt")
    record_list = textFileReader.read_data()
    for l in record_list:
        print(l)
