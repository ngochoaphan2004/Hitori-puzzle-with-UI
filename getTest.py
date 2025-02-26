from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import argparse

difficul_info = [
    "5x5 Easy Hitori", "5x5 Normal Hitori", "5x5 Hard Hitori",
    # "10x10 Easy Hitori", "10x10 Normal Hitori", "10x10 Hard Hitori",
    # "15x15 Easy Hitori", "15x15 Normal Hitori", "15x15 Hard Hitori",
    # "20x20 Easy Hitori", "20x20 Normal Hitori", "20x20 Hard Hitori"
]

parser = argparse.ArgumentParser(description="Choose the difficulty level and number of test cases.")

parser.add_argument(
    "--difficult", type=int, choices=range(len(difficul_info)),
    help="Choose difficulty:\n" + "\n".join([f"{i}: {difficul_info[i]}" for i in range(len(difficul_info))])
)
parser.add_argument(
    "--num_test", type=int, help="Number of test cases (positive integer)"
)

args = parser.parse_args()

# class a():
#     difficult = 3
#     num_test = 1

# args = a()

matrix_size = 0
if args.difficult in range(0,3):
    matrix_size = 5
# elif args.difficult in range(3,6):
#     matrix_size = 10
# elif args.difficult in range(6,9):
#     matrix_size = 15
# else:
#     matrix_size = 20

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager" 
options.add_argument("--headless=new") 
options.add_argument("--disable-gpu") 
options.add_argument("--no-sandbox") 
options.add_argument("--disable-dev-shm-usage") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

with open(f"tests/dif_{args.difficult}_numtest_{args.num_test}.txt", "w", encoding="utf-8") as file:
    file.truncate(0) 
file.close()

for iteration in range(args.num_test):
    print(f"test {iteration + 1}", end=": ")

    driver.get(f"https://www.puzzle-hitori.com/?size=-{args.num_test}/")

    try:
        div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hitori-cell-back")))
        print("found")
        child_divs = div.find_elements(By.CLASS_NAME, "number")
        for i, child in enumerate(child_divs, 0):
            matrix[int(i / matrix_size)][i % matrix_size] = int(child.text)

        with open(f"tests/dif_{args.difficult}_numtest_{args.num_test}.txt", "a", encoding="utf-8") as file:
            file.write(repr(matrix) + "\n")

    except Exception as e:
        print("error:", e)

file.close
driver.quit()