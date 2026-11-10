from datetime import datetime
import csv

class Transaction:
    def __init__(self, customer_name, amount_due, amount_paid, balance):
        self.customer_name = customer_name
        self.amount_due = amount_due
        self.amount_paid = amount_paid
        self.balance = balance
        self.time_of_purchase = datetime.now()

    def purchase_details(self):
        """ Details of purchase"""

        return [self.customer_name, self.amount_due, self.amount_paid, self.time_of_purchase]
    
    
    def add_details(self):  #cs50p file io csv writer
        """ Adding details of transaction to transaction.csv"""

        with open("transaction_details.csv", "a") as outfile:  
            writer = csv.writer(outfile)
            writer.writerow(self.purchase_details())

    def __str__(self):
        ...