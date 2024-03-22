import re
import pandas as pd

#excel = pd.read_excel(r"C:\Users\User\Documents\telegram public chanel get messages\data3_2023-10-15.xlsx")
#print(excel)

o = re.search(r"(?<=\:\s)\d+", "PVP: 300$")
print(o.group(0))

var =1