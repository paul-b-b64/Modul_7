class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open('products.txt', 'r')
        read_file = file.read()
        file.close()
        return read_file

    def add(self, *procucts):
        for i in procucts:
            text = self.get_products()
            if i.name not in text:
                file = open('products.txt', 'a')
                file.write(f'\n{i.name}, {i.weight}, {i.category}')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
