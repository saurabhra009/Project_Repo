import pytest

class MyCalc:
    def __init__(self):
        self.ans = 0
    
    def add(self, num):
        # My UCID      ---> Smr9
        # Date written ---> 02/25/23
        # Summary: added given parameter num to running ans
        self.ans += num
        
        
    def subtract(self, num):
        # My UCID      ---> Smr9
        # Date written ---> 02/25/23
        # Summary: Subtract num from the running ans.
        self.ans -= num
    
    def multiply(self, num):
        # My UCID      ---> am3496
        # Date written ---> 02/21/23
        # Summary: Multiply the running ans by num.
        if self.ans == 0:
            self.ans = num
            return
        self.ans *= num
    
    def divide(self, num):
        # My UCID      ---> am3496
        # Date written ---> 02/25/23
        # Summary:Divide the running total by num.Return an error message if num is zero.
        if self.ans == 0:
            self.ans = num
            return
        if num == 0:
            print("Error: Cannot divide by zero.")
        else:
            self.ans /= num
    
def main():
     # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Function Summary: The main() function creates an instance of the MyCalc class, then enters a while loop that prompts 
    # the user to enter a mathematical expression or to exit the program. 
    # It uses the eval() function to evaluate the input string as a Python expression and prints the result. 
    # If the input string contains the substring "ans", it replaces it with the current value of the ans attribute of the MyCalc object.
    my_calc = MyCalc()
    while True:
        user_input = input("Enter a math expression or type 'exit' to quit: ")
        if user_input == "exit":
            break
        try:
            if "ans" in user_input:
                user_input = user_input.replace("ans", str(my_calc.ans))
                result = eval(user_input)
                my_calc.ans = result
                print(result)
            else:
                result = eval(user_input)
                my_calc.ans = result
                print(result)
        except:
            print("Invalid input")

def test_number_add_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_number_add_number() function tests the add() method of the MyCalc class by creating an instance of the class, 
    # adding two numbers to it, and checking that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.add(5)
    calc.add(10)
    assert calc.ans == 15

def test_ans_add_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    #Summary: The test_ans_add_number() function tests the add() method of the MyCalc class when the ans attribute 
    # has already been set.It sets the ans attribute, adds a number to it, and checks that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.ans = 5
    calc.add(10)
    assert calc.ans == 15

def test_number_sub_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    #Summary: The test_number_sub_number() function tests the subtract() method of the MyCalc class by creating an instance of the 
    # class, subtracting two numbers from it, and checking that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.subtract(5)
    calc.subtract(10)
    assert calc.ans == -15

def test_ans_sub_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_ans_sub_number() function tests the subtract() method of the MyCalc class when the 
    # ans attribute has already been set. 
    # It sets the ans attribute, subtracts a number from it,
    # and checks that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.ans = 5
    calc.subtract(10)
    assert calc.ans == -5

def test_number_mult_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_number_mult_number() function tests the multiply() method of the MyCalc 
    # class by creating an instance of the class, multiplying two numbers to it,
    # and checking that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.multiply(5)
    calc.multiply(10)
    assert calc.ans == 50

def test_ans_mult_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    #Summary: The test_ans_mult_number() function tests the multiply() method of the MyCalc class when the ans attribute has already been set. 
    # It sets the ans attribute, multiplies a number to it, and checks that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.ans = 5
    calc.multiply(10)
    assert calc.ans == 50

def test_number_div_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary:The test_number_div_number() function tests the divide() method of the MyCalc class by creating an instance of the class, 
    # dividing two numbers from it, and checking that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.divide(5)
    calc.divide(2)
    assert calc.ans == 2.5

def test_ans_div_number():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_ans_div_number() function tests the divide() method of the MyCalc class when the ans attribute has already been set.
    # It sets the ans attribute, divides a number from it, and checks that the value of the ans attribute is correct.
    calc = MyCalc()
    calc.ans = 5
    calc.divide(2)
    assert calc.ans == 2.5

def test_divide_by_zero():
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_divide_by_zero() function tests the divide() method of the MyCalc class when the input number is zero.
    # It creates an instance of the class, divides by zero, and checks that the value of the ans attribute is zero.
    calc = MyCalc()
    calc.divide(0)
    assert calc.ans == 0  


# additional tests with fixtures
@pytest.fixture
def new_calc():
    return MyCalc()

@pytest.mark.parametrize("nums, expected_ans", [
    ([5, 10], 15),
    ([0, 5, 10], 15),
    ([-5, -10], -15)
])
def test_addition(new_calc, nums, expected_ans):
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_addition function tests the addition operation, by adding each number in a list of nums to the calculator 
    # and checking if the resulting ans attribute of the
    # calculator matches the expected answer expected_ans.
    for num in nums:
        new_calc.add(num)
    assert new_calc.ans == expected_ans

@pytest.mark.parametrize("nums, expected_ans", [
    ([5, 10], -15),
    ([0, 5, 10], -15),
    ([-5, -10], 15)
])
def test_subtraction(new_calc, nums, expected_ans):
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_subtraction function tests the subtraction operation, by subtracting each number in a list of 
    # nums from the calculator and checking 
    # if the resulting ans attribute of the calculator matches the expected answer expected_ans.
    for num in nums:
        new_calc.subtract(num)
    assert new_calc.ans == expected_ans

@pytest.mark.parametrize("nums, expected_ans", [
    ([5, 10], 50),
    ([100, 20, 10], 20000),
    ([-5, 10], -50)
])
def test_multiplication(new_calc, nums, expected_ans):
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_multiplication function tests the multiplication operation, by multiplying each number in a list of nums 
    # to the calculator and checking if the resulting ans attribute of the calculator matches the expected answer expected_ans.
    for num in nums:
        new_calc.multiply(num)
    assert new_calc.ans == expected_ans

@pytest.mark.parametrize("nums, expected_ans", [
    ([5, 2], 2.5),
    ([100, 5,2], 10),
    ([-5, 2], -2.5)
])
def test_division(new_calc, nums, expected_ans):
    # My UCID      ---> Smr9
    # Date written ---> 02/25/23
    # Summary: The test_division function tests the division operation, by dividing the calculator by each number in a 
    # list of nums and checking if the resulting ans attribute of the calculator matches the expected answer expected_ans.
    for num in nums:
        new_calc.divide(num)
    assert new_calc.ans == expected_ans

