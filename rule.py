from node import Node, remainNumber
import copy
from collections import deque

def isConnected(matrix, white_cells, start):
    n = len(matrix)
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    connected_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        connected_count += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in white_cells and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return connected_count == len(white_cells)  

def checkIsolation(matrix, x, y):
    
    if matrix[x][y] == -1:
        return False  
    
    n = len(matrix)
    white_cells = {(i, j) for i in range(n) for j in range(n) if matrix[i][j] != -1 and (i, j) != (x, y)}
    
    if not white_cells:
        return False  
    
    start = next(iter(white_cells))  
    
    return not isConnected(matrix, white_cells, start)  

# tim vi tri ma o bi trung lap
def shouldShadedPositions(matrix):
    size = len(matrix)
    duplicates = []
    for i in range(size):
        seen = {}
        for j in range(size):
            num = matrix[i][j]
            if num in seen and num != -1:
                duplicates.append((i, j))
                duplicates.append(seen[num])
            else:
                seen[num] = (i, j)
    for j in range(size):
        seen = {}
        for i in range(size):
            num = matrix[i][j]
            if num in seen and num != -1:
                duplicates.append((i, j))
                duplicates.append(seen[num])
            else:
                seen[num] = (i, j)
    
    return list(set(duplicates))


def positionNeighbor (posible: list, size):
    
    ans = []
    if posible[0] + 1 < size: 
        ans.append([posible[0]+ 1, posible[1]])
    if posible[0] - 1 >= 0:
        ans.append([posible[0] -1, posible[1]])
    if posible[1] + 1 < size:
        ans.append([posible[0], posible[1] + 1])
    if posible[1] - 1 >= 0:
        ans.append([posible[0], posible[1] - 1])
    return ans
    
def checkBetweenPair (matrix: list, position: list):
    list1 = positionNeighbor(position, len(matrix))
    if [position[0]+1, position[1]] in list1 and [position[0]-1, position[1]] in list1:
        if matrix[position[0]+1][position[1]] == matrix[position[0]-1][position[1]]:
            return True
    if [position[0], position[1]+1] in list1 and [position[0], position[1]-1] in list1:
        if matrix[position[0]][position[1]+1] == matrix[position[0]][position[1]-1]:
            return True
    return False

def canShadePosition (temp: Node, position: list) -> bool:
    i = position[0]
    j = position[1]
    if temp.matrix[i][j] == -1:
        return False
    list2 = positionNeighbor(position, temp.size)
    for item in list2:
      if temp.matrix[item[0]][item[1]] == -1:
          return False
    if checkIsolation(temp.matrix, i, j):
        return False
    return True
            

    
def isGoalState(matrix: list):
    for row in matrix:
        filtered_row = [x for x in row if x != -1]  
        if len(filtered_row) != len(set(filtered_row)): 
            return False

    
    num_cols = len(matrix[0])
    for col in range(num_cols):
        column_values = [matrix[row][col] for row in range(len(matrix)) if matrix[row][col] != -1]
        if len(column_values) != len(set(column_values)):  
            return False

    return True


    

def generateNode(current: Node, carePosition: list)->list:
   ans = []
   for i in range(current.size):
      for j in range(current.size):
            if current.matrix[i][j] != -1 and (i, j) in carePosition  and canShadePosition(current, [i,j]):
               temp = Node(copy.deepcopy(current.matrix), current.size, current)
               temp.matrix[i][j] = -1
               temp.remainNum = remainNumber(temp.matrix)
               ans.append(temp)
   return ans