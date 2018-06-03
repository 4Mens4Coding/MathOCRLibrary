import os
from xlwt import Workbook, easyxf
from traceback import format_exc
from win32com.client import Dispatch
from PIL import ImageGrab # to make a shortcut in excel
from pywintypes import com_error


directory = os.path.dirname (os.path.abspath (__file__))

def getListFromFile (fileName):
    """ Des: Function to create a list of lines in file
        Inf: Valentinas                                 6/2/2018 """
    with open (os.path.join (directory, fileName), "r") as f:
        return [line for line in f.read ().splitlines ()]
            

def printSymbolsToExcel (sheet, fontType = ""):
    """ Des: Fill excel sheet with symbols and all different fonts
        Inf: Valentinas, Deividas                        6/2/2018 """
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


def saveExcel (wb, fileName):
    """ Des: Save excel file from started workbook
        Inf: Valentinas                                 6/2/2018 """
    try:
        wb.save (os.path.join (directory, fileName))
        print (fileName + " was successfully created")
    except:
        print ("File is not created")
        print (format_exc ())

 
def createAndSaveSheetInExcel (fileName, *styles):
    """ Des: Save excel file from started workbook
        Inf: Valentinas                                 6/2/2018 """
    wb = Workbook ()
    fontSheet = wb.add_sheet (fileName[:-4])
    printSymbolsToExcel (fontSheet, ", ".join (styles))
    saveExcel (wb, fileName)


def createAFolder (path, name):
    """ Des: Create a folder in selected location
        Inf: Valentinas                                 6/2/2018 """
    loc = os.path.join (path, name)
    if not os.path.exists (loc):
        os.makedirs (loc)
    return loc


def getImageFromCell (fileName):
    """ Des: Get image from excel
        Inf: Valentinas                                 6/2/2018 """
    xls = Dispatch ('Excel.Application')
    xls.Visible = 0
    xlswb = xls.Workbooks.Open (os.path.join (directory, fileName), ReadOnly = True)
    excelFile = xlswb.Sheets (fileName[:-4])
    for i in range (1, len (symbolList) + 1):
        location = createAFolder (os.path.join (directory, "TrainingData"), str (i))
        for j in range (1, len (fontList) + 1):
            print ("{0}: {1}, {2}".format (fileName[:-4], i, j))
            try:
                rng = excelFile.Application.Cells (i, j)
            except com_error:
                raise Exception ("Failed locating in excel")
        
            # See http://stackoverflow.com/a/42465354/1924207
            for shape in rng.parent.Shapes: pass

            retries = 50
            success = False
            while not success:
                try:
                    rng.CopyPicture (1, 2)
                    im = ImageGrab.grabclipboard ()
                    path = os.path.join (location, str (j) + fileName[:-4] + ".PNG")
                    im.save (path, "PNG")
                    success = True
                except (com_error, AttributeError) as e:
                    # When other (big) Excel documents are open,
                    # copyPicture fails intermittently
                    retries -= 1
                    if retries == 0: raise
    xlswb.Close (True)

fontList = getListFromFile ("Fonts.txt")
symbolList = getListFromFile ("Symbols.txt")

# Create and format an excel workbook for regular font
createAndSaveSheetInExcel ("RegularFont.xls")
# Create and format an excel workbook for bold font
createAndSaveSheetInExcel ("BoldFont.xls", "bold 1")
# Create and format an excel workbook for italic font
createAndSaveSheetInExcel ("ItalicFont.xls", "italic 1")
# Create and format an excel workbook for bold italic font
createAndSaveSheetInExcel ("ItalicAndBoldFont.xls", "bold 1", "italic 1")

# create images from created excel files
getImageFromCell ("RegularFont.xls")
getImageFromCell ("BoldFont.xls")
getImageFromCell ("ItalicFont.xls")
getImageFromCell ("ItalicAndBoldFont.xls")
