from datetime import datetime, date


class Transaction:
    def __init__(self, customer_name, amount_purchased):
        self.customer_name = customer_name
        self.amount_purchased = amount_purchased
        self.time_of_purchase = date.today()

    def transaction_details(self):
        return f"{self.customer_name},{self.amount_purchased},{self.time_of_purchase}\n"

    def __str__(self):
        ...


def main():
    record_details, balance = create_transaction()
    create_record(record_details)


def create_record(record):
    with open("transaction_details.csv", "a") as file:
        file.write(record.transaction_details())
    


def get_customer_name():
    while True:
        try:
            customer_name = input("Enter customer name: ").strip()
            if not customer_name:
                raise ValueError("Invalid customer name")
            return customer_name
        except ValueError: 
            pass

def get_cash(prompt):                       #Cs50p ps fuel gauge
    while True:
        try:
            cash = int(input(prompt).strip())
            if cash <= 0:
                raise ValueError
            return cash
        except ValueError:
            pass 

def create_transaction():
    customer_name = get_customer_name()
    purchased_amount = get_cash("Amount Purchased: ")
    cash_received = get_cash("Cash Received: ")
    amount_due = cash_received - purchased_amount
    return [Transaction(customer_name, purchased_amount), amount_due]   #CS50P oop lecture


if __name__ == "__main__":
    main()