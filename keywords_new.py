#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 3.7

import collections

import jieba
import jieba.posseg as psg
import wordcloud
from matplotlib import pyplot as plt

jieba.setLogLevel(jieba.logging.INFO)
analytic_file = "./2_分析/分析.txt"
custom_words = "./1_配置/自定义词.txt"
stop_words = "./1_配置/停用词.txt"
word_class_dict = {
    "a": "形容词",
    "ad": "形容词",
    "ag": "形容词",
    "al": "形容词",
    "an": "形容词",
    "b": "区别词",
    "bl": "区别词",
    "c": "连词",
    "cc": "连词",
    "d": "副词",
    "df": "副词",
    "dg": "副词",
    "e": "叹词",
    "eng": "英文",
    "f": "方位词",
    "g": "语素",
    "h": "前缀",
    "i": "成语",
    "j": "简称略语",
    "k": "后缀",
    "l": "习用语",
    "m": "数词",
    "mg": "数词",
    "mq": "数量词",
    "n": "名词",
    "ng": "名词",
    "nl": "名词",
    "nr": "名词",
    "nr1": "名词",
    "nr2": "名词",
    "nrf": "名词",
    "nrfg": "名词",
    "nrj": "名词",
    "nrt": "名词",
    "ns": "名词",
    "nsf": "名词",
    "nt": "名词",
    "nz": "名词",
    "o": "拟声词",
    "p": "介词",
    "pba": "介词",
    "pbei": "介词",
    "q": "量词",
    "qt": "量词",
    "qv": "量词",
    "r": "代词",
    "rg": "代词",
    "rr": "代词",
    "rz": "代词",
    "rzs": "代词",
    "rzt": "代词",
    "rzv": "代词",
    "ry": "代词",
    "rys": "代词",
    "ryt": "代词",
    "ryv": "代词",
    "s": "处所词",
    "t": "时间词",
    "tg": "时间词",
    "u": "助词",
    "ud": "助词",
    "ude1": "助词",
    "ude2": "助词",
    "ude3": "助词",
    "udeng": "助词",
    "udh": "助词",
    "ug": "助词",
    "uguo": "助词",
    "uj": "助词",
    "ul": "助词",
    "ule": "助词",
    "ulian": "助词",
    "uls": "助词",
    "uv": "助词",
    "usuo": "助词",
    "uyy": "助词",
    "uz": "助词",
    "uzhe": "助词",
    "uzhi": "助词",
    "v": "动词",
    "vd": "动词",
    "vf": "动词",
    "vg": "动词",
    "vi": "动词",
    "vl": "动词",
    "vn": "动词",
    "vq": "动词",
    "vshi": "动词",
    "vx": "动词",
    "vyou": "动词",
    "w": "标点符号",
    "wb": "标点符号",
    "wd": "标点符号",
    "wf": "标点符号",
    "wj": "标点符号",
    "wh": "标点符号",
    "wkz": "标点符号",
    "wky": "标点符号",
    "wm": "标点符号",
    "wn": "标点符号",
    "wp": "标点符号",
    "ws": "标点符号",
    "wt": "标点符号",
    "ww": "标点符号",
    "wyz": "标点符号",
    "wyy": "标点符号",
    "x": "字符串",
    "xu": "字符串",
    "xx": "字符串",
    "y": "语气词",
    "z": "状态词",
    "zg": "状态词",
    "un": "未知词",
}


def get_input():
    """
    获取用户输入信息
    :return:
        top_n: 数字 关键词个数
        file_name: 字符串 保存的文件名前缀
        limit: 数字 单词长度至少要大于 n
    """
    print("按提示输入，并按回车键继续！")
    print("-----------------------------------------------")
    top_n = int(input("提取前 n 个高频词汇(输入0则提取全部) ->"))
    limit = int(input("去掉单个字吗? (去掉输入1,不去掉输入0) ->"))
    file_name = input("输出结果文件名(如: sougood) ->")
    print("-----------------------------------------------")
    print("\n正在分析，请稍等......")
    print("\n-----------------------------------------------\n")
    return (top_n, file_name, limit)


def data_clean(data):
    """
    去除字符串中的特俗字符, 标点符号, 换行符等
    :param data: 字符串
    :return: data 处理之后的字符串
    """
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        data = data.replace(ch, "")
    return data


def get_data():
    """
    读取txt类型的文本文件
    :return: 处理好的文本字符串
    """
    data_file = open(analytic_file, "r", encoding = "utf-8")
    data = data_file.read().lower()
    data_file.close()
    data_str = data_clean(data)
    return data_str


def data_cut(data_str):
    """
    进行分词处理, 支持用户自定义词典
    :param data: 字符串
    :return: keywords 单词列表
    """
    jieba.load_userdict(custom_words)
    keywords = jieba.cut(data_str, cut_all=False, HMM=True)
    return keywords


def drop_stop_keywords(keywords, limit):
    """
    过滤词: 停用词, 以及用户限制长度的词
    :param cut_words: 列表 单词列表
    :param limit: 数字 单词长度至少要大于 n
    :return: keywords_lst 单词列表
    """
    pass


# WARNING: Decompyle incomplete


def analytic_counts(after_dorp_keywords_lst, top_n):
    """
    词频统计
    :param after_dorp_keywords_lst: 列表 单词列表
    :param top_n:  数字 关键词个数(前n个高频词)
    :return:
        word_counts: Counter 用于制作词语图
        all_counts: 列表 包含(单词, 词频)元组的列表, 全部词频
        top_keywords: 列表 包含(单词, 词频)元组的列表, 前 n 个词的词频
    """
    wordcloud_counts = collections.Counter(after_dorp_keywords_lst)
    all_keywords = wordcloud_counts.most_common(len(wordcloud_counts))
    top_keywords = wordcloud_counts.most_common(top_n)
    if top_n == 0:
        return (wordcloud_counts, all_keywords)
    return (None, top_keywords)


def output_file(file_name, top_n, top_keywords):
    """
    生成词频文件
    :param file_name: 文件名
    :param top_n: 前 n 个高频词
    :param top_keywords: 列表 包含(单词, 词频)元组的列表, 前 n 个词的词频
    :return: None
    """
    if top_n == 0:
        top_n = len(top_keywords)
    file_path = "./3_结果/{}_top{}_高频词.txt".format(file_name, top_n)
    file_out = open(file_path, "w",  encoding = "utf-8")
    file_out.write("@copyright 新媒体搜索引擎: https://www.sougood.top\n")
    file_out.write("-----------------------------------------------\n")
    file_out.write("词语\t词频\t词性\n")
    count = 0
    for word, frequency in top_keywords:
        for c_en in psg.cut(word):
            if count == top_n:
                break
            c_cn = word_class_dict[c_en.flag]
            file_out.write("{}\t{}\t{}\n".format(word, frequency, c_cn))
            print("{}\t{}\t{}\n".format(word, frequency, c_cn), "", "end")
            count += 1
    print("\n-----------------------------------------------")
    file_out.close()


def make_word_cloud(keywords, top_n):
    """
    制作词云图
    :param keywords: Counter 用于制作词语图
    :param num: 前 n 个高频词
    :return: None
    """
    if top_n == 0:
        top_n = 50
    wc = wordcloud.WordCloud(font_path = "C:/Windows/Fonts/simhei.ttf", background_color = "white", max_words = top_n , max_font_size = 85)
    wc.generate_from_frequencies(keywords)
    plt.figure("词云")
    plt.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.99,wspace=0, hspace=0)
    plt.imshow(wc, cmap="gray", interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print('\nOK~ 统计已完成! 打开 "3_结果" 文件夹查看！')
    print("OK~ 词云已完成! 点击保存即可")


if __name__ == "__main__":
    (top_n, file_name, limit) = get_input()
    data_str = get_data()
    keywords = data_cut(data_str)
    after_dorp_keywords_lst = drop_stop_keywords(keywords, limit)
    (wordcloud_counts, top_keywords) = analytic_counts(after_dorp_keywords_lst, top_n)
    output_file(file_name, top_n, top_keywords)
    make_word_cloud(wordcloud_counts, top_n)
    print("\n-----------------------------------------------")
    print("@copyright 新媒体搜索引擎: https://www.sougood.top")
    input("按任意键即可退出程序 ->")