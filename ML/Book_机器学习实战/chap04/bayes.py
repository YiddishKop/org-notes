from numpy import *

# 模拟从文章中剪切出来的文章词汇表
# 用于训练贝叶斯分类器
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems',
                    'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to',
                    'dog','park','stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute',
                    'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless',
                    'gargabe'],
                   ['mr', 'licks', 'ate', 'my','steak', 'how'
                    'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless','dog','food',
                    'stupid']]
    classVec = [0,1,0,1,0,1] # 模拟文章标签是否【侮辱性的】：是为1,不是为0
    return postingList, classVec

# 构造单词表
# 通过所有文章的词汇表取并集获得单词表
# <set1>|<set2> 表示两个集合取并操作
# list of list -> list
# dataSet -> vocabList
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# 对比文章单词表和词汇表，有1无0,获得代表文章的向量
# list, set -> list or vector
# vocabList, inputSet -> returnVec
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in inputSet:
            if word in vocabList:
                returnVec[vocabList.index(word)] = 1
            else: print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

# 每篇文章经过上面的函数都转换为一个 vector: 单词向量
# list of list, list -> list, list, float
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    # p0Num = zeros(numWords); p1Num = zeros(numWords)
    # use ones to avoid probability value = 0
    p0Num = ones(numWords); p1Num = ones(numWords)
    # p0Denom = 0.0; p1Denom = 0.0
    # same reason as below
    p0Denom = 2.0; p1Denom = 2.0
    for i in range (numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive


# use probabilities get from trainNB0() to classify a new article
# list, list, list, float -> int
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

# use 'love my dalmation' and 'stupid garbage' to test whether classifier is good
# [null] -> [print]
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love','my','dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ',classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ',classifyNB(thisDoc, p0V, p1V, pAb))

# calculate the number of word occur in articles, instead of use '1' to represent
# list, list -> list
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

# use regex as symbol to split articles
# string -> list
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

# use probabilities get from trainNB0() to classify email and calculate error rate
# [null] -> [print]
def spamTest():
    docList = []; classList = []; fullText = []
    # 从邮件中构建出 docList, classList, fullText
    # docList : list of list, every inner-list represent an email
    # classList : list, every item is the class-lable of docList with same sequence
    # fullText : list, list of all the words occur in all emails
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    # build vocabList from docList
    vocabList = createVocabList(docList)
    # build trainingSet, which is just indexes from 0~49
    trainingSet = list(range(50)); testSet = []
    # build testSet from trainingSet
    for i in range(10):
        # produce a random number by uniform distribution
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []; trainClasses = []
    # build trainMat from trainingSet
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    # get the the 3 probabilities to compute p(C1|w) by bayes
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    # compute the error rate
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print('error email is: ', docIndex)
    print('the error rate is: ', float(errorCount)/len(testSet))

# get most 30 frequent word from 'fullText' according to 'vocabList'
# list, list -> list of tuple
def calcMostFreq(vocabList, fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    # sorted() return a list of 2-elements tuple, to this example
    # return something like this: [('key1', value1),('key2', value2),('key3', value3),...,('keyn', valuen)]
    sortedFreq = sorted(freqDict.items(), key = operator.itemgetter(1), reverse = True)
    return sortedFreq[:30]


# get context from rss feed
def localWords(feed1, feed0):
    import feedparser
    docList=[]; classList=[]; fullText=[]
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30words = calcMostFreq(vocabList, fullText)
    for pairW in top30words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    # range don't return list in python3.x, so just convert by list(range())
    trainingSet = list(range(2*minLen)); testSet=[]
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]; trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print('the error rate is: ', float(errorCount)/len(testSet))
    return vocabList, p0V, p1V

# 获得与某个分类标签C1 关联度大于某个阈值的词汇列表
# dict1, dict2 -> [print]
# [注]: p0V 是 [p(c0|w0), p(c0|w1), p(c0|w2),...] 这样的list
# p(c0|article) = p(c0|w0,w1,w2,...) =naiveBayes==> p(c0|w0)*p(c0|w1)*p(c0|w2)*...
# = p(w0|c0)*p(c0)/p(w0) * p(w1|c0)p(c0)/p(w1) * p(w2|c0)p(c0)/p(w2) * ...
# = w0 在 c0 标签文章中所有单词总数的比例 * c0标签在所有文章所有单词总数的比例 / w0出现的几率
def getTopWords(ny, sf):
    import operator
    vocabList, p0V, p1V = localWords(ny, sf)
    topNY = []; topSF = []
    # 统计出关联度 > -5.0 的所有单词，按照格式
    # (word, relationality) 存储在 topSF 和 topNY 两个数组中
    # topSF 和 topNY 都是这样子的： [('love', -2.0),('favor', -4.5),('business', -5.4),...]
    for i in range(len(p0V)):
        if p0V[i] > -5.0 : topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -5.0 : topNY.append((vocabList[i], p1V[i]))
    # 按照topSF 每个元素（topSF中的元素是tuple）的第二个item（pair[1]）排序
    sortedSF = sorted(topSF, key = lambda pair: pair[1], reverse = True)
    print("SF**SF**SF**SF**SF**SF**SF**SF**")
    for item in sortedSF:
        print(item[0])
    sortedNY = sorted(topNY, key = lambda pair: pair[1], reverse = True)
    print("NY**NY**NY**NY**NY**NY**NY**NY**")
    for item in sortedNY:
        print(item[0])
