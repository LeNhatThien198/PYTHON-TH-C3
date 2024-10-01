
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

def ve_hinh_3(n2):
    for i in range(n2):
        for j in range(i + 1):
            if i == n - 1 or j == i:
                if i == n - 1:
                    print("* " * n2, end="")
                    break
                else:
                    print("*", end=" ")
            else:
                print(" ", end=" ")
           
        print()


ve_hinh_1_2(n)
print()
ve_hinh_3(n2)        
        




