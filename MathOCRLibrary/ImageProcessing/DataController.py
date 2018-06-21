from ImageProcessing import ImageController
import MySQLdb
 
db = MySQLdb.connect (host = "localhost", user = "root", passwd = "50dbc998", db = "MathOCR")
cur = db.cursor ()
ic = ImageController ()
ic.appendImageFromPath ("/home/MathOCR/MathOCRLibrary/ImageProcessing/6")
ic.firstToBinaryArray ()
matrix = ic.getBinaryArray (0)
correct = "5"
cur.execute ("INSERT INTO binarizedData (image, correct) VALUES ({0},{1})".format (matrix,correct))