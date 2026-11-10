from string import capwords
"""
    Getting item purchased total 
    
    Ref: CS50P...Problem set 3...Felips Tequira
"""
def amount():
    """ Get total of items purchased"""
    return get_total()

def get_item(item):
      """ List of items avaiilable"""
      item_list = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
      return item_list[item]

def get_count():
    while True:
        try:
            item_count = int(input("Count: "))
            return item_count
        except ValueError:
            pass
    


def get_total():
    """ Iterate to get the items total till user stop"""
    total = 0
    
    while True:
        try:
            user_input = capwords(input("Item: ").strip())
            total = total + (get_item(user_input) * get_count())
            print(f"Total: ${total}")
        except KeyError:
            pass
        except EOFError:
            return total

if __name__ == "__main__":
    amount()
