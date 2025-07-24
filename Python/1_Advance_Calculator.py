History_File = "history.txt"

def show_history():
    file = open(History_File, "r")
    lines = file.readlines()

    if len(lines) == 0:
        print("NO HIstory is Found")
    else:
        for line in reversed(lines):
            print(line.strip())

    file.close()

def clear_history():
    file = open(History_File, 'w')
    file.close()
    print("History is Cleared")


def save_history(equation, result):
    file = open(History_File,'a')
    file.write(str(equation) + " = " + str(result) + '\n')
    file.close()


def user():
    user_input = []
    while True:
        
        while True:
            num = input("enter your number: ")
            try:
                float(num)
                user_input.append(num)
                break
            except ValueError:
                print("Invalid Number")

        while True:    
            operator = input("enter your Operator or '=' to finish: ")
            op =  ('+', '-', '/', '*')
            if operator == "=":
                if len(user_input) <3:
                    print("❌ You must enter at least one operator and another number before '='.")
                    continue
                else:
                    print("✅Your Result is: ")
                    break 

            elif operator in op:
                user_input.append(operator)
                break
            else:
                print("Invalid Operator / use ('+', '-', '/', '*')")

        if operator == "=":
            break
    return user_input

def calulation(a):    
    data = a.copy()
    result = float(data[0])

    while len(data) > 1:
        operator = data[1]
        next_num = float(data[2])

        if operator == '+':
            result += next_num
        elif operator == '-':
            result -= next_num
        elif operator == '*':
            result *= next_num
        elif operator == "/":
            if next_num == 0:
                print("Can't divide by 0")
                return
            result /= next_num

        # updating the data value
        data = [result] + data[3:]

        if int(result) == result:
            result = int(result)
        
    save_history(a,result)

    return result


def main():
    print("----SIMPLE CALCULATOR----")

    while True:
        user_input = user()
        print(calulation(user_input))
        
        while True:
            user_choice = input("PRESS 'Q' TO QUIT, 'H' TO ACCESS HISTORY, 'X' TO CLEAR HISTORY OR 'C' TO COUNTINUE: ").strip().lower()
            if user_choice not in ('q', 'h','x', 'c'):
                print("Plz perform a valid Action")
                continue
            elif user_choice == "h":
                show_history()
                continue
            elif user_choice == 'x':
                clear_history()
                continue
            elif user_choice == 'c':
                break
            elif user_choice == 'q':
                break



        if user_choice == 'q':
            print("Thanks for using my calculator")
            break
    
main()

   





