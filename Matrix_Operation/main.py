# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import getMatrix as M
import Addition as add
import Subtraction as sub
import Multiplication as mult
import Transpose as TT


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A=M.getMatrix()
    print(A)
    # B=M.getMatrix()
    # add.Addition(A,B)
    print(TT.Transpose(A))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
