# coding:utf-8
import re


def convert_number(cn_num):
    chinese_number = u'一二三四五六七八九十'
    num_dct = dict(zip(chinese_number, xrange(1, 11)))
    dct = {
        u'一觉': 28000,
        u'二觉': 35000,
        u'两觉': 35000,
        u'三觉': 42000,
        u'满觉': 49000
    }

    if cn_num in dct:
        return dct[cn_num]

    try:
        num = float(cn_num)  # 数字直接返回
    except Exception, e:
        lst = list(cn_num)
        if len(lst) == 1:  # 个位数
            num = num_dct[cn_num]
        else:
            num_str = reduce(lambda x, y: str(num_dct[x])+str(num_dct[y]), lst)  # 十三：103  二十三：2103
            num = float(num_str[0]+num_str[-1])  # 截取第一位和最后一位
    return num*10000 if num <= 100 else num


def func(ss):
    ss = re.sub('\s', '', ss)
    re_lst = re.findall(u'(\d+\.\d+|\d+|[一二三四五六七八九十]+)[wW万\＋\+]?多?魂', ss) \
             + re.findall(u'[一二两三满]觉', ss) + re.findall(u'魂(\d+\.\d+|\d+|[一二三四五六七八九十]+)[wW万]多?', ss) # 匹配魂数量
    num_lst = [convert_number(i) for i in re_lst]
    if num_lst:
        return max(num_lst)
    else:
        return False


if __name__ == '__main__':
    ss = u'8橙吕布，十八魂 ¥59.0 18 4个多月心血号弃坑'
    ss = u'18级吴国队，两万3魂18级县长无敌，积分不高可掉回县长'
    ss = u'【26级】63000＋魂刺史'
    print func(ss)

