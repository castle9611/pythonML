import jieba

s = '大家好，欢迎大家阅读周二机器学习专题，今天的这篇文章依然会讲SVM模型。'
a = jieba.cut(s)
s[1]
s[2:10]
s[11:13]
print(list(a))

