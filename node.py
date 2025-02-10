import copy

def remainNumber(matrix: list):
    count = 0
    for row in matrix:
        filtered_row = [x for x in row if x != -1]  
        count += len(filtered_row) - len(set(filtered_row))
        

    
    num_cols = len(matrix[0])
    for col in range(num_cols):
        column_values = [matrix[row][col] for row in range(len(matrix)) if matrix[row][col] != -1]
        count += len(column_values) - len(set(column_values))  
            
    return count

class Node:
    def __init__(self, matrix: list, size, previous: None) -> None:
        self.size = size
        self.matrix = copy.deepcopy(matrix)
        self.previous = previous
        if (self.previous == None):
            self.step = 0
        else:
            self.step = self.previous.step + 1
        
        self.remainNum = remainNumber(matrix)
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i][j] != __o.matrix[i][j]:
                        return False
            return True
        return False
    def __bool__(self):
        if len(self.matrix) == 0:
            return False
        return True
    # def __lt__(self, __o: object):
    #     return self.remainNum < __o.remainNum

    # def __le__(self, __o: object):
    #     return self.remainNum <= __o.remainNum

    # def __gt__(self, __o: object):
    #     return self.remainNum > __o.remainNum

    # def __ge__(self, __o: object):
    #     return self.remainNum >= __o.remainNum
    
    def printMatrix(self):
        for row in self.matrix:
            print(" ".join(f"{num:3}" for num in row))