from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import random
from time import sleep


# open selenium web driver and go to specified url
# returns webdriver handle
def create_browser(url='https://www.livesudoku.com/en/sudoku/easy'):
    browser = webdriver.Firefox()
    browser.get(url)
    return browser


# gets soduku puzzle. browser must be on livesudoku site with correct format
# returns puzzle as 2D array - 0 represents unknown
def get_puzzle(browser):
    puzzle = [[0] * 9 for i in range(0, 9)]  # empty puzzle

    id_base = 'td'
    for i in range(0, 81):
        temp_val = browser.find_element_by_id(id_base + str(i)).get_attribute("innerText")
        if temp_val.isdigit():
            puzzle[int(i / 9)][i % 9] = int(temp_val)  # save an given values

    return puzzle


# posts soduku puzzle solution. browser must be on livesudoku site with correct format
def post_solution(browser, solution):
    id_base = 'td'
    for i in range(0, 81):
        temp_cell = browser.find_element_by_id(id_base + str(i))
        if not temp_cell.get_attribute("innerText").isdigit():
            temp_cell.click()  # click on any unfilled cell
            ActionChains(browser).send_keys(str(solution[int(i / 9)][i % 9])).perform()  # post solution


# closes selenium web driver
def close_browser(browser):
    browser.close()
