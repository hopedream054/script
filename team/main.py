import os
import sys
import urllib.request
from intro import FIRST_INTRO

Query = None
while True:
    Menu_num = FIRST_INTRO.printMenu_number()
    Answer = FIRST_INTRO.Movie_name_service(Menu_num)
    if Menu_num == '5':
        break

