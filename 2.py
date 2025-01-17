#精确查找
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("--".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("--".join(seg_list))  # 精确模式


seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print("--".join(seg_list))