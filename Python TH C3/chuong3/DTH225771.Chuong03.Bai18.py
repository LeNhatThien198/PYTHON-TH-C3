
# Online Python - IDE, Editor, Compiler, Interpreter
n=4
n2=7
def ve_hinh_1_2(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ", end=" ")

        for j in range(n - i + 1):
            print(" ", end=" ")
        for k in range(i + 1):
            print("*", end=" ")
        print()

def test(n3):
    for i in range(n3):
        if i == n3 // 2:
            print("*"*n3)
        else:
            if i < n3 // 2 and i != 0:
                print("*" + " " * (i-1) + "*")
            elif i > n3 // 2 and i != n3 - 1:
                print(" " * i + "*" + " " * (n3 - (i+2)) + "*")
            else:
                print(" " * i + "*")
test(7)
        




