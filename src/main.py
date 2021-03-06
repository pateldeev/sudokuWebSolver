import solver
import webConnector

import time

print("Connecting to livesudoku website")

browser = webConnector.create_browser()  # open website

print("Connected! Now getting puzzle")

puzzle = webConnector.get_puzzle(browser)  # get puzzle

print("Got Puzzle!")
print("Now solving the puzzle:", puzzle)

# log file for debug
log_file_name = "solver_log.txt"
print("Running my solver. See log file for details on solution:", log_file_name)
log_file = open(log_file_name, 'w')
log_file.write('finding solution for: ' + str(puzzle) + '\n')

# solve puzzle and time
start_time = time.time()
is_solved = solver.solve(puzzle, log_file)
end_time = time.time()

log_file.close()

print("Elapsed time for my solver: %g seconds" % (end_time - start_time))

if is_solved:
    print("Puzzle solved:", puzzle)

    print("Now uploading solution")
    webConnector.post_solution(browser, puzzle)

    print("Solution uploaded!")

    print("Solution submitted!")

else:
    print("Puzzle could not be solved. Does not have a solution")

time.sleep(10)
print("Now closing browser!")
webConnector.close_browser(browser)