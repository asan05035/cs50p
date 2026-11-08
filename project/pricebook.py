class Pricebook:
    price_book = []

    @classmethod
    def add_item(cls, item_name, price, quantity):
        cls.price_book.append({
            "item_name" : item_name,
            "price" : price,
            "quantity" : quantity
        })

    @classmethod
    def update_item(cls):
        ...

    @classmethod
    def remove_item(cls):
        ...

    @classmethod
    def inventory_items(cls):
        print(cls.price_book)
