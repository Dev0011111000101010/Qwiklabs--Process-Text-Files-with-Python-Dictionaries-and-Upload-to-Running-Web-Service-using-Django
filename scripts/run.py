#!/usr/bin/env python3

import os
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
print('#QA: Result: If everything is correct, it should return a list of TXT feedback files.')
print(os.listdir(feedback_txt_files_folder_path))
print('----------------------')



