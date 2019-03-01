#this is one of the first big projects to try to find emails and phone numbers in a txt file
# phoneAndEmail.py - Finds phone numbers and emails on clipboard
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?          
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}}))?
    )''', re.VERBOSE)
# TODO : everything else lol
