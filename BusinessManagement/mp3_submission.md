<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Saurabh Rai (smr9)</td></tr>
<tr><td> <em>Generated: </em> 5/1/2023 10:37:13 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/smr9" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380073-6354e3cb-3cb0-43bd-ae6c-e512b2d8bac4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-mt85 updated to my UCID i.e. DIAR-smr9 and bought to you by message<br>updated with my  firstname, ucid, and IS601 section<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380415-46d46c0f-a7c1-4720-bf99-5a05f7e7ca0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference added for company search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380415-46d46c0f-a7c1-4720-bf99-5a05f7e7ca0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference added for company add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380415-46d46c0f-a7c1-4720-bf99-5a05f7e7ca0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference added for employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380415-46d46c0f-a7c1-4720-bf99-5a05f7e7ca0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference added for employee add<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380480-ae19a9e8-63de-4c24-9553-9c21184851a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant url_for reference added for admin import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380535-99095627-088e-4ba2-ab8b-72a83a16cad2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB table from VS code showing both IS601_MP3_Companies and  IS601_MP3_Employees  table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380850-5996dabe-ceae-4778-bce1-dba486a3f1aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of /import route code part-1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380851-83336c8d-bdca-47dc-ac5c-fe4528f3c9c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of /import route code part-2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235380966-10816888-9c4d-4ff0-8e35-5685ce71cb35.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code checking whether the file is .csv or not otherwise rejecting with a<br>flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235381074-62a41ed2-2e44-4a13-9bf4-ea0dddaa1e3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code checking CSV file should be read from the provided stream as a<br>dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235381074-62a41ed2-2e44-4a13-9bf4-ea0dddaa1e3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code reading file and extracted employee and company data is appended as dictionary<br>to employee list and company list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235381579-94e473f4-41b1-4694-bcf2-6dc7cc257b7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of processed records showing in flash message that how many record were<br>processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235381935-6f2b42ea-d207-44f9-95db-7cf9acb96a2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code if nothing was loaded  and flash message that the particular list<br>wasn&#39;t loaded or was empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235562471-4e85e615-9b38-44cf-b478-fd6f8f9128e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website showing proper success message while uploading csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235562471-4e85e615-9b38-44cf-b478-fd6f8f9128e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website showing proper count message of 1000 data inserted successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235562468-403bc8f1-862a-494b-a26b-240c05db1433.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website showing invalid file error message when the file is not<br>a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235562470-c0c07d4e-4bb1-419d-af63-0fe755d3b09c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website showing error message when the form was submitted without a<br>file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235563000-4a6857fe-18da-4aed-808f-2bae663b93bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database when some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235563001-fa5887fb-3b2b-47af-8c2f-ef2337e7cb35.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database when some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382190-31fc9471-8f38-44e2-845c-64af5e3de4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382190-31fc9471-8f38-44e2-845c-64af5e3de4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing retrieving first_name, last_name, company (id), email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382190-31fc9471-8f38-44e2-845c-64af5e3de4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing first_name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382190-31fc9471-8f38-44e2-845c-64af5e3de4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing  last_name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382190-31fc9471-8f38-44e2-845c-64af5e3de4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing company doesn&#39;t require a flash and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382190-31fc9471-8f38-44e2-845c-64af5e3de4f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing email is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382530-8847316f-53dd-4531-a4a0-62a675f8fa5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> code showing INSERT query should be visible along with the data being<br>passed in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382530-8847316f-53dd-4531-a4a0-62a675f8fa5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing Except block should have a user-friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382950-9a6501b0-327a-4db8-83d9-a179bfce742d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website screenshot showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235383032-8366a371-b161-4ae6-9423-099fb61d52b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing success message of employee record created<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382719-6af629bd-62e1-478f-8d3e-d3406bfc4b94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First_name error message screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382722-fb6ea256-6550-4dcd-b4dd-c88cceedd56e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name error message screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382723-3af95373-994b-4c5e-8855-39c179df0414.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> email error message screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235382866-b766a65b-d492-4395-a720-c31103fb38f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if submitted without filling<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235383488-1506022a-03c1-4db4-bb0a-387c7cb61d0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing new employee record added in database which include valid data shown<br>previously. I have created new employee data of Saurabh Rai. Check employee data<br>with id=29 which is at last position in table  <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389201-eb4395b6-bf1a-4a1b-9191-80fda5edb95e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /search route of employee -Part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389203-43dd07e0-1433-4200-af7b-ce4b845a27f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /search route of employee -Part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389339-8684d042-fc64-4093-bddb-f2b50dbb0ab3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing Select query to retrive data i.e.  to pull employ id,<br>first_name, last_name, email, company_id, company_name via a LEFT JOIN<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389444-43bbcdd4-9260-40c4-99b0-1a5ad1c57c6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which is Checking requested args for fn, ln, email, company, column, order,<br>limit (exact naming is required)  <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389596-94382e90-2e8a-418c-b673-69dc1836e02a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Appending  filter for First_name, last_name, email, company_id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389845-5f5bcb8a-a296-41c7-b511-09ca721bbb88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to append sorting append sorting if column and order are provided and<br>within the allowed columns and order options (asc, desc) allowed_columns = [&quot;first_name&quot;, &quot;last_name&quot;,<br>&quot;email&quot;, &quot;company_name&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389845-5f5bcb8a-a296-41c7-b511-09ca721bbb88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check append limit (default 10) or limit greater than or equal<br>to 1 and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235389845-5f5bcb8a-a296-41c7-b511-09ca721bbb88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code that provide a proper error message if limit isn&#39;t a number or<br>if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235390160-79d66ad9-5ae6-4f6f-aa03-d738d0e9b917.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code where except block should have a user friendly message flashed and a<br>print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235391390-b5551a28-8dae-42b8-a958-815067b3b53f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235391392-16e8f899-df7e-492d-ae20-c66739ce35e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235391393-844eea1d-8b42-49a2-8c8c-b27aaf5ffd60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235391394-02e1df38-c44b-4aef-adca-7a06fd24c431.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235391395-800c5bcb-b044-48c0-a25f-484edbd5420b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing result for one asc filter when first_name as column was selected<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235391396-9a752ff7-ee51-465b-85dd-60e9a274d99d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing result for one dsc filter when last_name as column was selected<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235393694-fcdfddef-2604-4531-86a3-e85038def45d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /edit route of employee - Part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235566696-98b3d94a-1740-49df-baed-920c4d9dc333.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /edit route of employee - Part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235393774-3984e6ef-f059-413b-896f-5129b8ccb5a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code  to retrieve id (from request args) first_name, last_name, company<br>(id), email from form.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394158-0236c9a2-59d7-420c-8351-069f0cb20bdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code where  missing id is handled with a flash message<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394336-14a9a806-35cd-4cff-8164-7b15ed386d2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check first_name is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394336-14a9a806-35cd-4cff-8164-7b15ed386d2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check last_name is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394336-14a9a806-35cd-4cff-8164-7b15ed386d2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which shows company doesn&#39;t require a flash and may be empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394336-14a9a806-35cd-4cff-8164-7b15ed386d2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check email is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394642-d35a3713-d6c9-4221-a38d-7896a9a0a4f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code when update query is executed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394787-bf27296d-2fb5-4759-ba90-d4c4b6afedf5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Except blocks (two) should have a user friendly message flashed and<br>a print() of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394964-dc58b950-a36d-43db-bbd5-9a54ed7224a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code when select query is executed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235394964-dc58b950-a36d-43db-bbd5-9a54ed7224a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code when Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235395328-752be468-293b-4ec9-9b27-331bbeb57139.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of employee data of Saurabh Rai before data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235395674-896c7829-0bf0-4478-9a87-4d3c80b3d47f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of employee data after edit of eomployee_id =29 where I have changed<br>the first name of employee from Saurabh to Manoj. You can see before<br>edit first name was Saurabh and after edit it is Manoj<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235396064-a795ef3b-8bf4-41c6-9b47-94a1646ccc21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website while  editing employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235396062-d0dc4c47-300f-4d00-851d-8a466d7d141f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website showing success message of update employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235395484-2b677ebc-6c3f-4a48-a5e4-4bd354fd92de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235395676-0c3274b9-06eb-4514-b435-d5019132c068.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of DB after edit where I have changed the first name of<br>Saurabh to Manoj. You can see before edit first name was Saurabh and<br>after edit it is Manoj<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235528796-12522de7-8318-41ab-bbe4-8202fe8c139a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /add route of company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536518-251c9226-50d7-4ad1-addf-d9edb2e7ab24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing name is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536518-251c9226-50d7-4ad1-addf-d9edb2e7ab24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing address is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536518-251c9226-50d7-4ad1-addf-d9edb2e7ab24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing city is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536518-251c9226-50d7-4ad1-addf-d9edb2e7ab24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing state is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536518-251c9226-50d7-4ad1-addf-d9edb2e7ab24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing country is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235530023-dfc2e5a3-15e5-47ea-9d16-6164e4a97bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>geography.py  code showing state should be validated against pycountry package<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235530023-dfc2e5a3-15e5-47ea-9d16-6164e4a97bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>geography.py  code showing country should be validated against pycountry package<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536518-251c9226-50d7-4ad1-addf-d9edb2e7ab24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing ZipCode is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235530586-961557cb-7a9e-4a37-9c4e-b9d30dde2e44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing INSERT query being executed should be visible along with the data<br>being inserted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235530586-961557cb-7a9e-4a37-9c4e-b9d30dde2e44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing except block and having user friendly message for error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536762-8fe2647f-0cdb-414a-86a2-f75ada0cc783.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536766-3aec30d0-dcdd-421c-b95b-bb13219391ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing success message of &quot;Added Company successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536769-a79623eb-3047-47b3-b43c-468fafbf6907.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing Company Name required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536770-02c86b91-c85b-45b8-9758-540749be9611.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing address required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536773-bbe56311-cf3e-4253-a1eb-78251f0fdf76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing city required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536779-251ae30a-4dc0-4a5a-996d-f8a64e33c1c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing zip code is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536782-d4fea477-a5b3-49b8-835c-1fb61a19c778.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing country field is missing or required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235536783-1757f50a-2e88-4dcc-8cda-c54dada256bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Screenshot showing state field missing or required<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235537819-03dd5a95-188b-48c2-b2b5-781afe1c1b72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot sowing valid company data added shown previously in website screenshot with company<br>name  = NJIT and id =29 located at last of table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538159-f95bc2a5-18b4-426f-ac56-c687b6132006.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /search route of company - Part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538163-21987b65-29e8-4921-9695-0e44b8b9d51f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /search route of company - Part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538698-0d549d1a-68e4-4023-af00-c7a802299798.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which execute SELECT query which fetch id, name, address, city, country, state,<br>zip, website, employee count (as employee) for the company (likely a sub-query is<br>needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538699-d670227f-cc61-491c-a4fd-6b30dfcaacf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538701-9d5a960e-d456-40ca-aa48-52b5ba89c235.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which append a LIKE filter for name if provided;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538701-9d5a960e-d456-40ca-aa48-52b5ba89c235.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which append an equality filter for country if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538701-9d5a960e-d456-40ca-aa48-52b5ba89c235.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which append an equality filter for state if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538704-291be1a6-529a-4915-9924-cbd54b589b55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for append sorting if column and order are provided and within the<br>allows columsn and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538704-291be1a6-529a-4915-9924-cbd54b589b55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code that append limit (default 10) or limit greater than or equal to<br>1 and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538704-291be1a6-529a-4915-9924-cbd54b589b55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which provide a proper error message if limit isn&#39;t a number or<br>if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235538705-75f6dd1e-303a-4ef5-ae5b-97fc33753c9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code which check Except block should have a user friendly message flashed and<br>a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235540462-2f365041-01a2-494f-92bb-144d418d29eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website screenshot showing results with company name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235540470-5f43c593-c9d4-410e-a08c-410f2de5c33f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website screenshot showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235540472-0a0c65ad-f04e-4374-8ddb-3ae15e5b2b12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website screenshot showing with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235540473-cc793d14-e41f-4158-b7a2-5ec94b2c14e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website screenshot showing result for one asc filter when company name as column<br>is selected<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235540474-aec123e5-b895-44fc-92dc-525fa9d67056.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website screenshot showing result for one desc when state as column is selected<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541116-9c2ed2ab-d83e-4ae7-a227-c89f2d25c2f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /edit route of company - Part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541123-8d800b13-8497-46fc-80b7-11665cbdeeaf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshots of code for /edit route of company - Part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541284-f3981614-938c-42a7-a53c-fab28332a0d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing name is required and shows flash proper error message if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541284-f3981614-938c-42a7-a53c-fab28332a0d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing address is required and shows flash proper error message if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541284-f3981614-938c-42a7-a53c-fab28332a0d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing city is required and shows flash proper error message if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541284-f3981614-938c-42a7-a53c-fab28332a0d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing state is required and shows  error message if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235541284-f3981614-938c-42a7-a53c-fab28332a0d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing country is required and shows error message if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235530023-dfc2e5a3-15e5-47ea-9d16-6164e4a97bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing state should be validated against pycountry package<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235530023-dfc2e5a3-15e5-47ea-9d16-6164e4a97bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing country should be validated against pycountry package<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235542541-0f552fdc-0855-4ee5-8cca-c685e2d50d8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing update query executed with passed in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235542745-18f36b71-adc4-4aad-982b-d4c2cbb54a4d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing for Except blocks (two) which have a user friendly message flashed<br>and a print() of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235543154-e77802b9-eb0a-41e9-8474-4655cd1359b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing select query being executed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235543323-fa6e8b23-5017-4055-82a4-ea0c45538544.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing company data passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235557752-b943ecbf-58fb-49b6-ae53-91b8bc8fae3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235557753-c0fb1bb3-f8e9-44b3-9cd6-8488709495de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website data after edit where I have changed address and city<br>of company NJIT. Before edit address was Newark. After edit new address is<br>Martin Luther  KIng. Similarly before edit city was New Jersey. After edit<br>city is Newark<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558135-1fda7643-2468-42f1-a9f4-5975ff4fb455.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website while updating company NJIT details<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558136-f4740e6e-1df9-4233-a8dc-55b4083f04e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website showing company details updated successfully.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558370-97b6491b-9288-4db2-8075-a926f5323add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558373-d8c12864-45ea-4386-90c1-ba75f3834589.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database after edit  where I have changed address and city<br>of company NJIT. Before edit address was Newark. After edit new address is<br>Martin Luther  KIng. Similarly before edit city was New Jersey. After edit<br>city is Newark<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558829-aa42e913-39a9-466d-8366-9bb5ab1eda8a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /delete route of employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558993-0c9c1118-65c6-4aed-a8bd-bcae77137ba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing to Delete employee by id, if missing showing flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558993-0c9c1118-65c6-4aed-a8bd-bcae77137ba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing Redirect to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558993-0c9c1118-65c6-4aed-a8bd-bcae77137ba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showingAll request args (minus id) are being passed to the redirect route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558993-0c9c1118-65c6-4aed-a8bd-bcae77137ba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing success message being flashed if process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235559502-f4471848-3aa1-4a8b-b002-07f98b674af6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website before deleting employee data of &quot;Manoj Rai&quot;. You can see<br>&quot;Manoj Rai&quot; employee data at the end with id=29<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235559534-08937f48-7c44-4414-86dd-c8a034853643.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website after deleting employee data of &quot;Manoj Rai&quot;. You can see<br>employee data of &quot;Manoj Rai&quot; is not there in website search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235559953-bc7ae548-f47d-446d-9d28-a83d793093b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Database before deleting employee data of &quot;Manoj Rai&quot;. You can see<br>&quot;Manoj Rai&quot; employee data at the end with id=29<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235559954-c8a75a92-3261-4201-aafa-3566c741eac3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database after deleting employee data of &quot;Manoj Rai&quot;. You can see<br>employee data of &quot;Manoj Rai&quot; is not there in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235558678-24680531-c826-4be2-8097-7032e838040b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for /delete route of company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235560226-82c883b6-f11f-4dd9-9594-c9182a175a50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing Delete company by id, if missing showing flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235560226-82c883b6-f11f-4dd9-9594-c9182a175a50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing redirect to company search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235560226-82c883b6-f11f-4dd9-9594-c9182a175a50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing all request args (minus id) are passed to the redirect route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235560226-82c883b6-f11f-4dd9-9594-c9182a175a50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing success message being flashed if process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235561618-6c382bf7-02b2-460d-8899-2601a6c70f1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website before deleting company data &#39;TCS&#39; was deleted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235561621-2ac11700-246e-41a2-b635-b761fb607672.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of website after deleting company data with company name = &#39;TCS&#39;. You<br>can see company data TCS is not there at the end<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235561996-de2a4137-e817-4060-aa9c-785fe917aa15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database before deleting company data &#39;TCS&#39; was deleted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235561998-b7cacbc0-8289-4f6e-a66f-4c3da82c2746.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of database after deleting company data with company name = &#39;TCS&#39;. You<br>can see company data TCS is not there in the database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/235565911-197a7a94-72c6-425b-998e-9b3ab28b5ed7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of all test case passed by running pytest -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p><b>Learnings:</b><div><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">In this assignment, we have<br>studied about the integration of Python, SQL, Jinja,&nbsp;<span style="font-size: 12pt;">flask and HTML to<br>create a website, where we are uploading data from&nbsp;</span><span style="font-size: 12pt;">a CSV and,<br>using it to perform few operations like adding, editing, deleting&nbsp;</span><span style="font-size: 12pt;">etc. We<br>have also used flash messages to give a user friendly response&nbsp;</span><span style="font-size: 12pt;">to<br>the end user in case of any errors. This has a real</span></p>&lt;p class=&quot;MsoNormal&quot;<br>style=&quot;margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;&quot;&gt;&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family:<br>Calibri, sans-serif;">world implication and, we use these kind of websites on a day<br>to<span style="font-size: 12pt;">day basis, so knowing the back-end process it is extremely useful.</span></p>&lt;p<br>class=&quot;MsoNormal&quot; style=&quot;margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;&quot;&gt;&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt;<br>font-family: Calibri, sans-serif;">&lt;o:p&gt;&nbsp;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">In particular,&nbsp;<span style="font-size:<br>12pt;">we have used HTML pages to create a layout for our website then,&nbsp;</span>&lt;span<br>style=&quot;font-size: 12pt;&quot;&gt;we have used SQL using Oracle DB to storing the data by<br>creating&nbsp;</span><span style="font-size: 12pt;">two tables; one employees and another for company data, moreover we<br>have&nbsp;</span><span style="font-size: 12pt;">also used python for our back-end operations and, for showing flash<br>messages.</span></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 12pt;"><br></span></p><p class="MsoNormal" style="margin:<br>0in; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 12pt;"><b>Issue Faced:</b></span></p><p class="MsoNormal" style="margin: 0in; font-size:<br>12pt; font-family: Calibri, sans-serif;">Few issues&nbsp;<span style="font-size: 12pt;">which I have faced while implementing this<br>project is listed below along with&nbsp;</span><span style="font-size: 12pt;">the resolution to it,</span></p><p class="MsoNormal" style="margin:<br>0in; font-size: 12pt; font-family: Calibri, sans-serif;">&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri,<br>sans-serif;">- Faced issues in running the test cases due to&nbsp;<span style="font-size: 12pt;">different column<br>names, later resolved it by keeping the same column names.</span></p><p class="MsoNormal" style="margin: 0in;<br>font-size: 12pt; font-family: Calibri, sans-serif;">&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">-<br>Faced&nbsp;<span style="font-size: 12pt;">issues in extracting the data exactly using the left join, later<br>resolved it&nbsp;</span><span style="font-size: 12pt;">updating the query. (Syntax error initially)</span></p><p class="MsoNormal" style="margin: 0in; font-size:<br>12pt; font-family: Calibri, sans-serif;">&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">- Few<br>minor issues like, Test cases were&nbsp;<span style="font-size: 12pt;">not getting detected automatically, so added<br>the folder to workspace and configured test&nbsp;</span><span style="font-size: 12pt;">cases manually.</span></p><p class="MsoNormal" style="margin: 0in;<br>font-size: 12pt; font-family: Calibri, sans-serif;">&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">-<br>DB table hasn&#39;t got created by running the DB file, so<span style="font-size: 12pt;">I<br>ran both the table queries manually to resolve this issue after activating</span></p>&lt;p class=&quot;MsoNormal&quot;<br>style=&quot;margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;&quot;&gt;&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family:<br>Calibri, sans-serif;">the connection.&lt;o:p&gt;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;">- Faced issue<br>when my file was working locally but not after deploying on heroku app<br>but later got to know that I did not setup the config var<br>in heroku where we have to link or set our DB_URL and secret_key</p>&lt;p<br>class=&quot;MsoNormal&quot; style=&quot;margin: 0in; font-size: 12pt; font-family: Calibri, sans-serif;&quot;&gt;&lt;o:p&gt;&nbsp;</o:p></p><p class="MsoNormal" style="margin: 0in; font-size: 12pt;<br>font-family: Calibri, sans-serif;">&lt;o:p&gt;</o:p></p></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/smr9" target="_blank">Grading</a></td></tr></table>