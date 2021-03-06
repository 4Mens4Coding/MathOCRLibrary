from ImageProcessing import ImageController
import MySQLdb as mdb
 
try:
    con = mdb.connect ("server_ip", "user", "password", "database")
    cur = con.cursor ()
    ic = ImageController () 
    ic.appendImageFromPath ("/home/MathOCR/MathOCRLibrary/ImageProcessing/6")
    ic.firstToBinaryArray ()
    matrix = ic.getBinaryArray (0)
    correct = "5"
    cur.execute ("INSERT INTO `MathOCR`.`binarizedData` (`id`,`image`,`correct`) VALUES ({0},{1},{2}".format (id, matrix, correct))

finally:
    if (con):
        con.close ()