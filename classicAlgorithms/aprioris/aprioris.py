# -*- coding:UTF-8 -*-

# 首先需要找到频繁项集，然后根据频繁项集获得关联规则
class aprioris:
    # 读取dat文件数据
    def loadDataSet(self):
        parse_data = [line.split() for line in open('../data/kosarak.dat').readlines()]
        print "data_lens",len(parse_data)
        print "sample_data",parse_data[1]
        return parse_data


if __name__ == "__main__":
    apr = aprioris()
    apr.loadDataSet()