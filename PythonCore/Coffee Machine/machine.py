class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print(f'The coffee machine has:\n{self.water} of water\n{self.milk} of milk\
                \n{self.beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money')

    def buy(self):
        coffee_tuple = ('espresso', 'latte', 'cappuccino')
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::\n')
        if coffee.isdigit():
            coffee = int(coffee) - 1
            coffee_dict = {coffee_tuple[0]: {'water': 250, 'milk': 0, 'beans': 16, 'money': 4},
                           coffee_tuple[1]: {'water': 350, 'milk': 75, 'beans': 20, 'money': 7},
                           coffee_tuple[2]: {'water': 200, 'milk': 100, 'beans': 12, 'money': 6}}
            if self.water - coffee_dict[coffee_tuple[coffee]]['water'] < 0:
                return 'Sorry, not enough water!'
            elif self.milk - coffee_dict[coffee_tuple[coffee]]['milk'] < 0:
                return 'Sorry, not enough milk!'
            elif self.beans - coffee_dict[coffee_tuple[coffee]]['beans'] < 0:
                return 'Sorry, not enough beans!'
            elif self.cups - 1 < 0:
                return 'Sorry, not enough cups!'
            self.water -= coffee_dict[coffee_tuple[coffee]]['water']
            self.milk -= coffee_dict[coffee_tuple[coffee]]['milk']
            self.beans -= coffee_dict[coffee_tuple[coffee]]['beans']
            self.money += coffee_dict[coffee_tuple[coffee]]['money']
            self.cups -= 1
            return False

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:\n'))
        self.milk += int(input('Write how many ml of milk you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.cups += int(input('Write how many disposable coffee cups you want to add:\n'))

    def take(self):
        print(f'I gave you {self.money}')
        self.money = 0

    def start_machine(self):
        command = input('Write action (buy, fill, take, remaining, exit):\n')
        while command != 'exit':
            if command == 'remaining':
                self.remaining()
            elif command == 'buy':
                n = self.buy()
                if n:
                    print(n)
            elif command == 'fill':
                self.fill()
            elif command == 'take':
                self.take()
            command = input('Write action (buy, fill, take, remaining, exit):\n')


if __name__ == '__main__':
    CoffeeMachine().start_machine()
