import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException,NeedsCleaningException
#this is an example test showing how to cascade fixtures to build up state
from BurgerMachine import BurgerMachine, STAGE, Bun, Patty, Topping
import locale
@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False

# add required test cases below

# # Test 1 - bun must be the first selection (can't add patties/toppings without a bun choice)
def test_pick_bun_first():
    burger_machine = BurgerMachine()
    with pytest.raises(InvalidStageException):
        burger_machine.pick_patty("Beef")
    with pytest.raises(InvalidStageException):
        burger_machine.pick_toppings("Lettuce")
        


def test_add_patties_in_stock():
    burger_machine = BurgerMachine()
    burger_machine.handle_bun("White Burger Bun")
    burger_machine.handle_patty("Beef")
    assert burger_machine.remaining_patties == 2

def test_add_patties_out_of_stock():
    burger_machine = BurgerMachine()
    burger_machine.remaining_patties = 0
    burger_machine.handle_bun("White Burger Bun")
    with pytest.raises(ExceededRemainingChoicesException):
        burger_machine.pick_patty("Beef")



def test_add_toppings_in_stock():
    burger_machine = BurgerMachine()
    burger_machine.handle_bun("White Burger Bun")
    burger_machine.handle_patty("Beef")
    burger_machine.handle_patty("next")
    burger_machine.handle_toppings("Lettuce")
    assert burger_machine.remaining_toppings == 2

def test_add_toppings_out_of_stock():
    burger_machine = BurgerMachine()
    burger_machine.remaining_toppings = 0
    burger_machine.handle_bun("White Burger Bun")
    burger_machine.handle_patty("Beef")
    burger_machine.handle_patty("next")
    with pytest.raises(ExceededRemainingChoicesException):
        burger_machine.handle_toppings("Lettuce")
        

def test_only_3_add_patties():
    # create an instance of the BurgerMachine
    burger_machine = BurgerMachine()
    # pick a bun first
    burger_machine.handle_bun("White Burger Bun")
    # pick 3 different types of patties
    burger_machine.handle_patty("Beef")
    burger_machine.handle_patty("Veggie")
    burger_machine.handle_patty("Turkey")
    # try to add a 4th patty
    with pytest.raises(ExceededRemainingChoicesException):
        burger_machine.handle_patty("Beef")
    # try to add another patty of the same type
    with pytest.raises(ExceededRemainingChoicesException):
        burger_machine.handle_patty("Beef")
        # add another patty of a different type
        burger_machine.handle_patty("Veggie")


def test_only_3_add_toppings():
    # create an instance of the BurgerMachine
    burger_machine = BurgerMachine()
    # pick a bun first
    burger_machine.handle_bun("White Burger Bun")
    burger_machine.handle_patty("Beef")
    burger_machine.handle_patty("next")
    
    # pick 3 different types of toppings
    burger_machine.handle_toppings("Lettuce")
    burger_machine.handle_toppings("Tomato")
    burger_machine.handle_toppings("Pickles")
    # try to add a 4th topping
    with pytest.raises(ExceededRemainingChoicesException):
        burger_machine.handle_toppings("Ketchup")
    # try to add another topping of the same type
    with pytest.raises(ExceededRemainingChoicesException):
        burger_machine.handle_toppings("Mayo")
        # add another topping of a different type
        burger_machine.handle_toppings("Mustard")
    

def test_cost_calculation( ):
    burger_machine = BurgerMachine()
    with pytest.raises(InvalidStageException):
        burger_machine.handle_patty("Beef")
        burger_machine.handle_patty("next")
        burger_machine.handle_toppings("Cheese")
        burger_machine.handle_toppings("Lettuce")
        burger_machine.handle_toppings("done")
        assert burger_machine.calculate_cost() == 1.25

def test_cost_calculation_with_multiple_toppings( ):
    burger_machine = BurgerMachine()
    with pytest.raises(InvalidStageException):
        burger_machine.handle_bun("Wheat Burger Bun")
        burger_machine.handle_patty("Beef")
        burger_machine.handle_toppings("Cheese")
        burger_machine.handle_toppings("Lettuce")
        burger_machine.handle_toppings("Tomato")
        assert burger_machine.calculate_cost() == 2.0

def test_currency_format( ):
    burger_machine = BurgerMachine()
    with pytest.raises(InvalidStageException):
        burger_machine.handle_patty("Beef")
        burger_machine.handle_patty("next")
        burger_machine.handle_toppings("Cheese")
        burger_machine.handle_toppings("Lettuce")
        burger_machine.handle_toppings("done")
        cost = burger_machine.calculate_cost()
        assert cost == 1.25
        assert locale.currency(cost) == "$1.25"

def test_cost_calculation_with_invalid_choices( ):
    burger_machine = BurgerMachine()
    with pytest.raises(Exception):
        burger_machine.handle_bun("Brioche Bun")
    with pytest.raises(Exception):
        burger_machine.handle_patty("Chicken")
    with pytest.raises(Exception):
        burger_machine.handle_toppings("Bacon")



def test_total_burgers_increment():
    machine = BurgerMachine()
    with pytest.raises(InvalidStageException):
        machine.handle_bun("White Burger Bun")
        machine.handle_patty("Beef")
        machine.handle_toppings("Cheese")
        machine.handle_toppings("Ketchup")
        machine.handle_toppings("done")
        assert machine.total_burgers == 1

        machine.handle_bun("Wheat Burger Bun")
        machine.handle_patty("Veggie")
        machine.handle_toppings("Lettuce")
        machine.handle_toppings("Tomato")
        machine.handle_toppings("done")
        assert machine.total_burgers == 2

        machine.handle_bun("Lettuce Wrap")
        machine.handle_patty("Turkey")
        machine.handle_toppings("Mustard")
        machine.handle_toppings("Mayo")
        machine.handle_toppings("BBQ")
        machine.handle_toppings("done")
        assert machine.total_burgers == 3
        
def test_total_sales_calclation():
    machine = BurgerMachine()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(2,'2')
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(3,'3')
    machine.handle_bun("no Bun")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Mayo")
    machine.handle_toppings("done")
    machine.handle_pay(1.25,'1.25')
    expected_total_sales = 2 + 3 + 1.25
    assert(expected_total_sales==machine.total_sales)
        
        
# Miscellaneous Test Cases
def test_invalid_choice():
    burger_machine = BurgerMachine()
    burger_machine.handle_bun("White Burger Bun")
    with pytest.raises(InvalidChoiceException):
        burger_machine.handle_patty("Invalid Patty")



def test_add_patty_with_needs_cleaning():
    burger_machine = BurgerMachine()
    burger_machine.remaining_uses = 0
    burger_machine.handle_bun("White Burger Bun")
    with pytest.raises(NeedsCleaningException):
        burger_machine.handle_patty("Beef")
#
def test_add_patty_with_invalid_stage():
    burger_machine = BurgerMachine()
    burger_machine.currently_selecting = STAGE.Toppings
    with pytest.raises(InvalidStageException):
        burger_machine.handle_patty("Beef")
        


def test_out_of_stock_exception():
    machine = BurgerMachine()
    machine.buns[0].quantity = 0
    with pytest.raises(OutOfStockException):
        machine.pick_bun("no bun")

def test_exceeded_remaining_choices_exception():
    machine = BurgerMachine()
    machine.remaining_toppings = 0
    machine = BurgerMachine()
    machine.currently_selecting = STAGE.Toppings
    machine.remaining_toppings = 0
    topping = Topping(name="Lettuce", quantity=5, cost=0.50)
    machine.toppings.append(topping)
    with pytest.raises(ExceededRemainingChoicesException):
        machine.pick_toppings("lettuce")
        


