# -*- coding:UTF-8 -*-

#获得频繁项集
class frequentCollection:

    # 构建初始候选集列表
    def createC1(self,dataSet):
        C1 = []
        for transaction in dataSet:
            for item in transaction:
                if [item] not in C1:
                    C1.append([item])
        C1.sort()
        return map(frozenset,C1)

    # 计算Ck的项集在数据集合D中的支持度
    # 保留符合最小支持度项集
    def scanSupport(self,dataSet,Ck,minSupport):
        supports_can = {}
        for transaction in dataSet:
            for ci in Ck:
                if ci.issubset(transaction):
                    supports_can[ci] = supports_can.get(ci,0)+1

        num_items = float(len(dataSet))
        ret_list = []
        support_data = []
        for key in supports_can:
            supports = supports_can[key]/num_items
            if supports >= minSupport:
                ret_list.insert(0,key)

            support_data[key] = supports

        return ret_list,support_data

    # 由初始候选集集合Lk生成新的生成候选集
    # k表示生成的新项集所包含的元素个数
    # 频繁项集列表Lk和项集个数k生成候选项集Ck+1
    def apriori_Gen(self,Lk,k):
        ret_list = []
        len_lk = len(Lk)
        for i in range(len_lk):
            for j in range(i+1,len_lk):
                L1 = list(Lk[i])[:k-2] # 取列表的前k-1个元素
                L2 = list(Lk[j])[:k-2]
                L1.sort()
                L2.sort()
                if L1==L2:
                    ret_list.append(Lk[i]|Lk[j])
        return ret_list

    def apriori(self,dataSet,minSupport=0.5):
        C1 = self.createC1(dataSet)
        D = map(set,dataSet)
        L1,support_data = self.scanSupport(D,C1,minSupport)
        L = [L1]
        k = 2

        while (len(L[k-2]) > 0):
            Ck = self.apriori_Gen(L[k-2],k)
            Lk,supK = self.scanSupport(D,Ck,minSupport)
            support_data.update(supK)
            L.append(Lk)
            k += 1

        return L,support_data










