# LADOT Python programs
#
def foo():
    print("Inside foo")
    return 0

def foobar():
    print("Inside foobar")
    return 0

x = 0
x = 1
x = 2
x = 3
x = 4

if x == 1:
    print("It is 1")
elif x == 2:
    print("It is not 1")
elif x == 3:
    foobar()
else:
    foo()

try:
    foobarbaz()
except RuntimeError:
    print("Caught runtime error")
except TypeError:
    print("Caught type error")
except NameError:
    print("Caught name error")
except OSError:
    print("Caught OS error")
except:
    print("Unhandled exception")
finally:
    print("Return -1")


def foobarbaz():
    print("Inside foobarbaz")
    return 0

foobarbaz()

import os
print(os.getcwd())

try:
    my_fh = open(".\foo.txt", "r")
    my_fh.close
except RuntimeError:
    print("Caught runtime error")
except TypeError:
    print("Caught type error")
except NameError:
    print("Caught name error")
except OSError:
    print("Caught OS error")
except:
    print("Unhandled exception")
finally:
    print("Return -1")

try:
    my_fh = open("C:\\Users\\bisuser\\Documents\\foo.txt", "r")
    my_fh.close
    print("File opened and closed")
except RuntimeError:
    print("Caught runtime error")
except TypeError:
    print("Caught type error")
except NameError:
    print("Caught name error")
except OSError:
    print("Caught OS error")
except:
    print("Unhandled exception")
finally:
    print("Return -1")

my_list = [1,2,3,4,5]
my_list.append(6)
my_append = [7,8,9,0]
my_list.extend(my_append)
for i in my_list:
    print(i)
n = my_list.pop()
print(n)

my_matrix = [['a', 'b', 'c'], my_list, ['e', 'f', 'g']]
for j in my_matrix:
    for k in j:
        print("%s" % k, end=" ")
    print()


