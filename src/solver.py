import setup.initialise as init
import sudoku.rules as rules

#
def main():
    board = init.parse_board(hard[0])
    provided = init.provided_points(board)
    rules.run_event_loop(board, provided)
    print()
    print(init.visualise_board(board))
    solved = init.validate_board(board)
    print(init.get_message(solved))



easy = []
medium = []
hard = []
expert = []

# sample.append("")
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " ---------------------\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " ---------------------\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " . . . | . . . | . . .\n"
# sample[0] += " . . . | . . . | . . ."

# hard
hard.append("")
hard[0] += " 6 4 . | . . 1 | 7 . 2\n"
hard[0] += " 8 . 7 | . . 9 | . 1 .\n"
hard[0] += " . . 1 | . 7 . | . . 9\n"
hard[0] += " ---------------------\n"
hard[0] += " . . 6 | . 5 7 | . . .\n"
hard[0] += " 2 . . | . . . | . . .\n"
hard[0] += " . 5 . | 2 8 . | . . .\n"
hard[0] += " ---------------------\n"
hard[0] += " . 6 . | 4 . 5 | . . 3\n"
hard[0] += " . 8 . | . 6 . | . . 4\n"
hard[0] += " . . . | . . . | 1 . 5"


# easy
easy.append("")
easy[0] += " 3 5 . | 6 . 2 | . . 4\n"
easy[0] += " . . 7 | . 4 . | . 1 3\n"
easy[0] += " . 6 9 | 8 3 1 | . . 7\n"
easy[0] += " ---------------------\n"
easy[0] += " 5 . 3 | . . . | . 9 6\n"
easy[0] += " . . . | 3 . . | 7 4 5\n"
easy[0] += " 9 4 6 | . . . | 8 . .\n"
easy[0] += " ---------------------\n"
easy[0] += " 6 9 2 | 4 . . | . . 8\n"
easy[0] += " 8 . . | 7 . 3 | . . .\n"
easy[0] += " . . 4 | . 2 . | . . 1"


medium.append("")
medium[0] += " . . . | . . 2 | 6 7 .\n"
medium[0] += " 8 6 3 | . . . | . . 5\n"
medium[0] += " . . 7 | 5 . 8 | . . .\n"
medium[0] += " ---------------------\n"
medium[0] += " . . . | . 8 . | 4 9 7\n"
medium[0] += " . 7 . | . . . | . 8 .\n"
medium[0] += " . 5 . | . 3 . | 1 . 6\n"
medium[0] += " ---------------------\n"
medium[0] += " . . 1 | 9 . 6 | . . .\n"
medium[0] += " 4 3 . | . 5 . | . 6 .\n"
medium[0] += " . 2 . | . 7 . | . 1 ."


# expert
expert.append("")
expert[0] += " . . 9 | . 3 4 | . 6 .\n"
expert[0] += " . . . | . 8 . | . . .\n"
expert[0] += " 7 . . | . 1 . | . . .\n"
expert[0] += " ---------------------\n"
expert[0] += " . . 3 | . . . | . . .\n"
expert[0] += " . 2 . | 5 . . | 9 1 .\n"
expert[0] += " 9 . . | . . . | . . 7\n"
expert[0] += " ---------------------\n"
expert[0] += " . . 6 | . . 3 | 8 . 1\n"
expert[0] += " 3 . . | . . . | . 2 .\n"
expert[0] += " . . . | 9 . . | . 4 ."

if __name__ == "__main__":
    main()
