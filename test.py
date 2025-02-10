from collections import deque
def is_connected(matrix, white_cells, start):
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

def check_isolation(grid, x, y):
    """
    Kiểm tra xem nếu tô đen ô (x, y) có làm cô lập các ô trắng không.
    """
    if grid[x][y][1] != 0:
        return False  # Chỉ có thể tô đen ô trắng
    
    n = len(grid)
    white_cells = {(i, j) for i in range(n) for j in range(n) if grid[i][j][1] == 0 and (i, j) != (x, y)}
    
    if not white_cells:
        return False  # Nếu không còn ô trắng nào, lưới không hợp lệ
    
    start = next(iter(white_cells))  # Chọn một ô trắng để bắt đầu kiểm tra
    
    return not is_connected(grid, white_cells, start)  # Nếu mất kết nối, trả về True (vi phạm)
def isGoalState(matrix: list):
    for row in matrix:
        filtered_row = [tup[0] for tup in row if tup[1] == 0]  
        if len(filtered_row) != len(set(filtered_row)): 
            return False

    
    num_cols = len(matrix[0])
    for col in range(num_cols):
        column_values = [matrix[row][col][0] for row in range(len(matrix)) if matrix[row][col][1] == 0]
        if len(column_values) != len(set(column_values)):  
            return False

    return True
def find_duplicate_positions(array):
    """
    Tìm các vị trí có chữ số trùng trên cùng một hàng hoặc một cột.
    :param array: Mảng 2 chiều.
    :return: Danh sách các vị trí có chữ số trùng.
    """
    size = len(array)
    duplicates = []
    
    # Kiểm tra trùng trong hàng
    for i in range(size):
        seen = {}
        for j in range(size):
            num = array[i][j][0]
            if num in seen:
                duplicates.append((i, j))
                duplicates.append(seen[num])
            else:
                seen[num] = (i, j)
    
    # Kiểm tra trùng trong cột
    for j in range(size):
        seen = {}
        for i in range(size):
            num = array[i][j][0]
            if num in seen:
                duplicates.append((i, j))
                duplicates.append(seen[num])
            else:
                seen[num] = (i, j)
    
    return list(set(duplicates))
matrix = [
                [[5, 0], [2, 0], [3, 0], [2,0], [1,0]],
                [[1, 0], [5, 0], [1, 0], [3,0], [4,0]],
                [[4, 0], [3, 0], [3, 0], [1,0], [4,0]],
                [[3, 0], [2, 0], [4, 0], [5,0], [2,0]],
                [[5, 0], [4, 0], [5, 0], [4,0], [3,0]],
            ]
# if isGoalState(matrix):
#     print("OK")
# else: 
#     print("Not OK")
def remainNumber(matrix: list):
    count = 0
    for row in matrix:
        filtered_row = [x for x in row if x != -1]  
        count += len(filtered_row) - len(set(filtered_row))
        print(count, " ", len(filtered_row), " ", set(filtered_row), "\n")
        

    
    num_cols = len(matrix[0])
    for col in range(num_cols):
        column_values = [matrix[row][col] for row in range(len(matrix)) if matrix[row][col] != -1]
        count += len(column_values) - len(set(column_values))
        print(count, " ", len(column_values), " ", set(column_values), "\n")
            
    return count

matrix1 = [
    [-1,  5,  4, -1,  2],
    [ 3,  4, -1,  5,  1],
    [-1,  2,  5,  1, -1],
    [ 2,  3,  1,  4,  5],
    [-1,  1, -1,  2, -1]
]


print(remainNumber(matrix1))

