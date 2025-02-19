from node import Node
import rule
from data import data
import time
import copy

class Searching:
    def __init__(self,size,test) -> None:
        self.size = size
        self.inputTESTCASE = data["size" + str(self.size)]["testcase" +str(test)]
        self.initNode = Node(self.inputTESTCASE["matrix"], self.size, None)
        #PreCheck the matrix
        self.carePosition = rule.shouldShadedPositions(self.initNode.matrix)
        self.checkedNode = self.initNode
        
        self.path = []
        self.result = 0
        self.time = 0
        self.numberNode = 0
        
    def preCheckNode(self):
        ignore = []
        #find triplet
        current = self.initNode
        for i in range(self.size):
            for j in range(self.size):
                if rule.checkBetweenPair(current.matrix, [i, j]):
                    if i+1 < self.size:
                        if current.matrix[i][j] == current.matrix[i+1][j]:
                            temp = Node(copy.deepcopy(current.matrix), current.size, current)
                            temp.matrix[i+1][j] = -1
                            temp.matrix[i-1][j] = -1
                            ignore.extend([(i+1, j), (i, j), (i-1, j)])
                            current = temp
                    elif j+1 < self.size: 
                        if current.matrix[i][j] == current.matrix[i][j+1]:
                            temp = Node(copy.deepcopy(current.matrix), current.size, current)
                            temp.matrix[i][j+1] = -1
                            temp.matrix[i][j-1] = -1
                            current = temp
                            ignore.extend([(i, j+1), (i, j), (i, j-1)])
                    else:
                        ignore.append((i, j))
                    
        self.checkedNode = current
        
        self.carePosition = [x for x in self.carePosition if x not in ignore]
    def getPath(self, endNode: Node) -> list:
        ans = []
        temp = endNode
        while temp != None:
            ans.insert(0, temp)
            temp = temp.previous
        return ans
    
    def bfs(self):
        startTime = time.time()
        self.preCheckNode()
        queue = [self.checkedNode]
        visited = []
        while len(queue) != 0:
            currentNode = queue.pop(0)
            visited.append(currentNode)
            if currentNode.remainNum == 0:
                self.path = self.getPath(currentNode)
                executeTime = time.time() - startTime
                print("Time for searching: ", str(round(executeTime, 4)))
                print("Total node generated: ", len(visited) + len(queue))
                print("Solution: ")
                currentNode.printMatrix()

                self.result = currentNode
                self.time = executeTime
                self.numberNode = len(visited) + len(queue)
                return
            
            generateNodeList = rule.generateNode(currentNode, self.carePosition)
            for item in generateNodeList:
                if item not in visited and item not in queue:
                    queue.append(item)
    
    
    def Astar(self):
        startTime = time.time()
        self.preCheckNode()
        openList = []
        closeList = []
        openList.append([self.checkedNode.remainNum, self.checkedNode])
        while(len(openList) != 0):
            currentNode = openList.pop(0)
            closeList.append(currentNode[1])
            if currentNode[1].remainNum == 0:
                self.path =  self.getPath(closeList[len(closeList) - 1])

                executeTime = time.time() - startTime
                print("Time for searching: ", str(round(executeTime, 4)))
                print("Total nodes generated: ", len(openList) + len(closeList))
                print("Solution: ")
                currentNode[1].printMatrix()


                self.result = currentNode[1]
                self.time = executeTime
                self.numberNode = len(openList) + len(closeList)
                return
            generateNodeList = rule.generateNode(currentNode[1], self.carePosition)
            for item in generateNodeList:
                if item not in closeList and item not in (subitem for subitem in openList):
                    openList.append([item.remainNum, item])
            openList.sort(key=lambda x: int(x[0]))

        self.path = self.getPath(closeList[len(closeList) - 1])    
    
   