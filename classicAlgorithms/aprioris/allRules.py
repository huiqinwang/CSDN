# -*- coding:UTF-8 -*-
import frequentCollection as fc
class allRules:
    def generate_rules(self,freqSet,L,support_data,minConf=0.7):
        big_rule_list = []

        for i in range(1,len(L)):
            for freq_set in L[i]:
                H1 = [frozenset(item) for item in freq_set]
                if i > 1:
                    # 三个及以上元素的集合
                   self.rulesFromConseq(freqSet, H1, support_data,big_rule_list, minConf)
                else:
                    # 两个元素的集合
                    self.calc_conf(freqSet, H1,support_data, big_rule_list, minConf)
        return big_rule_list



    # 对候选规则集进行评估
    def calc_conf(self,freqSet, H, supportData, brl, minConf=0.7):
        prunedH = []
        for conseq in H:
            conf = supportData[freqSet] / supportData[freqSet - conseq]
            if conf >= minConf:
                print freqSet - conseq, '-->', conseq, 'conf:', conf
                brl.append((freqSet - conseq, conseq, conf))
                prunedH.append(conseq)
        return prunedH

    # 生成候选规则集
    def rulesFromConseq(self,freqSet, H, supportData, brl, minConf=0.7):
        m = len(H[0])
        if (len(freqSet) > (m + 1)):
            Hmpl = fc.frequentCollection().apriori_Gen(H, m +1 )
            Hmpl = self.calc_conf(freqSet, Hmpl, supportData, brl, minConf)
            if (len(Hmpl) > 1):
               self. rulesFromConseq(freqSet, Hmpl, supportData, brl, minConf)