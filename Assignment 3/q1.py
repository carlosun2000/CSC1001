class Flower:
    def __init__(self,name='rose',number_of_pedals='1',price='88'):
        self.__name = name
        self.__number_of_pedals = number_of_pedals
        self.__price = price
    def set_name(self):
        name = obtain_the_name()
        while True:
            try:
                name = str(name)
                self.__name = name
                break
            except:
                print('not a valid name')
    def set_number_of_pedals(self):
        number_of_pedals=obtain_the_number_of_pedals()
        while True:
            try:
                self.__number_of_pedals = number_of_pedals
                break
            except:
                print('not a valid number of pedals')
    def set_price(self):
        price = obtain_the_price()
        while True:
            try:
                self.__price = price
                break
            except:
                print('not a valid price')

    def get_name(self):
        
        return self.__name
    def get_number_of_pedals(self):
        
        return self.__number_of_pedals
    def get_price(self):
        
        return self.__price

def obtain_the_name():
    name = input('Enter the name: ')
    return name

def obtain_the_number_of_pedals():
    while True:
        try:
            number= int(input('enter the pedals: '))
            if number>0:
                return number
            else:
                print('invalid input, try again!')
        except:
            print('invalid input, try again!')

def obtain_the_price():
    while True:
        try:
            price = float(input('enter the price: '))
            if price>0:
                return price
            else:
                print('invalid input, try again!')
        except:
            print('invalid input, try again')

flower = Flower()
flower.set_name()
flower.set_number_of_pedals()
flower.set_price()
print(
    'the name is {} the number of pedal is {} the price is {}'.format(
        flower.get_name(),
        flower.get_number_of_pedals(),
        flower.get_price()
    )
)