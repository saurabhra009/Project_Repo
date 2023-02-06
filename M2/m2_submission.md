<table><tr><td> <em>Assignment: </em> M2 Python-HW</td></tr>
<tr><td> <em>Student: </em> Saurabh Rai (smr9)</td></tr>
<tr><td> <em>Generated: </em> 2/6/2023 1:53:40 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m2-python-hw/grade/smr9" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you have the dev/prod branches created before starting this assignment.</p><p>Pre-req Steps if not done so yet:</p><p><ol><li>git checkout main</li><li>git checkout -b dev</li><li>git push origin dev</li><li>git checkout -b prod</li><li>git push origin prod</li></ol><div>This will ensure you have a dev and prod branch on github.</div></p><p>Setup steps:</p><ol><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M2-Python-HW</code></li></ol><p>You'll have 3 problems to save for this assignment.</p><p>Each problem you're given a template&nbsp;<strong>Do not edit anything in the template except where the comments tell you to</strong>.</p><p>The templates are done in such a way to make it easier to capture the output in a screenshot (if it's still not able to fit well, you can zoom out in your browser).</p><p>You'll copy each template into their own separate .py files, immediately git add, git commit these files (you can do it together) so we can capture the difference/changes between the templates and your additions. This part is required for full credit.</p><p>HW steps:</p><ol><li>Open your IDE at the root of your repository folder</li><li>In your IDE create a new folder/directory called M2</li><li>Create 3 new files in this new M2 folder (problem1.py, problem2.py, problem3.py)</li><li>Paste each template into their respective files</li><li><code>git add .</code></li><li><code>git commit -m "adding template baselines</code></li><li>Do the related work (you may do steps 8 and 9 as often as needed or you can do it all at once at the end)</li><li><code>git add .</code></li><li><code>git commit -m "completed hw"</code></li><li>When you're done push the branch<ol><li><code>git push origin M2-Python-HW</code></li></ol></li><li>Create the Pull Request with&nbsp;<strong>dev</strong>&nbsp;as base and&nbsp;<strong>M2-Python-HW</strong>&nbsp;as compare</li><li>Create a new file in the M2 folder in your IDE called m2_submission.md</li><li>Fill out the below deliverable items, save the submission, and copy to markdown<ol><li>For this assignment you may get screenshots from your IDE output or terminal/console output</li></ol></li><li>Paste the markdown into the m2_submission.md</li><li>add/commit/push the md file<ol><li><code>git add m2_submission.md</code></li><li><code>git commit -m "adding submission file"</code></li><li><code>git push origin M2-Python-HW</code></li></ol></li><li>Merge the pull request from step 11</li><li>On your local machine sync the changes<ol><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li></ol></li><li>Make a pull request from&nbsp;<strong>prod</strong>&nbsp;as base and&nbsp;<strong>dev</strong>&nbsp;as compare and immediately merge it</li><li>Submit the link to the m2_submission.md file from the prod branch to Canvas</li></ol><p><strong>Template Files</strong>&nbsp;You can find all 3 template files in this gist:&nbsp;<a href="https://gist.github.com/MattToegel/3c55ca7bb631ff6f492bf6f1ad27270e">https://gist.github.com/MattToegel/3c55ca7bb631ff6f492bf6f1ad27270e</a></p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Problem 1 - Only output Odd values of the Array under "Odds output" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 1 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/216896043-f6b6e80b-014a-45fb-8bb8-35aaa2444a25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem1.py_Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/216896068-d59d6de6-f03c-4145-9e38-9aed2cbb615e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem1.py_Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>Odds value in the array is calculated by using the remainder operator i.e<br>we use the % operator which calculates the remainder. If any integer mod<br>of 2 is equal to zero then the given number is even otherwise<br>the number is odd.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Problem 2 - Only output the sum/total of the list values by assigning it to the 'total' variable (the number must end in 2 decimal places, if it ends in 1 it must have a 0 at the end) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 2 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/216896082-921c552f-3177-482e-bced-f4e79ca45a1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem2.py_Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/216896098-64742fd6-420b-4ba1-bc0d-c2a672ab0a8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem2.py_Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>We have taken one variable and assigned the vale zero to it. After<br>that we iterated through each element in array and added each number to<br>the total. To keep the total up to two decimal places I have<br>used the round(total<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Problem 3 - Output the given values as positive under the "Positive Output" message (the data otherwise shouldn't change) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 3 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/216899824-85176916-47bf-48e6-9b30-7cbc5ec2c2be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem3.py_Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/116526268/216899839-4513924f-374b-48b4-8b9f-d5f3967cb007.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem3.py_Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>We have used abs function to convert negative number to positive number. We<br>have used to type to check the datatype of input and used int(str<br>data) to convert the string to integer. Also got familiar with the array<br>in python and how data in array is iterated and handled.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc Items </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Pull Request URL for M2-Python-HW to dev</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/saurabhra009/IS601-004/pull/2">https://github.com/saurabhra009/IS601-004/pull/2</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Talk about what you learned, any issues you had, how you resolve them</td></tr>
<tr><td> <em>Response:</em> <p>Learned basic of python by completing this HW. Learned different type of datatypes<br>in python and how they are handled in python.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m2-python-hw/grade/smr9" target="_blank">Grading</a></td></tr></table>