from tinydb import TinyDB


class DB:
    def __init__(self, file_name: str):
        self.db = TinyDB(file_name, indent=4)
        self.products = self.db.table('products')

    def add_product(self, name, description, price, quantity):
        pass

    def get_product(self, id):
        pass

    def update_product(self, name, description, price, quantity):
        pass

    def delete_product(self, id):
        pass
    
    def get_all_products(self):
        pass