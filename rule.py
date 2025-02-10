from node import Node, remainNumber
import copy
from collections import deque

def isConnected(matrix, white_cells, start):
    """
    Kiểm tra xem các ô trắng có còn kết nối sau khi tô đen một ô không.
    """
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
    
    return connected_count == len(white_cells)  # Tất cả ô trắng phải được kết nối

def checkIsolation(matrix, x, y):
    """
    Kiểm tra xem nếu tô đen ô (x, y) có làm cô lập các ô trắng không.
    """
    if matrix[x][y] == -1:
        return False  # Chỉ có thể tô đen ô trắng
    
    n = len(matrix)
    white_cells = {(i, j) for i in range(n) for j in range(n) if matrix[i][j] != -1 and (i, j) != (x, y)}
    
    if not white_cells:
        return False  # Nếu không còn ô trắng nào, lưới không hợp lệ
    
    start = next(iter(white_cells))  # Chọn một ô trắng để bắt đầu kiểm tra
    
    return not isConnected(matrix, white_cells, start)  # Nếu mất kết nối, trả về True (vi phạm)

def shouldShadedPositions(matrix):
    """
    Tìm các vị trí có chữ số trùng trên cùng một hàng hoặc một cột.
    :param matrix: Mảng 2 chiều.
    :return: Danh sách các vị trí có chữ số trùng.
    """
    size = len(matrix)
    duplicates = []
    
    # Kiểm tra trùng trong hàng
    for i in range(size):
        seen = {}
        for j in range(size):
            num = matrix[i][j]
            if num in seen and num != -1:
                duplicates.append((i, j))
                duplicates.append(seen[num])
            else:
                seen[num] = (i, j)
    
    # Kiểm tra trùng trong cột
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
    #Return neighbor.
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
    #Check if shade in 'position' will create an enclosed shaded square.
    i = position[0]
    j = position[1]
    if temp.matrix[i][j] == -1:
        return False
    # #shouldShaded
    # if (i, j) not in shouldShadedPositions(temp.matrix):
    #     return False
    #Check neighbor
    list2 = positionNeighbor(position, temp.size)
    for item in list2:
      if temp.matrix[item[0]][item[1]] == -1:
          return False
    # #Check between pair
    # if checkBetweenPair(temp.matrix, position):
    #     return False
    #Check Enclosed
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