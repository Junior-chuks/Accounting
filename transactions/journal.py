print("[Module] Journal loaded.")


def receive_income(amount):
    '''Displays the income.'''
    amount_2 = "{:.2f}".format(amount)
    print(f"[Journal] Received R{amount_2}")


def pay_expense(amount):
    '''Displays the amount paid.'''
    amount_2 = "{:.2f}".format(amount)
    print(f"[Journal] Paid R{amount_2}")