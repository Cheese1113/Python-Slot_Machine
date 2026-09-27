import random

MIN_LINES = 1 
MAX_LINES = 3 #constant value
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":3, 
    "B":4, 
    "C":6, 
    "D":8
    } #dictionary with no of symbols

symbol_value = {
    "A":5, 
    "B":4, 
    "C":3, 
    "D":2
    } #dictionary with no of symbols

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) #add symbol to list. Eg: Add 'A' 2 times
    
    columns = [] #nested lists = columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy entire list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #remove first instance of the symbol
            column.append(value)
    
        columns.append(column)
    
    return columns

def print_slot_machine(columns): #Transpose
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: #index 2
                print(column[row], "| ", end="") #Example: row 1 element 1, row 2 element 1.
            else:
                print(column[row], end="") #remove pipe in last element

        print() #next line

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] #first symbol in row
        for column in columns:
            symbol_to_check = column[line] #check if the other symbol in the row is == first symbol in row
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet #dict[key] = value
            winning_lines.append(line + 1)


    return winnings, winning_lines



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount) #string to integer
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("Invalid Input! Must be a number!")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on each line: (1 - " + str(MAX_LINES) + ")? ") #convert to string to avoid program crash
        if lines.isdigit():
            lines = int(lines) #string to integer
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount must be between " + str(MIN_LINES) + " - " + str(MAX_LINES) + "!")
        else:
            print("Invalid Input! Must be a number!")

    return lines
    
def get_bet():
    while True:
        bets = input("Enter the amount you want to bet (" + str(MIN_BET) + " - " + str(MAX_BET) + ")? $") #convert to string to avoid program crash
        if bets.isdigit():
            bets = int(bets) #string to integer
            if 1 <= bets <= MAX_BET:
                break
            else:
                print("Amount must be between " + "$" + str(MIN_BET) + " - " + "$" + str(MAX_BET) + "!")
        else:
            print("Invalid Input! Must be a number!")

    return bets

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough to bet that amount, your current balance is $" + str(balance) + "\n")
        else:
            break
    print("You are betting $" + str(bet) + " on " + str(lines) + " lines. Total bet is equal to $" + str(total_bet))

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print("You win on lines:", *winning_lines)
    print("You win $" + str(winnings) + "!")
    return winnings - total_bet
    

def main():
    balance = deposit()
    while True:
        print("Current balance is $" + str(balance))
        ans = input("Press enter to play (q to quit).").lower()
        if ans == 'q':
            break
        else:
            balance += spin(balance)
    
    print("You left with $" + str(balance))

main()