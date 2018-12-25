# Sudoku solver & web interface
This is a small project that I undertook to become learn & experiment with python. It uses selinium to pull soduku puzzles from the internet. Then, it solves them using a small backtracking algorithm I wrote. Finally, it posts to solution back online.

## Build notes
* Requires python3
* Requires selenium[https://selenium-python.readthedocs.io/]
  * pip3 install selenium
* Must have firefox & geckodriver[https://github.com/mozilla/geckodriver/releases] in $PATH folder for selenium to work

## Running
```bash
cd src
python3 main.py
```
