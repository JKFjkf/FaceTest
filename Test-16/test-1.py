#统计一个文本中单词频次最高的10个单词？
import re
#方法一

def test(filepath):

    distone = {}
    with open(filepath) as f :
        for line in f :
            line = re.sub("\w+"," ",line)#匹配任何非unicode的单词字符
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone] = 1
                else:
                    distone[keyone] += 1
    num_ten = sorted(distone.items(),key=lambda x:x[1],reverse=True)[:10]
    num_ten = [x[0] for x in num_ten]
    return num_ten