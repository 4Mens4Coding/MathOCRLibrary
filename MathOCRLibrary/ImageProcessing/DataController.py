from ImageProcessing import ImageController
<<<<<<< HEAD
import MySQLdb as mdb
 
try:
  con = mdb.connect('server_ip','user','password','database');
  cur = con.cursor()
  ic = ImageController() 
  ic.appendImageFromPath("/home/MathOCR/MathOCRLibrary/ImageProcessing/6")
  ic.firstToBinaryArray()
  matrix = ic.getBinaryArray(0)
  correct = "5"
  cur.execute("INSERT INTO `MathOCR`.`binarizedData` (`id`,`image`,`correct`) VALUES ({0},{1},{2}".format(id,matrix,correct))
finally:
  if con:
    con.close()
=======
import MySQLdb
 
db = MySQLdb.connect (host = "localhost", user = "root", passwd = "50dbc998", db = "MathOCR")
cur = db.cursor ()
ic = ImageController ()
ic.appendImageFromPath ("/home/MathOCR/MathOCRLibrary/ImageProcessing/6")
ic.firstToBinaryArray ()
matrix = ic.getBinaryArray (0)
correct = "5"
cur.execute ("INSERT INTO binarizedData (image, correct) VALUES ({0},{1})".format (matrix,correct))
>>>>>>> 102f6f990c8da49c4f58b5955a485346a2591dfe
