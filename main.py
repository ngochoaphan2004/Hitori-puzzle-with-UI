from searching import Searching

if __name__ == "__main__":
    size = int(input("size of test:"))
    test = int(input("test number:"))
    temp = Searching(size, test)
    choose = int(input("chose bfs: 1 or aStar: 2 --> "))
    if choose == 1:
        print("BFS solution: ")
        temp.bfs()
    elif choose == 2:
        print("A star solution: ")
        temp.Astar()
