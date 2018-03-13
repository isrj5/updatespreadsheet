#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:13:57 2018

@author: surajsingh
"""

import gspread
import os
import datetime
import time


from oauth2client.service_account import ServiceAccountCredentials
 
#to find next available row 
def next_available_row(sheet):
    str_list = list(filter(None, sheet.col_values(1)))  # fastest
    return str(len(str_list)+1)

# use creds to create a client to interact with the Google Drive API
def update_spreadsheet(username,SAMRAT_id,test_result):
    scope = ['https://spreadsheets.google.com/feeds']
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATA_JSON = basedir+'/'+'client_secret.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(DATA_JSON, scope)
    
    client = gspread.authorize(creds)
    
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("TESTING REPORT")
    worksheet=sheet.worksheet("INTEGRATION TEST")
    next_row = next_available_row(worksheet)
    
    
    
    count=int(next_row)
    count-=1
    
    
    #insert on the next available row
    date_today=datetime.date.today()
    time_today=time.strftime("%H:%M:%S")
    
    worksheet.update_acell("A{}".format(next_row), count)
    worksheet.update_acell("B{}".format(next_row), date_today)
    worksheet.update_acell("C{}".format(next_row), time_today)
    worksheet.update_acell("D{}".format(next_row), SAMRAT_id)
    worksheet.update_acell("E{}".format(next_row), test_result)
    worksheet.update_acell("G{}".format(next_row), username)


    

    