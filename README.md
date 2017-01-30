# WT2017-GradingAnonymization

## Objective :
This project is intended to improve current CS 151 grading system. It will allow graders to grade without knowing students’ names and grade histories.

## What each file do:
#### redactJAVA:
- This python script will redact student names in JAVA files. It will only redact student names in comments.
- Usage: ./redactJAVA <name list file> <original file> <redacted file>
- This script is fully tested locally, but not on the OCCS server.

#### redactREADME:
- This python script will redact student names in README files.
- Usage: ./redactREADME <name list file> <original file> <redacted file>
- This script is fully tested locally, but not on the OCCS server.

#### anonym_pregrade:
- This python script will make a redacted version for each student's submission and grade files. This script calls two other python scripts: redactJAVA, redactREADME. 
- Usage: ./anonym_pregrade
- This script is not tested locally or on the OCCS server. This script need some modification to work with the grader script. Both anonym_pregrade and grader need some minor modification. There are marks in anonym_pregrade to The grader script should execute anonym_pregrade for the pregrade part each time.

## Where are the files:
- Before this project:
```
grades
  	Spring2016
  	Fall2016
      	lab1
      	lab1_backup
      	lab1_grades
	  	lab2
	    	student1.2.2016-XX-XX_XX-XX-XX
	      		cool.java
	      		README1
	      		cool.class
	      		sample.txt
	    	bstudent.2.2016-XX-XX_XX-XX-XX
	      		fun.java
	      		fun.class
	      		readme_b.txt
	  	lab2_backup
	  	lab2_grades
	    	student1
	    	bstudent
```
- After this project:
```
grades
  	Spring2016
  	Fall2016
      	lab1
      	lab1_backup
      	lab1_grades
	  	lab2
	    	student1.2.2016-XX-XX_XX-XX-XX
	      		cool.java
	      		README1
	      		cool.class
	      		sample.txt
	    	bstudent.2.2016-XX-XX_XX-XX-XX
	      		fun.java
	      		fun.class
	      		readme_b.txt
	  	lab2_backup
	  	lab2_grades
	    	student1
	    	bstudent
	Spring2016_anonym
  	Fall2016_anonym
  		name_list
  		lab1
      	lab1_grades
      	lab2
	    	[3]disUhXsdscn8-G.2.2016-XX-XX_XX-XX-XX
	      		cool.java       [redacted copy]
	      		README1         [redacted copy]
	      		cool.class 	    -> grades/Fall2016/lab2/student1.2.2016-XX-XX_XX-XX-XX/cool.class
	      		sample.txt      -> grades/Fall2016/lab2/student1.2.2016-XX-XX_XX-XX-XX/sample.txt
	    	[1]bcsh3r)UcDa!|p.2.2016-XX-XX_XX-XX-XX
	      		fun.java        [redacted copy]
	      		fun.class       -> grades/Fall2016/lab2/bstudent.2.2016-XX-XX_XX-XX-XX/fun.class
	      		readme_b.txt    [redacted copy]
	  	lab2_grades
	    	[3]disUhXsdscn8-G   -> grades/Fall2016/lab2_grades/student1
	    	[1]bcsh3r)UcDa!|p   -> grades/Fall2016/lab2_grades/bstudent
```
- Note: "->" is a symbol for symbolic links. 
- Note: The file "name_list" should contain all student first names, last names, and cs account names.
- Note: "disUhXsdscn8-G" is just an example. It should be a hash name for student1 using sha224. The "[3]" in the front of the string meaning this should be graded by grader 3. This number is randomly generated base on the total number of CS151 graders, which is hard coded in anonym_pregrade and should be changed when needed.
- Note: Since graders should not know who they are grading, graders cannot enter each student's grades on blackboard and gradebook. My solution is to have one grader to enter the grade for each lab after all grading is finished. The selected grader will use "grader report" to see all grades and enter all the grades to blackboard and gradebook.
