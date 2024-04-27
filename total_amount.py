class Item:
    def total_amount_of_item(self,x,y):
        return x*y


item1 = Item()
item1.name ="phone"
item1.price = 1000
item1.quantity = 4
print(item1.total_amount_of_item(item1.price,item1.quantity))

item2 = Item()
item2.name ="mac"
item2.price = 1000088
item2.quantity = 63
print(item2.total_amount_of_item(item2.price,item2.quantity))