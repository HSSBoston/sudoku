## Python Sudoku Solver

#### Overview:

My final project is a sudoku solver. This sudoku solver takes in a sudoku problem and solves it within seconds.

Sudoku is a number puzzle that has a 9x9 cell grid. The grid is grouped into rows, columns, and blocks. A block consists of 3x3 cells, so there are 9 blocks in each problem (9x9 cell grid). In each section (row, column, and block) there are 9 cells. The rule is to fit the numbers 1 through 9 in each of those 9 cells of each section without repeating any numbers. Given a problem, which has some cells filled in and others left empty, the objective is to fill the empty cells by following this rule. The solution should have the numbers 1 through 9 once each in every row, column, and block.

#### Implementation:

The sudoku solver is written in the file project.py. Problems are stored as individual lines in a text file called problem.txt. Each problem is expressed as a single line in the file. Here is an example:

.8.....1. 1..2..9.. ..7..4..3 3...1..9. ...7.2... .6..8...4 9..4..1.. ..4..3..5 .2.....8.

An empty cell is notated by a dot (.). A space is used as a separator for rows.

The sudoku solver, project.py, first runs main(), which reads the problems from problem.txt one line/problem at a time. The check() function checks if a given problem is valid with regex. For example, it checks if a problem has 81 characters and 8 spaces and if the problem does not have invalid characters. It then puts the problem into a list. This list is used as an input for the solve() function.

The solve() function first uses empty(), which identifies empty cells. It then loops through each empty cell and finds the numbers that can be filled in the empty cell. These numbers are called “usable numbers”. They are found with the usableNums() function.

The usableNums() function finds usable numbers for an empty cell by identifying the numbers that have been placed in the row, column and block that the empty cell belongs to. It uses the functions row(), column(), and block() to do this and returns the usable numbers as a list.

The solve() function fills a usable number into a given empty cell and calls solve() recursively to work on the next empty cell. If no usable numbers are found for the next empty cell, that means the number placed in the first empty cell was wrong. Therefore, solve() backtracks and fills another usable number into the first empty cell and sees if the next empty cell has usable numbers. This way, solve() fills usable numbers into empty cells one by one as far as the next empty cell has at least one usable number. When no usable numbers are found for an empty cell, solve() backtracks to the previous empty cell and fills an alternative usable number into it. If no more alternatives are available, solve() backtracks again. When all empty cells are filled with their usable numbers, solve() has found the solution. It returns the solutions as a list.

The checkAnswer() function verifies the solution by checking if each row, column and block has a unique set of {1, 2, …, 8, 9}. If it is correct, the print9x9() function prints it in the 9x9 format for the user to look at. The time for solve() to find the solution is also printed using the time module.

This sudoku solver has been tested with the daily (easy, medium and hard) sudoku problems on the New York Times (https://www.nytimes.com/puzzles/sudoku). It can solve the three types of problems in ~0.1 second, about 0.1 second, and about 1 second, respectively.

This project implements a design choice to solve the problem efficiently. The solve() function finds usable numbers for each empty cell and tries out each of the numbers, instead of trying out all numbers from 1 to 9. This contributes to reducing the time to solve the problem.

#### Future Work:

This solver can still be improved. One possible improvement is to speed up the solver further by targeting the empty cells with fewer usable number choices earlier, rather than targeting empty cells at random. Another is to write a function that gives a hint to the user when solving the problem themselves. This can be done by telling the user the cell with the least number of usable number choices. Additionally, it would be nice to implement this solver as a web app, so the user can enter a problem and see the solution and hints for it.


