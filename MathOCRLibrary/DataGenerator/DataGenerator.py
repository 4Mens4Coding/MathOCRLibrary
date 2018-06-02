import os
from xlwt import Workbook, easyxf
from traceback import format_exc

directory = os.path.dirname (os.path.abspath (__file__))

def getListFromFile (fileName):
    with open (os.path.join (directory, fileName), "r") as f:
        return [line for line in f.readlines ()]
            

def printSymbolsToExcel (sheet, fontType = ""):
    for i in range (0, len (symbolList)):
        sheet.col (i).width_mismatch = True
        sheet.col (i).width = 256 * 16

    for i in range (0, len (fontList)):
        sheet.row (i).height_mismatch = True
        sheet.row (i).height = 256 * 7

    # Fill all excel with regular font symbols
    line = 0
    for font in fontList:
        formatLine = ", ".join (["font: name " + font, fontType, "height 1200; align: horiz center", "vert center"])
        fontStyle = easyxf (formatLine)
        col = 0
        for symb in symbolList:
            sheet.write (line, col, symb, fontStyle)
            col += 1
        line += 1 


def SaveExcel (wb, fileName):
    try:
        wb.save (os.path.join (directory, fileName + ".xls"))
        print (fileName + " was successfully created")
    except:
        print ("File is not created")
        print (format_exc ())

 
def CreateAndSaveSheetInExcel (fileName, *styles):
    wb = Workbook ()
    fontSheet = wb.add_sheet (fileName)
    printSymbolsToExcel (fontSheet, ", ".join (styles))
    SaveExcel (wb, fileName)


fontList = getListFromFile ("Fonts.txt")
symbolList = getListFromFile ("Symbols.txt")

# Create and format an excel workbook for regular font
CreateAndSaveSheetInExcel ("RegularFont")
# Create and format an excel workbook for bold font
CreateAndSaveSheetInExcel ("BoldFont", "bold 1")
# Create and format an excel workbook for italic font
CreateAndSaveSheetInExcel ("ItalicFont", "italic 1")
# Create and format an excel workbook for bold italic font
CreateAndSaveSheetInExcel ("ItalicAndBoldFont", "bold 1", "italic 1")