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
    with open("transaction_details.csv", "a") as file:
        file.write(record_details.transaction_details())
    print(f"Balance: {balance} ")

def get_customer_name():
    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        raise ValueError("Invalid customer name")
    return customer_name

def create_transaction():
    customer_name = get_customer_name()
    purchased_amount = float(input("Amount purchased: ").strip())
    cash_received = float(input("Cash received: ").strip())
    amount_due = cash_received - purchased_amount
    return [Transaction(customer_name, purchased_amount), amount_due]


if __name__ == "__main__":
    main()