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
        return [line for line in f.readlines ()]
            

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
    fontSheet = wb.add_sheet (fileName)
    printSymbolsToExcel (fontSheet, ", ".join (styles))
    saveExcel (wb, fileName)


def createAFolder (name):
    """ Des: Create a folder in selected location
        Inf: Valentinas                                 6/2/2018 """
    path = os.path.join (directory, name)
    if not os.path.exists (path):
        os.makedirs (path)
    return path


def getImageFromCell (fileName):
    """ Des: Get image from excel
        Inf: Valentinas                                 6/2/2018 """
    # TODO: need to test this function!!!
    xls = Dispatch ('Excel.Application')
    xlswb = xls.Workbooks.Open (os.path.join (directory, fileName), ReadOnly = True)
    print (fileName[:-4])
    excelFile = xlswb.Sheets (fileName[:-4])
    for i in range (0, len (symbolList)):
        for j in range (0, len (fontList)):
            _range = "%s:%s" % (i, j)
            try:
                range = excelFile.workbook.Application.Range (_range)
            except com_error:
                raise Exception ("Failed locating range %s" % (_range))
        
            # See http://stackoverflow.com/a/42465354/1924207
            for shape in range.parent.Shapes: pass

            xlScreen, xlPrinter = 1, 2
            xlPicture, xlBitmap = -4147, 2
            retries, success = 50, False
            while not success:
                try:
                    range.CopyPicture (xlScreen, xlBitmap)
                    im = ImageGrab.grabclipboard ()
                    im.save (str (symbolList[i]) + str (j) + fileName[:-4] + ".PNG", str (symbolList[i]) + str (j))
                    success = True
                except (com_error, AttributeError) as e:
                    # When other (big) Excel documents are open,
                    # copyPicture fails intermittently
                    retries -= 1
                    if retries == 0: raise


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

## create images from created excel files
getImageFromCell ("RegularFont.xls")
getImageFromCell ("BoldFont.xls")
getImageFromCell ("ItalicFont.xls")
getImageFromCell ("ItalicAndBoldFont.xls")
