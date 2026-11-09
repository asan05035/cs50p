import customer

def main():
    """ Create new customer purchase record and saving it"""
    txn_details = customer.create_transaction()
    txn_details.add_details()


if __name__ == "__main__":
    main()