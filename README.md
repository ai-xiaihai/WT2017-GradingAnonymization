# WT2017-GradingAnonymization

**Objective :**
This project is intended to improve current CS 151 grading system. It will allow graders to grade without knowing students’ names and grade histories.

**What each file do:**
*redactJAVA:
-This python script will redact student names in JAVA files. It will only redact student names in comments.
-Usage: ./redactJAVA <name list file> <original file> <redacted file>
-This script is fully tested locally, but not on the OCCS server.

*redactREADME:
-This python script will redact student names in README files.
-Usage: ./redactREADME <name list file> <original file> <redacted file>
-This script is fully tested locally, but not on the OCCS server.

*anonym_pregrade
-This python script will make a redacted version for each student's submission and grade files. This script calls two other python scripts: redactJAVA, redactREADME. 
-Usage: ./anonym_pregrade
-This script is not tested locally or on the OCCS server. This script need some modification to work with the grader script. Both anonym_pregrade and grader need some minor modification. The grader script should execute anonym_pregrade for the pregrade part.