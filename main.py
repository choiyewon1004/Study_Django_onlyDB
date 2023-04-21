# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

check_count =1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test1():
    global check_count
    if check_count ==0 :
        return

    print("test1 : ",check_count)
    pass

def test2():
    global check_count
    if check_count ==0 :
        return

    print("test2 : ", check_count)
    check_count = 0
    print("test2 : ", check_count)
    pass

def testall():
    for i in range(0,2):
        print(i, ") main : ", check_count)
        test1()
        test2()
        print(i, ") main : ", check_count)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   testall()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
