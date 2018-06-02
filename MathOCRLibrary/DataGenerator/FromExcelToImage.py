#import win32api
#e_msg = win32api.FormatMessage (-2147024894)
#print (e_msg)
#print (e_msg.decode ('CP1251'))
from win32com.client import Dispatch
xl = Dispatch ("Excel.Application")
print ("Paejo")
for i in range (5):
    print (i)
