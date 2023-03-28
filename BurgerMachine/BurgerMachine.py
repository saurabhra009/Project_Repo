from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            print
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0
    def __repr__(self) -> str:
        return self.name

class Bun(Usable):
    pass

class Patty(Usable):
    pass

class Topping(Usable):
    pass

class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4

class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3


    buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun("Wheat Burger Bun", cost=1.25),Bun("Lettuce Wrap", cost=1.5)]
    patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(name="Veggie", quantity=10, cost=1), Patty(name="Beef", quantity=10, cost=1)]
    toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25), Topping(name="Pickles", quantity=10, cost=.25), \
    Topping(name="Cheese", quantity=10, cost=.25), Topping(name="Ketchup", quantity=10, cost=.25),
    Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25),Topping(name="BBQ", quantity=10, cost=.25)] 

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_patties = MAX_PATTIES
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_burgers = 0
    

    inprogress_burger = []
    currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment
    

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        raise InvalidChoiceException

    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            raise ExceededRemainingChoicesException
        for f in self.patties:
            if f.name.lower() == choice.lower():
                if f.in_stock():
                    f.use()                    
                    self.inprogress_burger.append(f)
                    self.remaining_patties -= 1
                    self.remaining_uses -= 1
                    return
        raise InvalidChoiceException


    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException
        


        


    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your burger!")
            self.total_burgers += 1
            self.total_sales += expected # only if successful
            print(f"Total Burgers Sold {self.total_burgers}")
            print(f"Total sales so far {locale.currency(self.total_sales)}")
            self.reset()
        else:
            raise InvalidPaymentException
        
    def print_current_burger(self):
        print(f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_burger
        # My UCID Smr9
        # Date:03/20/23
        # This method iterates through the inprogress_burger list and adds up
        # the cost of each item to the cost variable. Finally, it returns the calculated cost.
        cost = 0
        for item in self.inprogress_burger:
            cost += item.cost
        return cost

        
    def run(self):
        # My UCID Smr9
        # Date:03/20/23
        try:
            if self.currently_selecting == STAGE.Bun:
                # My UCID Smr9
                # Date:03/20/23            
                bun = input(f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                while bun.lower() == "no bun":
                    print("can't add patties/toppings without a bun choice")
                    bun = input(f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                    
                try:
                    self.handle_bun(bun)
                except OutOfStockException:
                    print(f"{bun} is currently out of stock.")
                except InvalidChoiceException:
                    print("Invalid choice. Please select a valid bun.")
                self.print_current_burger()
                
                
            elif self.currently_selecting == STAGE.Patty:
                # My UCID Smr9
                # Date:03/20/23
                patty = input(f"Would type of patty would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                try:
                    self.handle_patty(patty)
                except OutOfStockException:
                    print(f"{patty} is currently out of stock.")
                    return
                except NeedsCleaningException:
                    while True:
                        clean = input("The burger machine needs cleaning. Type 'clean' to clean the machine: ")
                        if clean.lower() == "clean":
                            print("The machine has been cleaned.")
                            self.remaining_uses = self.USES_UNTIL_CLEANING
                            break
                except InvalidChoiceException:
                    print("Invalid choice. Please select a valid patty.")
                except ExceededRemainingChoicesException:
                    print("**You have exceeded the maximum number of patties for this burger.**")
                    print("Can add up to 3 patties of any combination!")
                    
                    
                self.print_current_burger()
                
                
            elif self.currently_selecting == STAGE.Toppings:
                # My UCID Smr9
                # Date:03/20/23
                toppings = input(f"What topping would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                try:
                    self.handle_toppings(toppings)
                except OutOfStockException:
                    print(f"{toppings} is currently out of stock.")
                except InvalidChoiceException:
                    print("Invalid choice. Please select a valid topping.")
                except ExceededRemainingChoicesException:
                    print("**You have reached the maximum number of toppings allowed**")
                    print("Can add up to 3 toppings of any combination!")
                self.print_current_burger()
                
            elif self.currently_selecting == STAGE.Pay:
                # show expected value as currency format
                # require total to be entered as currency format
                # My UCID Smr9
                # Date:03/20/23
                expected = self.calculate_cost()
                total = input(f"**Your total is {locale.currency(expected)}, please enter the exact value.**\n")
                # the locale.setlocale(locale.LC_ALL, 'en_US') call sets the locale to the default locale on the system, 
                # which should automatically use the appropriate currency symbol and formatting for the user's locale. 
                # The locale.currency() function is then used to format the expected value as currency, and the input() 
                # function is used to prompt the user to enter the total in currency format.
                try:
                    # My UCID Smr9
                    # Date:03/20/23
                    self.handle_pay(expected, total)
                except InvalidPaymentException:
                    print("Invalid Payment,Please try again.")
                    self.handle_pay(expected, total)

                
                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    #exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the burger machine")
                    return 1
                
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()
        
        # handle InvalidChoiceException
            # show an appropriate message of what stage/category was the invalid choice was in
        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category
        # handle InvalidPaymentException
            # show an appropriate message
        except:
            # this is a default catch all, follow the steps above
            print("Something went wrong")
        
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()