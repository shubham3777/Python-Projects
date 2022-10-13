import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)     # choose a value from current_symbols list
            current_symbols.remove(value)       # Remove the random selected value from current_symbols list
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")

        print()


def deposit():
    while True:
        amount = input("What you want to deposit? : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a valid digit")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on(1-" + str(MAX_LINES) + ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("Please enter a number")

    return lines


def get_bet():
    while True:
        bet = input("What would you like to bet? : ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a bet in between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return bet


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is {balance}")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Your total bet is {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings} !!!!!!!!")
    print(f"You won on lines : ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is {balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}")


main()