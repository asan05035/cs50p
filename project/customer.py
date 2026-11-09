import txn

def get_name():         #cs50p exceptionlecture
    """ Get customer name"""
    while True:
        try:
            customer_name = input("Enter customer name: ").strip()
            if not customer_name:
                raise ValueError("Invalid customer name")
            return customer_name
        except ValueError: 
            pass

def get_cash(prompt):  #Cs50p ps fuel gauge
    """ Get cash """
    while True:
        try:
            cash = int(input(prompt).strip())
            if cash <= 0:
                raise ValueError
            return cash
        except ValueError:
            pass 

def create_transaction():   #CS50P oop lecture
    """ Creating new trsanction object """
    customer_name = get_name()
    purchased_amount = get_cash("Amount Purchased: ")
    cash_received = get_cash("Cash Received: ")
    balance = cash_received - purchased_amount
    return txn.Transaction(customer_name, purchased_amount, cash_received, balance)   
