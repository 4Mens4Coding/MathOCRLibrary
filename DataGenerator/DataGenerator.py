import os
from xlwt import Workbook, easyxf
from traceback import format_exc

# Create and format an excel workbook
wb = Workbook ()
sheet_Notes = wb.add_sheet ("DataForTraining")

fontList = ["Agency FB", "Aharoni", "Aldhabi", "Algerian", "Almanac MT", "American Uncial", "Andale Mono", "Andalus", "Andy", "AngsanaUPC",
            "Angsana New", "Aparajita", "Arabic Transparent", "Arabic Typesetting", "Arial", "Arial Black", "Arial Narrow", "Arial Narrow Special",
            "Arial Rounded MT", "Arial Special", "Arial Unicode MS", "Augsburger Initials", "Baskerville Old Face", "Batang", "BatangChe", "Bauhaus 93",
            "Beesknees ITC", "Bell MT", "Berlin Sans FB", "Bernard MT Condensed", "Bickley Script", "Blackadder ITC", "Bodoni MT", "Bodoni MT Condensed",
            "Bon Apetit MT", "Bookman Old Style", "Bookshelf Symbol", "Book Antiqua", "Bradley Hand ITC", "Braggadocio", "BriemScript", "Britannic Bold",
            "Britannic Bold", "Broadway", "BrowalliaUPC", "Browallia New", "Brush Script MT", "Calibri", "Californian FB", "Calisto MT", "Cambria",
            "Candara", "Cariadings", "Castellar", "Centaur", "Century", "Century Gothic", "Century Schoolbook", "Chiller", "Colonna MT",
            "Comic Sans MS", "Consolas", "Constantia", "Contemporary Brush", "Cooper Black", "Copperplate Gothic", "Corbel", "CordiaUPC", "Cordia New",
            "Courier New", "Curlz MT", "DaunPenh", "David", "Desdemona", "DFKai-SB", "DilleniaUPC", "Directions MT", "DokChampa", "Dotum", "DotumChe",
            "Ebrima", "Eckmann", "Edda", "Edwardian Script ITC", "Elephant", "Engravers MT", "Enviro", "Eras ITC", "Estrangelo Edessa", "EucrosiaUPC",
            "Euphemia", "Eurostile", "FangSong", "Felix Titling", "Fine Hand", "Fixed Miriam Transparent", "Flexure", "Footlight MT", "Forte",
            "Franklin Gothic", "Franklin Gothic Medium", "FrankRuehl", "FreesiaUPC", "Freestyle Script", "French Script MT", "Futura", "Gabriola",
            "Gadugi", "Garamond", "Garamond MT", "Gautami", "Georgia", "Georgia Ref", "Gigi", "Gill Sans MT", "Gill Sans MT Condensed", "Gisha",
            "Gloucester", "Goudy Old Style", "Goudy Stout", "Gradl", "Gulim", "GulimChe", "Gungsuh", "GungsuhChe", "Haettenschweiler", "Harlow Solid Italic",
            "Harrington", "High Tower Text", "Holidays MT", "Impact", "Imprint MT Shadow", "Informal Roman", "IrisUPC", "Iskoola Pota", "JasmineUPC",
            "Jokerman", "Juice ITC", "KaiTi", "Kalinga", "Kartika", "Keystrokes MT", "Khmer UI", "Kino MT", "KodchiangUPC", "Kokila", "Kristen ITC",
            "Kunstler Script", "Lao UI", "Latha", "LCD", "Leelawadee", "Levenim MT", "LilyUPC", "Lucida Blackletter", "Lucida Bright", "Lucida Bright Math",
            "Lucida Calligraphy", "Lucida Console", "Lucida Fax", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter", "Lucida Sans Unicode",
            "Magneto", "Maiandra GD", "Malgun Gothic", "Mangal", "Map Symbols", "Matisse ITC", "Matura MT Script Capitals", "McZee", "Mead Bold",
            "Meiryo", "Meiryo UI", "Mercurius Script MT Bold", "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft JhengHei UI", "Microsoft New Tai Lue",
            "Microsoft PhagsPa", "Microsoft Sans Serif", "Microsoft Tai Le", "Microsoft Uighur", "Microsoft YaHei", "Microsoft YaHei UI", "Microsoft Yi Baiti",
            "MingLiU-ExtB", "PMingLiU", "MingLiU_HKSCS-ExtB", "MingLiU_HKSCS", "Minion Web", "Miriam", "Miriam Fixed", "Mistral", "Modern No. 20", "Mongolian Baiti",
            "Monotype.com", "Monotype Corsiva", "Monotype Sorts", "MoolBoran", "MS Gothic", "MS LineDraw", "MS Mincho", "MS PGothic", "MS PMincho",
            "MS Reference", "MS UI Gothic", "MV Boli", "Myanmar Text", "Narkisim", "News Gothic MT", "New Caledonia", "Niagara", "Nirmala UI", "NSimSun",
            "Nyala", "OCR-B-Digits", "OCRB", "OCR A Extended", "Old English Text MT", "Onyx", "Palace Script MT", "Palatino Linotype", "Papyrus", "Parade", "Parchment",
            "Parties MT", "Peignot Medium", "Pepita MT", "Perpetua", "Perpetua Titling MT", "Placard Condensed", "Plantagenet Cherokee", "Playbill", "PMingLiU-ExtB",
            "PMingLiU-ExtB", "Poor Richard", "Pristina", "Raavi", "Rage Italic", "Ransom", "Ravie", "RefSpecialty", "Rockwell", "Rockwell Condensed", "Rockwell Extra Bold",
            "Rod", "Runic MT Condensed", "Sakkal Majalla", "Script MT Bold", "Segoe Chess", "Segoe Print", "Segoe Pseudo", "Segoe Script", "Segoe UI Symbol", "Segoe UI Symbol",
            "Shonar Bangla", "Showcard Gothic", "Shruti", "Signs MT", "SimHei", "Simplified Arabic Fixed", "Simplified Arabic Fixed", "SimSun-ExtB", "SimSun-ExtB", 
            "Sports MT", "Stencil", "Stop", "Sylfaen", "Symbol", "Tahoma", "Tempo Grunge", "Tempus Sans ITC", "Temp Installer Font", "Times New Roman", "Times New Roman Special",
            "Traditional Arabic", "Transport MT", "Trebuchet MS", "Tunga", "Tw Cen MT", "Tw Cen MT Condensed", "Urdu Typesetting", "Utsaah", "Vacation MT", "Vani", "Verdana",
            "Verdana Ref", "Vijaya", "Viner Hand ITC", "Vivaldi", "Vixar ASCI", "Vladimir Script", "Vrinda", "Westminster"]

symbolList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "/", "*", "=", ",", ".", "(", ")", "[", "]", "{", "}"]

for i in range (0, len (symbolList)):
        sheet_Notes.col (i).width_mismatch = True
        sheet_Notes.col (i).width = 256*10

for i in range (0, len (fontList)):
        sheet_Notes.row (i).height_mismatch = True
        sheet_Notes.row (i).height = 256*5

# Fill all excel with symbols	
line = 0
for font in fontList:
        font_style = easyxf ("font: name " + font + ", height 1200")
        col = 0
        for symb in symbolList:
                sheet_Notes.write (line, col, symb, font_style)
                col += 1
        line += 1 

# Save excel file
try:
        wb.save ("DataForTraining.xls")
        print ("File successfully created")
except:
        print ("File is not created")
        print (format_exc ())
