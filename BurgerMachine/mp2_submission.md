<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Saurabh Rai (smr9)</td></tr>
<tr><td> <em>Generated: </em> 3/26/2023 1:11:17 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/smr9" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229389537-206b9728-87d6-43f7-8b39-9edea597b128.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot showing updated calculate_cost() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229389538-d66d871d-d5b5-462e-b6d4-3d8312037506.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing The input() message displaying display the value in currency format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <div>This is a method that calculates the cost of a burger order that<br>is currently in progress. The method iterates through each item in the inprogress_burger<br>list and adds its cost to the cost variable. Finally, it returns the<br>total cost of the burger order.<br></div><div>The currency formating is done using the&nbsp;<code>locale</code>&nbsp;module in<br>Python.The locale in this example is set to the system's default locale using<br>the locale.setlocale(locale.LC ALL, ") call, which should automatically utilize the correct currency symbol<br>and formatting for the user's locale.The expected value is then formatted as currency<br>using the locale.currency() method, and the user is then prompted to enter the<br>total in currency format using the input() function.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390069-271e7c16-3d97-4a3c-a7b0-62603a8c5bb2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of handling of OutOfStockException in handle_bun() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390073-e35e786b-5d85-4f3a-93d9-778ffeb4e671.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of handling of OutOfStockException in handle_patty() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390074-fec14c9b-4290-468b-a613-9861674ffe95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of handling of OutOfStockException in handle_toppings() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390075-7756233d-adab-43db-8498-7706d0aa163f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code snippet showing handling of NeedsCleaningException.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390658-f4258bf8-9849-48fc-9f98-f0d01e6cc447.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Handling of InvalidChoiceException at various stages of burgermachine while selecting bun<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390660-757037bd-4519-425b-91d0-412157be74f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Handling of InvalidChoiceException at various stages of burgermachine while selecting patty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390662-4e6c3085-a7a4-4dff-92aa-50e38efcafae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Handling of InvalidChoiceException at various stages of burgermachine while selecting toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390660-757037bd-4519-425b-91d0-412157be74f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing handling of ExceededRemainingChoicesException during burger making process while selecting patty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229390662-4e6c3085-a7a4-4dff-92aa-50e38efcafae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing handling of ExceededRemainingChoicesException during burger making process while selecting toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391044-4c079eb0-71a8-4111-b85b-45501598da6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing Handling of InvalidPaymentException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229416000-f0ca846b-8831-443c-ac99-1e4caa63d77a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of OutOfStockException for Bun and continue flow of program after<br>that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229405417-18c95e1f-053e-4b5d-b9df-5c9faae6576b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of OutOfStockException for Patty and continue flow of program after<br>that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229405418-3167d039-0688-432d-b227-e3da7450a61e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of OutOfStockException for Toppings and continue flow of program after<br>that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229406263-79c0d3ae-79c3-4cd2-9f15-88f259588f1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of NeedCleaningException i.e. machine is cleaned after certain use and<br>continue flow of program after that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229407110-71f504fc-a770-43b6-a974-71b00ec16816.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of InvalidChoiceException for Bun and continue flow of program after<br>that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229407112-6d95cf29-a7c8-4600-b9d6-28069575dac5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of InvalidChoiceException for Patty and continue flow of program after<br>that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229407113-c4b00e34-b05e-4410-a0f3-5812ebe331a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of InvalidChoiceException for Toppings and continue flow of program after<br>that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229408498-7eafe0a6-0ff4-48cb-b77d-964f753fd5cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of ExceededRemainingChoicesException for Patty(can&#39;t exceed more than 3)  and<br>continue flow of program after  that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229408506-2da96175-42a5-450f-b3d7-2da777b9714c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of ExceededRemainingChoicesException Toppings(can&#39;t exceed more than 3) and continue flow<br>of program after  that<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229407696-666f61d7-b040-4ef0-a46e-60d616f03616.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing output of InvalidPaymentException  and continue flow of program after <br>that<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><b>OutOfStockException:<br></b><div>If an OutOfStockException is raised, the program prints an appropriate message indicating which<br>item is out of stock, and then continues running. The user is given<br>the opportunity to make a different choice or move on to the next<br>stage/category.It tries to print that particular item is currently out of stock.</div><div><b>NeedsCleaningException:</b></div><div>When the<br>handle_patty() method raises a NeedsCleaningException, the program flow moves to the except block<br>and enters a while loop that prompts the user to enter &#39;clean&#39; to<br>clean the burger machine. Once the user enters &#39;clean&#39;, the machine is cleaned<br>and the remaining uses is reset to the maximum uses before needing to<br>be cleaned.<br>If the user does not enter &#39;clean&#39;, the program will continue to<br>prompt the user until they enter the correct input. Once the machine is<br>cleaned, the program flow will continue to the next step in the current<br>stage of the burger building process.<b><br></b></div><div><b>InvalidChoiceException:</b></div><div>The InvalidChoiceException is handled using a try-except block<br>in the provided code. If the exception is raised when the user selects<br>an invalid bun, the except block is executed. The code prints out a<br>message &quot;Invalid choice. Please select a valid bun.&quot; to prompt the user to<br>choose a valid option. After that, the current burger is printed using the<br>print_current_burger() method.</div><div><b>ExceededRemainingChoicesException:</b></div><div>if the ExceededRemainingChoicesException is raised during the execution of the handle_toppings method<br>or handle_patty method, it will be caught by the try-except block. The code<br>inside the except ExceededRemainingChoicesException block will be executed, which will print the message<br>&quot;You have reached the maximum number of toppings allowed.&quot; to the console.<br></div><div><b>InvalidPaymentException:</b></div><div>InvalidPaymentException is<br>a custom exception class that is raised when a payment made by a<br>customer is invalid.<br>When this exception is raised, the code inside the except block<br>is executed, which in this case is simply printing a message &quot;Invalid Payment,Please<br>try again.&quot; to the console.<br>Therefore, if an InvalidPaymentException is raised in the try<br>block, the code will handle it by printing a message to the console,<br>informing the user that the payment was invalid and suggesting they try again.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391160-8fc8d1f5-55ee-4b20-a3bc-24bb8fc9b060.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 1-bun must be the first<br>selection (can&#39;t add patties/toppings without a bun choice)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391161-833e91b2-8906-4a6f-a8c5-6903f223be71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 2-can only add patties if<br>they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391162-a21df1e2-15d7-46a5-91b5-eb935e8a81c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 3-can only add toppings if<br>they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391164-54500f04-af3a-4bc8-8508-26c1f84be4ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 4- Can add up to<br>3 patties of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391165-d68a427c-367d-4dbf-9399-5c2ce90d43bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 5-Can add up to 3<br>patties of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391166-95e74f21-bf5e-4894-ab4b-efc888924161.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 6-cost must be calculated properly<br>based on the choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391167-98bf1e7f-d90a-4782-acaa-07333c634aa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 6-cost must be calculated properly<br>based on the choices with different permutation of burgers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391169-c9939924-8efc-42f0-8be9-bf75a61ec968.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 6 - to check the<br>currency format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391171-eae8e026-4341-4228-887a-7306de334d07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 7-Total Sales (sum of costs)<br>must be calculated properly (test case should have a few permutations of at<br>least 3 valid burgers)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229391172-dbcf0b60-92ce-4322-a305-b591538e94c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing code snippet to deal with test 8- Total burgers should properly<br>increment for each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229415434-b775a26a-4770-46ec-983e-78ca51e51753.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing output for all Tests 1-8 passing.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div><b>Test 1:&nbsp;The first assertion checks that when the user tries to select a<br>patty before selecting a bun, the pick_patty method should raise an InvalidStageException. This<br>exception is likely defined by the BurgerMachine class to indicate that the user<br>is trying to perform an action out of order.</b></div><div><b><br></b></div><div><b>Similarly, the second assertion checks<br>that when the user tries to select toppings before selecting a bun, the<br>pick_toppings method should raise an InvalidStageException.</b></div><div><b><br></b></div><div><b>Overall, this test case ensures that the BurgerMachine<br>class enforces the correct order of operations for making a burger and that<br>it raises the appropriate exception if a user tries to perform an action<br>out of order.</b></div><div><b><br></b></div><div><b>Test 2: T</b><b>est function, 2 "test_patties_out_of_stock_exception()", tests whether the "BurgerMachine" class<br>raises an exception when attempting to add a patty to a burger when<br>there are no remaining patties in stock. The test initializes an instance of<br>the "BurgerMachine" class, sets the&nbsp; patties quantity count to 0, handles a "Lettuce<br>Wrap", and then attempts to add a "Turkey patty. The test uses the<br>"pytest.raises" context manager to assert that the expected exception, "OutOfStockException", is raised.</b></div><div><b><br></b></div><div><b>Test 3:&nbsp;</b><b>T</b><b>est<br>function, 3 "test_toppings_out_of_stock_exception()", tests whether the "BurgerMachine" class raises an exception when attempting<br>to add a topping to a burger when there are no remaining topping<br>in stock. The test initializes an instance of the "BurgerMachine" class, sets the&nbsp;<br>toppings quantity count to 0, handles a "Lettuce Wrap", and then add next<br>for patty and while selecting toppings it raises OutOfStockException. The test uses the<br>"pytest.raises" context manager to assert that the expected exception, "OutOfStockException", is raised.</b></div><div><b><br></b></div><div><b>Test 4:&nbsp;</b><b>The<br>test starts by creating an instance of the BurgerMachine class and specifying the<br>type of bun and patty for the burger. Then, it adds three different<br>types of toppings to the burger using the handle_toppings method of the BurgerMachine<br>class. Finally, it tests that the handle_toppings method throws an exception when the<br>user tries to add a fourth topping or tries to add more toppings<br>of the same type.</b></div><div><b><br></b></div><div><div><b>Test 5:&nbsp;The test starts by creating an instance of the<br>BurgerMachine class and specifying the type of bun for the burger. Then, it<br>adds three different types of patties to the burger using the handle_patty method<br>of the BurgerMachine class. Finally, it tests that the handle_patty method throws an<br>exception when the user tries to add a fourth patty or tries to<br>add more patties of the same type.</b></div><div><b><br></b></div><div><div><b>Test 6:&nbsp;The first test, test_cost_calculation, checks whether<br>the calculate_cost() method of the BurgerMachine class calculates the cost of the burger<br>correctly. It starts by creating an instance of the BurgerMachine class and tries<br>to add a patty without first specifying the type of bun, which should<br>raise an InvalidStageException. Then, it adds a beef patty and two toppings (cheese<br>and lettuce) and marks the burger as done. Finally, it checks that the<br>calculate_cost() method returns the expected cost of 1.25.</b></div><div><br></div><div><b>The second test, test_currency_format, checks whether<br>the calculate_cost() method returns the cost in the expected currency format. It starts<br>by creating an instance of the BurgerMachine class and follows the same steps<br>as in the previous test to create a burger and calculate its cost.<br>Then, it checks that the cost returned by the calculate_cost() method is equal<br>to 1.25 and that the locale.currency() method returns this value formatted as "$1.25".</b></div></div><div><br></div><div><b>Test<br>7:&nbsp;The test_total_sales_calculation function tests whether the total_sales attribute of the BurgerMachine class is<br>updated correctly when a burger is purchased. It starts by creating an instance<br>of the BurgerMachine class and building three different burgers using the handle_bun(), handle_patty(),<br>handle_toppings(), and handle_pay() methods. The handle_pay() method is used to simulate a customer<br>paying for the burger with a specific amount of money.</b></div><div><b><br></b></div><div><b>After building the three<br>burgers, the expected total sales are calculated by adding up the prices paid<br>for each burger. Then, the test checks whether the total_sales attribute of the<br>BurgerMachine class is equal to the expected total sales using an assertion.</b></div><div><b><br></b></div><div><b>Test 8:&nbsp;The<br>test creates an instance of the BurgerMachine class and calls the handle_bun, handle_patty,<br>handle_toppings, and handle_pay methods to simulate ordering three different burgers. Each burger order<br>is marked as "done" using the handle_toppings method, which triggers the increment of<br>the total_burgers attribute. The test checks that the total_burgers attribute is correctly incremented<br>after each order by calling assert statements.</b></div><div><b><br></b></div><div><b>If the total_burgers attribute is implemented correctly<br>in the BurgerMachine class, and the handle_toppings method increments the attribute when the<br>order is marked as "done," then this test should pass without errors.</b></div></div><div><b><br></b></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/14">https://github.com/saurabhra009/IS601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <div><b>Issues:</b></div><div>Syntax errors: Any typos or syntax errors in the code can cause it<br>to fail to run or produce unexpected results.</div><div>Incorrect output: If the code is<br>not written correctly, it may produce incorrect results or throw errors during execution.<br>For example, if the use() method of the Usable class is called when<br>the quantity attribute is already zero, the OutOfStockException will be raised, but the<br>code may not be properly handling the exception, resulting in incorrect behavior.</div><div><b>Learnings:</b></div><div><b>Object-Oriented Programming:&nbsp;</b>This<br>project is an example of object-oriented programming (OOP) in Python. It uses classes,<br>inheritance, and objects to represent various items and components of a burger machine.<br><b><br></b></div><div><b>Exception<br>Handling:&nbsp;</b>The project demonstrates how to use exception handling in Python to handle errors<br>and unexpected situations. It defines several custom exceptions, such as OutOfStockException, InvalidChoiceException, and<br>InvalidStageException, and raises them when necessary.<br><b><br>Enumerations:&nbsp;</b>The project uses enumerations in Python to represent<br>the stages of burger assembly. It defines an STAGE enumeration with four values:<br>Bun, Patty, Toppings, and Pay. This allows the program to enforce the rule<br>that the bun must be chosen first, followed by the patty, toppings, and<br>payment.<br><b><br>Good Programming Practices:</b>&nbsp;The project follows good programming practices such as using constants instead<br>of hard-coding values, using descriptive variable and function names, using docstrings to document<br>functions, and separating the code into logical sections and modules.<br><br><b>Localization:</b>&nbsp;The project uses the<br>locale module in Python to set the locale to 'en_US'. This allows the<br>program to format numbers and currency values in a way that is appropriate<br>for the United States. This is an important consideration when dealing with user-facing<br>output, as users in different regions may expect different formatting.<br><br><b>Input Validation:</b>&nbsp;The project validates<br>user input to ensure that it is valid and appropriate for the current<br>stage of the burger assembly process. For example, if the user tries to<br>choose a patty before choosing a bun, or if the user tries to<br>add too many toppings, the program will raise an InvalidStageException or ExceededRemainingChoicesException, respectively.<br><br><b>State<br>Management:&nbsp;</b>The project keeps track of the state of the burger machine, such as<br>the number of remaining patties, toppings, and uses until cleaning. It uses this<br>state information to enforce rules and constraints on the burger assembly process, such<br>as the maximum number of patties and toppings, and the need for cleaning<br>after a certain number of uses.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229409437-2a4302b8-7bc8-49fe-8d25-2cbc0a7ce3ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows selection of white burger bun, turkey, veggie,  cheese, tomato,<br>mayo. The total price of this burger comes out to be $3.75.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229409438-0bb350bd-83a7-45f4-b1a3-b219dccd823d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows selection of Lettuce Wrap, turkey, veggie, beef , Ketchup, Pickles.<br>The total price of this burger comes out to be $5.00.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/229409439-f949ce40-8c80-4049-85b1-40f27ce2b2ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The screenshot shows selection of wheat burger bun, veggie,  cheese, mayo, mustard.<br>The total price of this burger comes out to be $3.00.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/smr9" target="_blank">Grading</a></td></tr></table>