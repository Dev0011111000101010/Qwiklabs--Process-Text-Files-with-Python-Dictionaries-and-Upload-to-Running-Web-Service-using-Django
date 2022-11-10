#!/usr/bin/env python3

import os
from os import system
import requests


## This folder stores TXT files feedback for the site
## The correct code to use on the combat server to complete the task
## The lines below need to be uncommented and applied when running the qwiklabs task
# feedback_txt_files_folder_path = '/data/feedback'
## The line below was created for local testing without creating a load on the qwiklabs Google server
## The line below should be commented out when running the job online in qwiklabs, while the line above is uncommented
feedback_txt_files_folder_path = '/Users/il/PycharmProjects/Qwiklabs--Process-Text-Files-with-Python-Dictionaries-and-Upload-to-Running-Web-Service-using-Djang/test_feedback'

# Get the list of all files and directories
# in the 'feedback_txt_files_folder_path' directory
print('----------------------')
print('----------------------')
print('# QA: Result: If everything is correct, it should return a list of TXT feedback files.')
print(os.listdir(feedback_txt_files_folder_path))
print('----------------------')

def txt_2_dictionary_jungo_structure(feedback_txt_files_folder_path):
    """1. Reading the contents of TXT files in a folder 'feedback_txt_files_folder_path'
       2. Convert content to dictionary using the correct names to upload to the site correctly"""

    # Get the list of all files and directories
    # in the 'feedback_txt_files_folder_path' directory
    print('----------------------')
    print('----------------------')
    print('# QA: Result: If everything is correct, it should return a list of TXT feedback files.')
    print('# Difference from above: This test is already running from the "txt_2_dictionary_jungo_structure" function')
    print(os.listdir(feedback_txt_files_folder_path))
    print('----------------------')

    # Creating a variable for a list of TXT files
    txt_files_list = os.listdir(feedback_txt_files_folder_path)
    # QA: Iterating over each individual feedback file
    for file in txt_files_list:
        print(file + '    # QA : Iterating over each individual feedback file')

    print('----------------------')
    print('----------------------')
    print('# QA : Iterating over each individual feedback file content')

    for file in txt_files_list:
        absolute_path_2_feedback = feedback_txt_files_folder_path + '/'
        with open(absolute_path_2_feedback + file) as f:
            # Hint on Loop Reading a File Line by Line
            # https://pythonru.com/osnovy/chtenie-iz-fajla-postrochno-v-python
            list_content_of_feedback_files = f.readlines()
            print(list_content_of_feedback_files)
            # Hint: list to dictionary
            # https://careerkarma.com/blog/python-convert-list-to-dictionary/
            list_dictionary_titles = ['title', 'name', 'date', 'feedback']
            feedback_dictionary = dict(zip(list_dictionary_titles, list_content_of_feedback_files))
            print(feedback_dictionary)


# Launching the "txt_2_dictionary_jungo_structure" function into which the "feedback_txt_files_folder_path" path is passed
convert_txt_feedbacks_2_dictionary_jungo_structure = txt_2_dictionary_jungo_structure(feedback_txt_files_folder_path)


