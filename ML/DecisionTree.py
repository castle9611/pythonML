import math

#Step 1. Load the weather data
def Loaddata():
    '''
    make the weather dataset
    :return: weatherData(原始数据); featureName(天气特征); classValues(分类结果：是否打球)
    '''
    weatherData = [['Sunny','Hot','High','FALSE','N'],
        ['Sunny','Hot','High','TRUE','N'],
        ['Overcast','Hot','High','FALSE','P'],
        ['Rain','Mild','High','FALSE','P'],
        ['Rain','Cool','Normal','FALSE','P'],
        ['Rain','Cool','Normal','TRUE','N'],
        ['Overcast','Cool','Normal','TRUE','P'],
        ['Sunny','Mild','High','FALSE','N'],
        ['Sunny','Cool','Normal','FALSE','P'],
        ['Rain','Mild','Normal','FALSE','P'],
        ['Sunny','Mild','Normal','TRUE','P'],
        ['Overcast','Mild','High','TRUE','P'],
        ['Overcast','Hot','Normal','FALSE','P'],
        ['Rain','Mild','High','TRUE','N']]

    featureName = ['Outlook', 'Temperature', 'Humidity', 'Windy']
    classValues = ['P', 'N']

    return weatherData, featureName, classValues
    
def calcShannonEnt(paraDataSet):
    '''
    计算给定数据集的香浓熵
    :param paraDataSet: 给定数据集
    :return: shannonEnt
    '''
    numInstances = len(paraDataSet)  # numInstances:当前给定数据集中数据的个数
    labelCounts = {}
    for featureVec in paraDataSet:  # featureVec:数据集中的单个数据
        tempLabel = featureVec[-1]
        if tempLabel not in labelCounts.keys():
            labelCounts[tempLabel] = 0
        labelCounts[tempLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts.keys():
        prob = float(labelCounts[key])/numInstances
        shannonEnt -= prob * math.log2(prob)

    return shannonEnt


print(Loaddata())