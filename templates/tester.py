import numpy as np
import pandas as pd

myData = {'Item': ['NBA Team','Grocery Store','Dining Hall'],
'Favorite':['Boston Celtics','Walmart','JJs'],
'Non-favorite':['LA Lakers','Target','John Jay']}

myDF = pd.DataFrame(myData, columns = ['Item','Favorite','Non-favorite'])
myDF.reset_index(drop=True, inplace=True)
myDF.set_index('Item',inplace = True)


myDF.to_html("df_html.html")

