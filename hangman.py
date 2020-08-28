def hangman(word):
    wrong = 0
    stages = ["",
             "__________         ",
             "|                  ",
             "|         |        ",
             "|         0        ",
             "|        /|\       ",
             "|        / \       ",
             "|                  "
             ]
    reletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcom to Hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter (Hint: a state of America)"
        char = input(msg)
        if char in reletters:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = '$'
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("You Lost! The Answer is {}.".format(word))



hangman("washington")
              
