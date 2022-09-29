
import connect4


def main():
    ifwin = True
    while ifwin:
        moves = 0
        moves2 = 0
        try:

            inp = (input('Enter The size of the game seperated by a comma.\n >>> '))
            if (inp.lower() == 'quit'):
                print("thank you for playing Mohsen's connect4 game. UwU")
                break
            newinp = list(map(int, inp.split(',')))
            nRows = int(newinp[0])
            nCols = int(newinp[1])
            totalmoves = nRows*nCols
            print(totalmoves)
            grid = connect4.makeGrid(nRows,nCols)
            grid2 = connect4.toString(grid)
            print(grid2)
        except ValueError:
            print("NOT A VALID INPUT... ")
            continue
        except TypeError:
            print("NOT A VALID INPUT... ")
            continue
        except IndexError:
            print("NOT A VALID INPUT... ")
            continue
        while True:
            try:
                choice1 = input('WHERE DOES RED WANT TO PLAY ')
                connect4.play(grid,choice1,'red')
                print(connect4.toString(grid))
                moves += 1
                win = connect4.win(grid , int(choice1))
                if win == 'red':
                    print(f'Red wins after {moves} moves , goodbye ')
                    ifwin = False
                    break
                choice2 = input('WHERE DOES BLACK WANT TO PLAY ')
                connect4.play(grid,choice2,'black')
                print(connect4.toString(grid))
                moves2 += 1
                win = connect4.win(grid , int(choice2))
                if win == 'black':
                    print(f'black wins after {moves2} moves , goodbye ')
                    ifwin = False
                    break
                if (moves+moves2) == totalmoves:
                    print("The game is a tie")
                    return False
            except ValueError:
                print("NOT A VALID INPUT... ")
            except TypeError:
                print("NOT A VALID INPUT... ")
            except IndexError:
                print("NOT A VALID INPUT... ")



if __name__ == "__main__":
    main()
