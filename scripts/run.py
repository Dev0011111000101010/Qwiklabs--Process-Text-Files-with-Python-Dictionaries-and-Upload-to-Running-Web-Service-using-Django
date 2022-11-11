#!/usr/bin/env python3

import os
import requests
import json

"""When "#" is used it means "comment"
If "##" is used, then this is a comment that is to ACTION so that the code works on a local OR online server"""

## This folder stores TXT files feedback for the site
## The correct code to use on the combat server to complete the task
## The lines below need to be uncommented and applied when running the qwiklabs task
"""Online"""
feedback_txt_files_folder_path = '/data/feedback'
## The line below was created for local testing without creating a load on the qwiklabs Google server
## The line below should be commented out when running the job online in qwiklabs, while the line above is uncommented
"""Local"""
# feedback_txt_files_folder_path = '/Users/il/PycharmProjects/Qwiklabs--Process-Text-Files-with-Python-Dictionaries-and-Upload-to-Running-Web-Service-using-Djang/test_feedback'

# URL of the server
## Replace <corpweb-external-IP> (35.222.215.76) with corpweb's external IP address.
"""Change me :) """
combat_server_url = 'http://35.222.215.76/feedback/'

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
    print('# QA : The second line shows the converted dictionary')

    for file in txt_files_list:
        absolute_path_2_feedback = feedback_txt_files_folder_path + '/'
        with open(absolute_path_2_feedback + file) as f:
            # Hint on Loop Reading a File Line by Line
            # https://pythonru.com/osnovy/chtenie-iz-fajla-postrochno-v-python
            list_content_of_feedback_files = f.readlines()
            print(list_content_of_feedback_files)
            # Hint: list to dictionary
            # https://careerkarma.com/blog/python-convert-list-to-dictionary/
            list_dictionary_titles = ["title", "name", "date", "feedback"]
            feedback_dictionary = dict(zip(list_dictionary_titles, list_content_of_feedback_files))
            print(feedback_dictionary)
            # post_each_1_feedback_in_json_format_2_server = requests.post(combat_server_url, json=feedback_dictionary)
            print('----------------------')
            print('----------------------')
            print(' # QA: print(json.dumps(feedback_dictionary))')
            print(json.dumps(feedback_dictionary))
            print('----------------------')
            dictionary_double_quotes_formate_transform = json.dumps(feedback_dictionary)
            post_each_1_feedback_in_json_format_2_server_double_quotes = requests.post(combat_server_url, json=dictionary_double_quotes_formate_transform)
            print('----------------------')
            print(' # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)')
            print(post_each_1_feedback_in_json_format_2_server_double_quotes)
            print('----------------------')
            print('')

    print('----------------------')
    print('----------------------')
    print(' # QA: response.status_code')
    print(post_each_1_feedback_in_json_format_2_server_double_quotes.status_code)
    print(' # QA: response.ok')
    print(post_each_1_feedback_in_json_format_2_server_double_quotes.ok)
    print('----------------------')
    print(' # QA: response.request.url')
    print(post_each_1_feedback_in_json_format_2_server_double_quotes.request.url)
    print('----------------------')
    print(' # QA: response.request.body')
    print(post_each_1_feedback_in_json_format_2_server_double_quotes.request.body)
    print('----------------------')
    print('')

# Launching the "txt_2_dictionary_jungo_structure" function into which the "feedback_txt_files_folder_path" path is passed
convert_txt_feedbacks_2_dictionary_jungo_structure = txt_2_dictionary_jungo_structure(feedback_txt_files_folder_path)


# Server console response
"""
student-00-1f0759f0151d@corpweb:~$ ./run.py
----------------------
----------------------
# QA: Result: If everything is correct, it should return a list of TXT feedback files.
['001.txt', '019.txt', '020.txt', '007.txt', '005.txt']
----------------------
----------------------
----------------------
# QA: Result: If everything is correct, it should return a list of TXT feedback files.
# Difference from above: This test is already running from the "txt_2_dictionary_jungo_structure" function
['001.txt', '019.txt', '020.txt', '007.txt', '005.txt']
----------------------
001.txt    # QA : Iterating over each individual feedback file
019.txt    # QA : Iterating over each individual feedback file
020.txt    # QA : Iterating over each individual feedback file
007.txt    # QA : Iterating over each individual feedback file
005.txt    # QA : Iterating over each individual feedback file
----------------------
----------------------
# QA : Iterating over each individual feedback file content
# QA : The second line shows the converted dictionary
['Great Customer Service\n', 'John\n', '2017-12-21\n', 'The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!\n']
{'title': 'Great Customer Service\n', 'name': 'John\n', 'date': '2017-12-21\n', 'feedback': 'The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!\n'}
----------------------
----------------------
 # QA: print(json.dumps(feedback_dictionary))
{"title": "Great Customer Service\n", "name": "John\n", "date": "2017-12-21\n", "feedback": "The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!\n"}
----------------------
----------------------
 # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)
<Response [400]>
----------------------

['Best experience so far\n', 'Katie\n', '2019-12-09\n', "My friend recommended this place and  I decided to give a try. I called them beforehand and made sure they have the models I was looking for. They evenly sent me a bunch of photos and specs of the car I was looking for. One the day I visited, the sales person John helped me with test drive and showed me what I should be aware of when buying a used car. I felt like I learned a lot. They made the process so smooth that I saved a lot of time. It's the best car purchasing experience I had so far!\n"]
{'title': 'Best experience so far\n', 'name': 'Katie\n', 'date': '2019-12-09\n', 'feedback': "My friend recommended this place and  I decided to give a try. I called them beforehand and made sure they have the models I was looking for. They evenly sent me a bunch of photos and specs of the car I was looking for. One the day I visited, the sales person John helped me with test drive and showed me what I should be aware of when buying a used car. I felt like I learned a lot. They made the process so smooth that I saved a lot of time. It's the best car purchasing experience I had so far!\n"}
----------------------
----------------------
 # QA: print(json.dumps(feedback_dictionary))
{"title": "Best experience so far\n", "name": "Katie\n", "date": "2019-12-09\n", "feedback": "My friend recommended this place and  I decided to give a try. I called them beforehand and made sure they have the models I was looking for. They evenly sent me a bunch of photos and specs of the car I was looking for. One the day I visited, the sales person John helped me with test drive and showed me what I should be aware of when buying a used car. I felt like I learned a lot. They made the process so smooth that I saved a lot of time. It's the best car purchasing experience I had so far!\n"}
----------------------
----------------------
 # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)
<Response [400]>
----------------------

['Waste of my time\n', 'Anonymous\n', '2018-09-21\n', "I came in around 6pm and they seemed about to close the store. One of the sales seemed not being patient with me and made me feel like I have to either buy a car or come back later. Of course I didn't buy a car there. Hopefully they can treat every customer with more patience.\n"]
{'title': 'Waste of my time\n', 'name': 'Anonymous\n', 'date': '2018-09-21\n', 'feedback': "I came in around 6pm and they seemed about to close the store. One of the sales seemed not being patient with me and made me feel like I have to either buy a car or come back later. Of course I didn't buy a car there. Hopefully they can treat every customer with more patience.\n"}
----------------------
----------------------
 # QA: print(json.dumps(feedback_dictionary))
{"title": "Waste of my time\n", "name": "Anonymous\n", "date": "2018-09-21\n", "feedback": "I came in around 6pm and they seemed about to close the store. One of the sales seemed not being patient with me and made me feel like I have to either buy a car or come back later. Of course I didn't buy a car there. Hopefully they can treat every customer with more patience.\n"}
----------------------
----------------------
 # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)
<Response [400]>
----------------------

['Good deal for a 2015 RAV4\n', 'Anonymous\n', '2018-04-17\n', 'Called them to look for a second-hand RAV4 and they are very nice and patience to help me find me a few matches then scheduled an appointmet with me. Came in and they had everything ready for me. I was surprised how professional those sales are and they explained and answered all my questions. Ended up buying the car and been using it for more than a month now. Everything looks good!\n']
{'title': 'Good deal for a 2015 RAV4\n', 'name': 'Anonymous\n', 'date': '2018-04-17\n', 'feedback': 'Called them to look for a second-hand RAV4 and they are very nice and patience to help me find me a few matches then scheduled an appointmet with me. Came in and they had everything ready for me. I was surprised how professional those sales are and they explained and answered all my questions. Ended up buying the car and been using it for more than a month now. Everything looks good!\n'}
----------------------
----------------------
 # QA: print(json.dumps(feedback_dictionary))
{"title": "Good deal for a 2015 RAV4\n", "name": "Anonymous\n", "date": "2018-04-17\n", "feedback": "Called them to look for a second-hand RAV4 and they are very nice and patience to help me find me a few matches then scheduled an appointmet with me. Came in and they had everything ready for me. I was surprised how professional those sales are and they explained and answered all my questions. Ended up buying the car and been using it for more than a month now. Everything looks good!\n"}
----------------------
----------------------
 # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)
<Response [400]>
----------------------

['You will find what you want here\n', 'Tom\n', '2019-06-05\n', "I've being look around for a second handed Lexus RX for my family and this store happened to have a few of those. The experience was similar to most car dealers. The one I ended up buying has good condition and low mileage. I am pretty satisfied with the price they offered.\n"]
{'title': 'You will find what you want here\n', 'name': 'Tom\n', 'date': '2019-06-05\n', 'feedback': "I've being look around for a second handed Lexus RX for my family and this store happened to have a few of those. The experience was similar to most car dealers. The one I ended up buying has good condition and low mileage. I am pretty satisfied with the price they offered.\n"}
----------------------
----------------------
 # QA: print(json.dumps(feedback_dictionary))
{"title": "You will find what you want here\n", "name": "Tom\n", "date": "2019-06-05\n", "feedback": "I've being look around for a second handed Lexus RX for my family and this store happened to have a few of those. The experience was similar to most car dealers. The one I ended up buying has good condition and low mileage. I am pretty satisfied with the price they offered.\n"}
----------------------
----------------------
 # QA: print(post_each_1_feedback_in_json_format_2_server_double_quotes)
<Response [400]>
----------------------

----------------------
----------------------
 # QA: response.status_code
400
 # QA: response.ok
False
----------------------
 # QA: response.request.url
http://35.222.215.76/feedback/
----------------------
 # QA: response.request.body
b'"{\\"title\\": \\"You will find what you want here\\\\n\\", \\"name\\": \\"Tom\\\\n\\", \\"date\\": \\"2019-06-05\\\\n\\", \\"feedback\\": \\"I\'ve being look around for a second handed Lexus RX for my family and this store happened to have a few of those. The experience was similar to most car dealers. The one I ended up buying has good condition and low mileage. I am pretty satisfied with the price they offered.\\\\n\\"}"'
----------------------

student-00-1f0759f0151d@corpweb:~$
"""