import sys
import math

command = input()
var_history = {}
operator = ["+", "-", "*", "/"]

def findOperator(str):
    for item in operator:
        if item in str:
            return True
    return False

def calcXY(command, index):
    var1 = command[5:index].strip()
    var2 = command[index+1:].strip()
    if findOperator(var1) or findOperator(var2):
        raise(IOError)
    if var1.isdigit():
        x = int(var1)
    else:
        x = var_history[var1]
    if var2.isdigit():
        y = int(var2)
    else:
        y = var_history[var2]
    return x, y

while 1:
    if command.lower() == "quit":
        sys.exit()

    elif command[:3] == "def":
        try: 
            index = command.index("=")
            var = command[4:index].strip()
            num = int(command[index+1:].strip())
            if var.isdigit():
                raise(IOError)
            if findOperator(var):
                raise(IOError)
            var_history[var] = num
        except: print("Invalid command")

    elif command[:4] == "calc":
        try:
            if "+" in command:
                index = command.index("+")
                x, y = calcXY(command, index)
                print(x + y)
            elif "-" in command:
                index = command.index("-")
                x, y = calcXY(command, index)
                print(x - y)
            elif "*" in command:
                index = command.index("*")
                x, y = calcXY(command, index)
                print(x * y)
            elif "/" in command:
                index = command.index("/")
                x, y = calcXY(command, index)
                z = math.ceil((x / y) * 100) / 100
                if int(z) == z :
                    print(int(z))
                else: 
                    print(z)
            else:
                raise("IOError")
           
        except ZeroDivisionError:
            print("Zero division error")
        except KeyError:
            print("Undefined variable")
        except:
            print("Invalid command")

    elif command[:3] == "see":
        print("==========")
        for key, value in var_history.items():
            print("%s: %d" %(key, value))
        print("==========")

    else:
        print("undefined")

    command = input()
