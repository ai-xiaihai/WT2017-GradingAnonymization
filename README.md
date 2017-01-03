# WT2017-GradingAnonymization
**Objective :**

I would like to make some tools and/or revise the current grading scripts to make
this grading system better. My eventual product would allow graders to grade without knowing students’ names and grade histories. Due to the limitation of time and knowledge, I will place my focus on the grading system of CSCI 151.

**Plan :**

1. I will make a program to replace students’ names in their source code with something else (possibly XXXXXXXX). The tricky part is that students may work with another student in some lab assignments. I also need to make sure that the program only changes the comments but not the actual code.
2. I will make a program to turn the filenames of students’ submission into unique hashcode. I will create a list of soft links to students’ submission. I also want to mark students’ submission if they are late.
3. I will modify the grading system so graders can see their grading assignments and put in grades but they cannot see students’ names and past grades. This goal involves multiple parts. I will create soft links to students’ grade files. I will also create a program to scan students’ grade files, fetch the grades and put them into a gradebook (maybe a Google sheet). I expect the program to be executed once a day by a cron job if it is actually incorporated into the grading system.

# Part 1: Redaction.
* Input: A list of student names (first, last, f+last); A java file.
* Output: A java file with students’ name redacted.
* Goal: Replace students’ names with XXXXX
* Note: 
  - only replace names in comments (\\, \* … … *\ , @); 
  - for each java file, look for all students’ names;
* Question: 
  - Where this redaction file will be executed?
  - Where do I get list of student names?
  - Which language?
