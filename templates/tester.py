import pandas as pd

myData = {'Item': ['NBA Team','Grocery Store','Dining Hall'],
'Favorite':['Boston Celtics','Walmart','JJs'],
'Non-favorite':['LA Lakers','Target','John Jay']}

myDF = pd.DataFrame(myData, columns = ['Item','Favorite','Non-favorite'])
myDF.reset_index(drop=True, inplace=True)
myDF.set_index('Item',inplace = True)


myDF.to_html("df_html.html")

mySchedule = {'Class': ['Symbolic Logic','Strategy Formulation',
                        'Game Theory', '1006'],
'Meeting Day':['M/W','Th','T/Th','T/Th'],
'Professor': ['Tamar Lando','Stephan Meier','Nima Haghpanah','Tim Paine']}
myScheduleDF = pd.DataFrame(mySchedule, columns = ['Class','Meeting Day',
                                                  'Professor'])
myScheduleDF.reset_index(drop=True, inplace=True)
myScheduleDF.set_index('Class',inplace = True)

myScheduleDF.to_html("class_html.html")
