from searching import Searching

if __name__ == "__main__":
    temp = Searching()
    choose = int(input("chose bfs: 1 or aStar: 2 --> "))
    if choose == 1:
        print("BFS solution: ")
        temp.bfs()
    elif choose == 2:
        print("A star solution: ")
        temp.Astar()
