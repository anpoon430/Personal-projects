# Personal-projects

## pwcheck.py 
Is a program that checks whether your password is strong or not. It uses multiple regular expressions to check your password so that it matches the criterion of a strong password 

1. 8 characters in length, including symbols, spaces and alphanumeric characters
2. Atleast an uppercase and lowercase letter
3. Atleast one number

pwcheck.py uses the module tryagain.py to allow the user to continue running the program and checking the strength of their password

## tryagain.py
Is a program that loops to ask if the user wants to re-run a program or not. Since this is such a common requirement for all programs, I have made it into a separate module that can be reused in my other programs

## regexsearch.py
This program searches all text files within a specified folder for a user-supplied regular expression. It then returns all matches for each text file and prints it to the screen.

## scrapedatajobpostings.py
This program scrapes hk.jobsdb.com/hk for job listings under the search term 'data' and experience level 'entry level'. It gathers all the links on each page to each posting, then scrapes each listing for all the relevant information and stores it in a dictionary. Finally, a CSV file containing the title, company name, company information and job posting details (responsibilities and requirements) is outputted.
