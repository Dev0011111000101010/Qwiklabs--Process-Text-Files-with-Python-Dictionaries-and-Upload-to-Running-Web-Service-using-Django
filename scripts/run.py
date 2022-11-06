#!/usr/bin/env python3

import os
import requests


# This folder stores TXT files feedback for the site
feedback_txt_files_folder_path = '/data/feedback'

# Get the list of all files and directories
# in the 'feedback_txt_files_folder_path' directory
print('----------------------')
print('----------------------')
print('#QA: Result: If everything is correct, it should return a list of TXT feedback files.')
print(os.listdir(feedback_txt_files_folder_path))
print('----------------------')



