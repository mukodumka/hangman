import random

def hangman(word):
    wrong = 0
    stages = ["",
              "__________________",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              "|       / \       ",
              "|                 "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("добро пожаловать на казнь!")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("буква: ")
        if guess in rletters:
            exchange = rletters.index(guess)
            board[exchange] = guess
            rletters[exchange] = "♥"
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0:wrong + 1]))
        if "_" not in board:
            print("победа за тобой ♥")
            print("загаданное слово:", "".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("проигрыш. загаданное слово: {}".format(word))

hangman(random.choice(["doll", "love", "death", "end"]))
