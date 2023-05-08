<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Saurabh Rai (smr9)</td></tr>
<tr><td> <em>Generated: </em> 5/8/2023 3:02:30 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/smr9" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236730452-d884231c-e5cd-4183-9f38-9d2dbd5f602f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User with admin or shop owner will be able to add products (Valid<br>data filled in)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236730453-49a44c8b-6f23-4860-8b39-66aff1aec578.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success message of admin being able to add products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236730821-0064ce93-8c3f-42aa-8096-35b5f9aede1f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of populated Products table clearly showing the columns<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">WTF With the aid of<br>the tool called Forms, users can create forms with a variety of fields,<br>including name (a string data type), description (a text area field), category (also<br>a text area field), stock (a numerical data type), unit price (another numerical<br>data type), picture field, visibility field, and submit button. These fields come with<br>the necessary validators to make sure that the entered data follows the guidelines<br>for a specific product.&nbsp;</p><p class="MsoNormal" style="margin: 0in;"><font face="Calibri, sans-serif"><span style="font-size: 16px;">An If-else block<br>is used to generate code for either modifying an existing product or generating<br>a new one after the form has been submitted. The form data is<br>entered into the products table using a SQL Insert command if the form<br>request has no ID (signifying the creation of a new product). The form<br>data is cleared and a flash message indicating the successful insertion of the<br>new record is displayed if the insertion is successful. A flash message indicating<br>an error is presented if the insertion fails.</span></font><br></p><p class="MsoNormal" style="margin: 0in;"><font face="Calibri, sans-serif"><span<br>style="font-size: 16px;">HTML is used to build form helpers, which make creating HTML files<br>for forms and handling their various fields simpler. These tools use Jinja templates<br>to get the layout file, header, and input form text and can handle<br>a variety of field kinds, such as form-control and boolean.</span></font></p><p class="MsoNormal" style="margin: 0in;"></p><p<br>class="MsoNormal" style="margin: 0in;"><font face="Calibri, sans-serif"><span style="font-size: 16px;">All required columns' input fields are created<br>using the render field function.</span></font></p><div><br></div><p class="MsoNormal" style="margin: 0in;"><font face="Calibri, sans-serif"><span style="font-size: 16px;"><br></span></font></p><p class="MsoNormal"<br>style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/59">https://github.com/saurabhra009/IS601-004/pull/59</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/admin/item">https://is601-smr9-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236732363-34bb6492-bfe6-4c71-856c-cd0944cf8f10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>creenshot of the Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236733631-6f823328-fe4a-44af-962b-22180d5fd3bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied-should<br>be more than 1 product (Limit filter applied in above screenshot where limit<br>is set to 4)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236733633-d345e0d0-1e30-47e3-b1b0-d8f537e1f037.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied-should<br>be more than 1 product (price Low to High filter applied)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236733635-68c868ef-a577-4eb7-bf6e-fd006ed1f7d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied-should<br>be more than 1 product (price High to Low filter applied)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236734503-38a95224-88b5-4b94-9d7f-e09188c93816.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied-should<br>be more than 1 product (category filter applied)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236734644-0a43d1ff-92f0-457c-a4e8-2d8d47d99ad8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Shop page showing both filters and a different sorting applied-should<br>be more than 1 product (name filter applied)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236735175-bb4b6493-853d-4931-9153-337e6dbfb109.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the filter/sort logic from the code - HTML<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236735176-b0e9c3e5-e74b-4ae0-8421-6e8a5cd6a392.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the filter/sort logic from the code (shop.py)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>Users can apply filters to their search queries by using the choose fields<br>on the product search form. The WHERE clause of the SELECT statement, which<br>is used to retrieve products from the database, is modified to include these<br>filters. The form has fields for name and category filtering, where name field<br>supports partial matching and category field demands an exact match.<div>When the form with<br>the selected filters is submitted, a select query is run using the WHERE<br>clause&#39;s conditions. The results of this query are displayed in a table along<br>with a list of the products that fit the provided filters. Each product&#39;s<br>name, description, category, stock, unit price, and visibility status are listed in separate<br>columns of the table.<br></div><div>Users can choose to sort the results by price in<br>either ascending or descending order, with a default page limit of 10 results.<br>This cap can be changed as needed. The reset button is also available<br>to remove the current search results and launch a fresh search. This makes<br>it simple for customers to look up and browse particular products depending on<br>their preferences.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/60">https://github.com/saurabhra009/IS601-004/pull/60</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/shop">https://is601-smr9-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236735942-a17f23a8-e739-48cf-bd0a-806246967831.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page/results  where non-visible products are there too<br>(see item with id =10 and id =14 for non visible product)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div>The "Add to Cart" button is located on the product page, where a<br>consumer can add an item to their shopping basket by going there. This<br>will include the item in their shopping cart and change the total. After<br>that, the customer can either carry on shopping or go to the checkout<br>page.<br></div><div>The customer will see a list of the products in their cart along<br>with the name, quantity, and price of each item on the checkout page.<br>By utilizing the plus and minus buttons or by manually inputting the desired<br>quantity, the client can change the quantity of an item. The "delete" button<br>is located next to each item if the user wants to take it<br>out of their cart.<br></div><div><div>The "Proceed to Payment" button can be clicked by the<br>buyer after they are prepared to finalize their transaction. The payment page will<br>then be displayed, where customers may input their payment details and finish the<br>transaction.</div><div>Overall, the shopping cart function makes it simple for customers to add, delete,<br>and update goods as they purchase, improving the convenience and effectiveness of online<br>shopping.</div></div><div>This SQL statement chooses information from the "IS601_Products" table. The query instructs the<br>database to return all rows from the table along with the values for<br>the "id," "name," "description," "category," "stock," "unit_price," "visibility," and "image" columns only. The<br>database is instructed to only return the first 25 rows of results by<br>the "LIMIT 25" clause at the conclusion of the query.<br></div><div><div>The SELECT statement is<br>used in the query to indicate which columns to return, and the FROM<br>clause is used to specify the table from which to retrieve the data.<br>The query's LIMIT clause is used to restrict the number of rows it<br>returns.</div><div>The first 25 rows of the "IS601_Products" table's result set from this query<br>will include the needed data. Each returned row in the table will have<br>a corresponding row in the result set, each row containing the values for<br>the designated columns.</div></div><div><br></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/61">https://github.com/saurabhra009/IS601-004/pull/61</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/admin/items">https://is601-smr9-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236737259-8fe845a6-176a-47b7-b89a-8158e62b0244.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236737397-4ab9477b-cfee-4485-8a49-0b6478fa6ad6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236737628-df9a3e1b-61c8-4b6f-846e-fe8e7835604a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page (The admin page)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236737775-e2db04ee-38e7-4a9c-9342-8c0f467f49ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit item page of admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236738138-36e87934-c34c-4d94-b6a4-b54797270b8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of admin product list page before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236737775-e2db04ee-38e7-4a9c-9342-8c0f467f49ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Editing a Product on the admin product list page - Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236738678-e77b06b4-1c7a-4ceb-b25d-222fd51bbdf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing success message of updating or editing item by admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236738744-0493625b-bcbc-41eb-bb0c-0b0f3f326184.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of admin product list page after edit (you can see name of<br>&quot;Armani Exchange&quot; is changed to &quot;Armani Exchange after edit , I have updated<br>the name of first watch old name = &quot;Armani Exchange&quot;, New name =<br>&quot;Armani exchange after edit&quot;)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>The form in question is used to update an existing product in a<br>database&#39;s products table, as indicated by the id given in the form request.<br>In order to do this, a SQL Update command must be executed, which<br>changes the product in the database with the newly entered data. A flash<br>message is sent to validate the update and the form data is cleared<br>after a successful form submission. In the event that the query fails for<br>whatever reason, an error message is shown in its place.<div>The Admin user is<br>then redirected back to the Shop page where they may examine the modified<br>product once this process is complete. By selecting the edit button, which opens<br>a form with the most recent information for that product already filled in,<br>the admin also has the ability to make additional changes to the product.<br>This enables simple product adjustment and the subsequent resubmission of the form.<br></div><div>The usage<br>of WTF Forms and Jinja templates, which speed up the construction and rendering<br>of the form, makes it easier to implement this feature. Numerous validators and<br>SQL statements are used to guarantee the effectiveness and accuracy of the updates<br>made to the products table. Overall, using the form and related procedures, the<br>admin can quickly edit or add new products to the database, view the<br>changes on the Shop page, and perform other related tasks.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/62">https://github.com/saurabhra009/IS601-004/pull/62</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/admin/item?id=1">https://is601-smr9-prod.herokuapp.com/admin/item?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236740107-740608eb-90b5-4a51-adf5-eaf0d8252afb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page (When you click on &quot;More Details&quot; button it get directed to<br>that product detail page-Shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236740803-dc0d1fb3-f771-46e7-b335-ee0c1cd7565d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page (When you click on &quot;More Details&quot; button it get directed to<br>that product detail page-Cart Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236740180-26862856-7203-4960-aa31-68a92f28aec0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing product detail page of product after clicking on &quot;More Details&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>Users can examine a detailed summary of a particular product on the Product<br>Details Page. It contains a variety of information, including the name, description, category,<br>stock level, unit cost, and image of the product. An SQL Select statement<br>is used to retrieve the required product data from a database as part<br>of the process flow that creates the page.<div>The WHERE clause of the Select<br>statement uses the product&#39;s unique identifier, the product id, to target the product<br>in question explicitly. The generated information is then sent to a Jinja template,<br>who renders the HTML for the Product Details Page. With the help of<br>the Jinja templating engine, developers may add variables and logic to template files<br>to produce dynamic HTML pages.<br></div><div>The name, description, category, stock, unit pricing, and image<br>of the product are all placeholder variables in this instance&#39;s Jinja template. The<br>Product Details Page always shows the most recent information about the product since<br>these placeholders are changed with the real values retrieved from the database when<br>the template is generated. In general, the process flow for creating the Product<br>Details Page entails pulling the pertinent product information out of the database and<br>using that information to build an HTML template.<br></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/63">https://github.com/saurabhra009/IS601-004/pull/63</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/productdetail?id=3">https://is601-smr9-prod.herokuapp.com/productdetail?id=3</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236741699-06a56593-25df-4ad4-947c-44b2ae669211.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236741870-2265ee0a-d888-4821-85b7-d3919900627f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the error message of adding to cart (i.e., User when not<br>logged in)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236742573-7084bf37-d0d7-4dcc-a1c5-420e0a423ac6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>It is important to use a number of approaches and strategies in order<br>to provide the capability for adding things to a cart and updating the<br>cart on a website. The request.form.get method can be used to acquire the<br>product ID and quantity of the desired item as the first step in<br>this procedure. The function current_user.get_id() can be used to find out the user&#39;s<br>ID.<div>It is feasible to update the cart with this information once the appropriate<br>data has been acquired. SELECT and INSERT statements are two examples of SQL<br>queries that can be used to do this. The INSERT query can be<br>used to add new products to the cart, while the SELECT query can<br>be used to retrieve things that are already in the cart. Through the<br>use of a join command, these queries can be connected to the proper<br>tables, enabling the appropriate data to be added or retrieved based on the<br>product ID and user ID.<br></div><div>A flash message can be displayed to notify the<br>user if any errors are made during this procedure, such as attempting to<br>modify the quantity of an item to a negative value. This makes sure<br>that the cart is correct and current at all times and that the<br>user is aware of any potential problems. Additionally, to maintain the cart&#39;s efficiency<br>and organization, if an item&#39;s amount is set to 0, it can be<br>removed from the cart. In order to assure the accuracy and effectiveness of<br>the cart, several approaches and procedures are used while adding things to the<br>cart and updating the cart on a website.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>A &quot;Add to Cart&quot; button is added to the product page to make<br>the process of adding things to a shopping cart easier. This button causes<br>an HTTP POST request to be made to the server. Users may also<br>add products to their cart directly from the store page by using an<br>INSERT query to add the necessary data, such as the product ID, quantity,<br>unit price, and user ID, to the cart.<div>A new row containing the product_id,<br>quantity, and price of the item being added is added to the cart_items<br>table in order to update the cart in the database. The amount and<br>price of each item in the cart are multiplied and added up to<br>determine the overall cost of the cart.<br></div><div>The user is informed via a flash<br>message if any errors arise during this process. The cart also shows the<br>quantity of things currently in it and their combined cost.<br></div><div>Creating a form, validating<br>and inserting the form data into the database, and updating the database&#39;s cart<br>with the newly added products are all steps in the process of adding<br>things to the cart. The usage of numerous libraries and frameworks, like WTF<br>Forms, Jinja, and SQL commands, facilitates this procedure.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/64">https://github.com/saurabhra009/IS601-004/pull/64</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236744070-c97f7a2a-c76e-42bb-ae1b-0e2744bfc6e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Cart View (where subtotal of each line is added properly,<br>cart total is added properly, link to product detail page of each product<br>is shown)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>The pertinent data, including the product name, quantity, and price, is saved in<br>the cart database when a product is added to a user&#39;s cart. The<br>namespace, or logical grouping of similar variables, is used by this database to<br>determine the total cost of the goods in the cart. The quantity of<br>each commodity is multiplied by its price to arrive at the subtotal.<div>The items<br>in the cart are then displayed on the website using the Jinja template<br>code. The essential data for each product is retrieved and shown in a<br>table format when this code loops over the rows in the cart table.<br>This makes it simple for the user to see the items they have<br>in their shopping cart, along with the quantities and prices that go with<br>them. Overall, the management and presentation of the products in a user&#39;s cart<br>is made possible by the interaction of the cart database and the Jinja<br>template code.<br></div><div>The subtotal for each item in the cart is calculated by dividing<br>the item&#39;s unit price by the item&#39;s quantity. This sum is then added<br>to a running total, which serves as the overall subtotal for the entire<br>cart, after being saved in a variable. A for loop is used to<br>implement this procedure, iterating through the session dictionary, which holds the relevant data<br>about each item in the cart.<br></div><div>Following calculation, the subtotal and total for the<br>cart are shown on the website using Jinja template code. The subtotal and<br>total for each item in the cart are displayed using a for loop<br>in this code, which iterates over the session dictionary. The subtotal and total<br>are shown as a table, with the subtotal and total for every product<br>listed in distinct cells.<br></div><div>Finally, the user has the choice to click the checkout<br>button to get to the checkout page. The user will then be sent<br>to a page where they can finalize their purchase by providing their shipping<br>and payment details. To safeguard the security and privacy of the user&#39;s personal<br>and financial information, the checkout process is made easier by the use of<br>secure servers and encrypted data transmission.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/65">https://github.com/saurabhra009/IS601-004/pull/65</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/cart">https://is601-smr9-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236745264-a5ad4b4b-7397-4280-995b-a08d22c85092.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart before updating the quantity of product name = &quot;Stuhrling Original&quot;<br>( Currently the quantity of &quot;Stuhrling Original&quot; in cart is 3)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236745506-2b6fda20-ebe5-417c-81ac-23d553597f95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart after updating the quantity of product name = &quot;Stuhrling Original&quot;<br>( The quantity of &quot;Stuhrling Original&quot;  after updating cart is 3 and<br>as result of that subtotal of  Stuhrling Original also changed to &quot;400&quot;<br>from &quot;240&quot; and hence  Total price of cart also change to &quot;880&quot;<br>frpm &quot;720&quot;) )<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236746540-a44d7bd5-6a64-43aa-8b8d-d4c00b711820.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart before setting quantity to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236746876-c3b01103-d719-43fc-a850-5e5e6b952284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart when quantity of product &quot;Stuhrling Original&quot; is set to<br>0.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236747253-12458d6a-b308-4476-8304-8db90d87bf17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart after setting quantity of  product &quot;Stuhrling Original&quot; to<br>0. You can see if we are setting the quantity to 0, it<br>is getting deleted from the cart and , a flash message is getting<br>generated. We have updated the quantity for &quot;Stuhrling Original&quot; to 0 and it<br>has been deleted from cart.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236748592-1a5891c4-556d-4235-9987-7e3fdf8c11ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart after setting quantity of  product &quot;Stuhrling Original&quot; to<br>0. After updating the quantity for &quot;Stuhrling Original&quot; to 0 it has been<br>deleted from cart.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236749028-a3c926bc-13cc-4484-95fd-02438eb918fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart before setting quantity to negative<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236749031-25b1c1e4-8201-45b8-b2d6-146f03fc1a9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart when quantity is set to negative. ( When I<br>set the quantity of Movado = -1 in cart it is getting deleted<br>from cart and and flash message is displayed that quantity cannot be less<br>than 0.)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236750454-2d5f2bb0-69bf-425d-bdfb-d070c8b66a95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart after quantity is set to negative. You can see<br>product Movado is not there in cart.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>The unique identity of the product that needs to be changed, also known<br>as the id, must be included in a form request in order to<br>update a product in the database. Using this ID, you may find the<br>appropriate entry in the products table. Structured Query Language (SQL)&#39;s DELETE command is<br>used to remove the product from the table if the form request includes<br>a stock value of 0. The user sees a notification confirming that the<br>product has been taken out of the cart.<div><div>The form&#39;s validators will catch this<br>issue and block submission if a user tries to submit a form with<br>a negative quantity for the stock of a product.</div><div>The user will see a<br>notification reminding them that they need to provide a positive number. The code<br>must be able to handle the case where the user decides to adjust<br>the stock amount to a negative value after the form has already been<br>submitted and the product has already been added to the products database. In<br>this instance, the new quantity is verified using an If-else block. If the<br>value is negative, a warning alerting the user that they are unable to<br>enter a negative quantity and that the stock quantity has not been changed<br>is displayed.</div></div><div>The code will use a SQL Update statement to update the stock<br>quantity in the products table, nevertheless, if the new quantity is positive. A<br>message is provided to confirm the update if the query is successful and<br>the stock quantity is updated. If the query is unsuccessful, a notice alerting<br>the user to the error is presented.<br></div><div><div>The implementation of validators to stop negative<br>quantities from being submitted, as well as an If-else block and SQL Update<br>command to handle updating the stock quantity in the products table if a<br>negative quantity is entered, make up the process flow for handling negative quantities<br>in WTF Forms. This guarantees that the products table appropriately reflects all permitted<br>quantities, which must be positive.</div></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/66">https://github.com/saurabhra009/IS601-004/pull/66</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236751644-8ca972dd-ad25-4601-907c-c3abf0e19582.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart before deleting the item in cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236751648-4f221d30-f305-4fab-9dfb-12bdd4956c21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart after deleting the item in cart. Showing success message<br>deleted item from cart. You can see product Tissot got deleted from cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236751649-96d13095-f472-47aa-be20-af5cf7fb3e6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of cart after deleting, You can see product Tissot is no more<br>in cart. It got deleted from there<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236752448-59775a2b-7b21-469d-9093-012c3ee57e5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart before clearing cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236752449-4deabbdb-480f-4564-8d85-93151e29ece0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart page after clearing cart. You can see the success<br>message of Records deleted successfully. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/236752450-62861bca-1cf7-4764-b29c-3983343962fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of user cart page after clearing cart. You can see there are<br>no items presented in cart.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>The first step in removing a single item from the basket is for<br>the user to click on the &quot;Delete&quot; button next to the item they<br>want to get rid of. As a result, the server receives a request<br>to remove the item from the cart.<div><div>The item will be retrieved from the<br>cart data structure and deleted as soon as the server receives the request.<br>When the item has been successfully removed from the cart, the server will<br>reply to the user and let them know.</div><div>The total cost of the goods<br>still in the cart will be revised after the data structure for the<br>cart is updated to reflect the removal of the item. If the user&#39;s<br>cart is now empty, the item that was deleted was the only one<br>there. The consumer can either proceed to checkout to finish their purchase or<br>keep shopping if there are still items in the cart.</div></div><div>It is crucial to<br>remember that removing an item from the cart requires communication between the user<br>and the server, which is responsible for altering the cart&#39;s data structure and<br>relaying pertinent information to the user.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/67">https://github.com/saurabhra009/IS601-004/pull/67</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div><b>Issue Faced:</b></div><div>We ran into a number of problems that needed to be fixed<br>as we finished this milestone.</div><div>The validation of form data was one of the<br>main problems. The information entered into the form had to be accurate and<br>adhere to certain specifications, such the name field being a string and the<br>stock field being a number. We created a number of validators to check<br>the user-provided data in order to solve this problem.</div><div>We also ran into problems<br>when trying to submit the form. Occasionally, the form wouldn't submit correctly, which<br>caused issues with the database. We had to debug the code in order<br>to find the problem's source, which was frequently improper data entry or a<br>lack of fields.</div><div><br></div><div><b>Learnings:</b></div><div><div>Despite above difficulties, we learned a lot throughout this significant milestone.<br>We learned the importance of form validation and how to use it efficiently.<br>Additionally, we improved our knowledge of how to troubleshoot form submission errors and<br>debug code to find the source of issues.</div><div>In conclusion, this achievement enabled us<br>to have a deeper understanding of forms and their function in data collection<br>and processing in a web application. We succeeded in developing a useful form<br>that can be used to add and modify products in a database as<br>a result of our work.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-smr9-prod.herokuapp.com/login">https://is601-smr9-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/smr9" target="_blank">Grading</a></td></tr></table>