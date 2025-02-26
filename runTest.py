from searching import Searching
import ast
import argparse
import sys
if __name__ == "__main__":
    
    difficul_info = [
        "5x5 Easy Hitori", "5x5 Normal Hitori", "5x5 Hard Hitori",
        "10x10 Easy Hitori", "10x10 Normal Hitori", "10x10 Hard Hitori",
        "15x15 Easy Hitori", "15x15 Normal Hitori", "15x15 Hard Hitori",
        "20x20 Easy Hitori", "20x20 Normal Hitori", "20x20 Hard Hitori"
    ]

    parser = argparse.ArgumentParser(description="Choose the difficulty level and number of test cases.")

    parser.add_argument(
        "--difficult", type=int, choices=range(len(difficul_info)),
        help="Choose difficulty:\n" + "\n".join([f"{i}: {difficul_info[i]}" for i in range(len(difficul_info))])
    )
    parser.add_argument(
        "--num_test", type=int, help="Number of test cases (positive integer)"
    )

    try:
        args = parser.parse_args()
    except SystemExit as e:
        sys.exit(e.code)

    matrix_size = 0
    if args.difficult in range(0,3):
        matrix_size = 5
    elif args.difficult in range(3,6):
        matrix_size = 10
    elif args.difficult in range(6,9):
        matrix_size = 15
    else:
        matrix_size = 20

    choose = int(input("chose bfs: 1 or aStar: 2 --> "))
        
    with open(f"result/dif_{args.difficult}_numtest_{args.num_test}_{"BFS" if choose == 1 else "Astar"}.txt", "w", encoding="utf-8") as f:
        f.truncate()
    f.close()
    try:
        file = open(f"tests/dif_{args.difficult}_numtest_{args.num_test}.txt", "r")
    except Exception as e:
        print(e)
        

    while True:
        value = file.readline()
        if not value:
            break
        test = ast.literal_eval(value)
        temp = Searching(matrix_size, test,False)
        if choose == 1:
            temp.bfs()
        elif choose == 2:
            temp.Astar()

        with open(f"result/dif_{args.difficult}_numtest_{args.num_test}_{"BFS" if choose == 1 else "Astar"}.txt", "a", encoding="utf-8") as writefile:
            writefile.write(repr(round(temp.time,6)) + "\n")



    file.close()
    writefile.close()

        
