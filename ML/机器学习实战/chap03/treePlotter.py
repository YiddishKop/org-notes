import matplotlib.pyplot as plt

decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "round4", fc = "18")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt,
                            xy = parentPt,
                            xycoords = 'axes fraction',
                            xytext = centerPt,
                            textcoords = 'axes fraction',
                            va = 'center',
                            ha = 'center',
                            bbox = nodeType,
                            arrowprops = arrow_args)


# {‘no surfacing' ：{o: 'no', 1: {'flippers': {0: 'no’, 1: 'yes'}}}}
def getNumLeafs(myTree):
    '''
    if subtree(value of some key) is a dict, execute this function recursively to add 1 or result of function.
    广度优先便利，利用循环＋递归
    '''
    leafNum = 0
    firstKey = list(myTree.keys())[0]
    secondDict = myTree[firstKey]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            leafNum += getNumLeafs(secondDict[key])
        else: leafNum += 1
    return leafNum

def getTreeDepth(myTree):
    '''
    1. 用一个 maxDepth 变量来承载最大深度
    2. 如果 value 类型是 dict,那么深度就是 add 递归函数
       如果 value 类型不是，则增加1.
    3. 这里需要注意，跟上一个函数 getLeafNum 的区别：
       getLeafNum 是见一个leafNode 总数自增1.
       getTreeDepth 是见一层 总数自增1
    '''
    maxDepth = 0
    firstKey = list(myTree.keys())[0]
    secondDict = myTree[firstKey]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            treeDepth = 1 + getTreeDepth(secondDict[key])
        else: treeDepth = 1
        if treeDepth > maxDepth: maxDepth = treeDepth
        # if treeDepth > maxDepth 这一句必须放在 for 循环内部
        # 意思是在众多子树中找到最深的返回
    return maxDepth



def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0:'no',1:{'flippers':
                                              {0: 'no', 1:'yes'}}}},
                   {'no surfacing':{0:'no',1:{'flippers':
                                              {0:{'head': {0:'no',1:'yes'}}, 1:'no'}}}}]
    return listOfTrees[i]

def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

    # Variables:
    # -------------------------------------
    # cntrPt:       引导线的指向坐标
    # firstStr:     待画结点的字符
    # depth:        当前子树的深度
    # numLeafs:     当前子树的叶子节点数
    # secondDict:   获取已经画出的结点(key)的 value,亦即下一层节点
    # plotTree.yOff: 下一层节点所处y 坐标，比当前层节点低一层

    # Functions:
    # -------------------------------------
    # plotMidText():画出引导线上的文字,分类依据
    # plotNode()   :画出该节点
    # for 循环用于解析出 当前节点value(secondDict) 中的诸多子树，
    # 并判断这个 *value* 的 value是否 dict 类型
    #     如果是：
    #     1. 以当前node 的位置做为引导线的起始位置，递归调用本函数
    #     2. node 文字 = 这个 value 的 value;
    #        midTxt = 这个 value de key
    #     如果不是则
    #     1. 这个节点的横坐标应该是在原油 xOff 的基础上加一个 leafNode 的距离
    #     2. midTxt = 这个 value 的key;
    #        node文字 = 这个 value 的value;
    #        node 位置 = y 坐标不变（本层位置）；x 坐标参考（1）
    #        引导线起始位置 = 上层 node的位置
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key],
                     (plotTree.xOff, plotTree.yOff),
                     cntrPt,
                     leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff),
                        cntrPt,
                        str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD


def createPlot(inTree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks = [], yticks = [])
    # 声明一些属性作为全局变量供其他函数（plotTree）调用
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()
