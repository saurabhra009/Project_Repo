<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Saurabh Rai (smr9)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 10:49:29 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/smr9" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221734243-2420ccad-0425-4b05-a252-214792da4b6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing Addition Function with date , ucid , summary commented<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221734244-e60ebc8d-d82e-4b7d-a2be-34cffb1690b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing Subraction Function with date , ucid and summary commented<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221748426-f16d3bde-1591-4063-85d8-145cf3a0805e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing Multiplication Function with date , ucid and summary commented<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221748430-6c7b0ca0-ce20-40dc-b6ff-411da01609a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing Division Function with handled division by zero error along with date<br>, ucid and summary commented<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735718-755de171-d022-4a7a-a741-fc35b6c45305.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test number-add-number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221736269-c8f82825-4bc5-42aa-a7e0-f438f763c180.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_addition function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_addition function test case result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735719-a575c987-5093-41e4-8f8f-8024efe80fab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_ans_add_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221736269-c8f82825-4bc5-42aa-a7e0-f438f763c180.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_addition function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans_add_number function test case result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221744638-758ce02f-fd4b-449e-86a4-f544e1f0c893.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of number-sub-number Test Case with commented date,ucid and function<br>summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221744640-2df67cd6-d0f4-4a04-a554-5e944d24abe3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_subtraction function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of number-sub-number function test case result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221744642-fd65ac3d-d30f-4186-996f-59d32978cdd3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_ans_sub_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221744640-2df67cd6-d0f4-4a04-a554-5e944d24abe3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_subtraction function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans-sub-number function test case result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746213-973fcb53-478e-4f28-82cd-f3d0fb3579fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_number_mult_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746215-5fc90505-062e-434d-858f-22fdcb87e9a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_number_mult_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_number_mult_number with commented date,ucid and function summary<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746217-8d0cde87-fd94-483b-8626-88b455ea850b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_ans_mult_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746215-5fc90505-062e-434d-858f-22fdcb87e9a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_multiplication function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans-multi-number function test case result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746860-c5eb4d8a-223d-482b-b7ef-e9ad0db26b81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_number_div_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746862-159f462b-bc81-45f2-8d59-ec8b6d5aa62e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_division function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of number-div-number function test case result<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746863-f859de70-af56-498b-a210-0486eeeccdf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a screenshot of test_ans_div_number with commented date,ucid and function summary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221746862-159f462b-bc81-45f2-8d59-ec8b6d5aa62e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing test_division function that process Processes a series of data to run<br>the test case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/221735057-c1155478-d30b-4081-9eb8-9040886ae60f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ans-div-number function test case result<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <div>I learned unit testing in Python using the pytest library during this lesson.<br>This session involved Individual units or components of a system are evaluated as<br>part of the software testing method known as unit testing to make sure<br>they function as intended. I discovered that a test case usually consists of<br>the expected output as well as a set of inputs for the system<br>being tested. The test fails if the result the system produces is not<br>what is anticipated.</div><div><br></div><div>Additionally, I discovered how to create a test case using pytest<br>to examine a class's functions. In order to check whether the outputs match<br>what we anticipate, I learned how to create an instance of a class<br>and call its methods with specific inputs. I also learned how to verify<br>whether a specific condition is true using the assert statement, and if it<br>is not, the test fails.</div><div><br></div><div>The final section of my review covered a simple<br>calculator class implementation using the add(), subtract(), multiply(), and divide() fundamental arithmetic methods<br>(). I also learned how to evaluate user-inputted mathematical expressions as Python code<br>using the eval() tool.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;Test scenarios are used to confirm that the code complies with the specifications<br>and performs as intended. It is a collection of requirements or inputs that<br>are used to assess the functionality of the program or application. To make<br>sure the software is dependable and fulfills user needs, testing is done.<div><div><br></div><div>A robust<br>Python testing tool that makes it simple to create and execute tests is<br>the pytest module. The MyCalc class&#39;s test cases are created in the aforementioned<br>code using the pytest package. A basic calculator that can add, subtract, multiply,<br>and split numbers is the MyCalc class.</div></div><div><br></div><div><div>To verify test findings, the pytest module<br>offers a selection of assertion methods. As an illustration, the assert line in<br>the test cases verifies that the value of the ans attribute of the<br>MyCalc object matches the anticipated value.</div><div><br></div><div>The MyCalc class is tested in the aforementioned<br>test cases using various inputs and situations to make sure it functions as<br>intended. The test number add number() code creates an instance of the MyCalc<br>class, adds two numbers to it, and verifies that the value of the<br>ans attribute is accurate before testing the add() method of the class. Similar<br>to this, the other test cases examine the MyCalc class&#39;s subtract(), multiply(), and<br>division() methods.</div></div><div><br></div><div>Overall, test cases are a crucial component of software development that ensure<br>the program functions as intended and meets user requirements. The pytest module makes<br>it simple to create and run tests and offers a number of practical<br>assertion methods to validate test results.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/6">https://github.com/saurabhra009/IS601-004/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/smr9" target="_blank">Grading</a></td></tr></table>