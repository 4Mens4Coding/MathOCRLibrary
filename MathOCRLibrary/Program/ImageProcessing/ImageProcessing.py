from PIL import Image
from queue import Queue
from traceback import format_exc

class ImageController:
    """ Des: Image processing class
        Inf: Valentinas                                 6/9/2018 """
    def __init__ (self, threshold = 255):
        self.__imageList = Queue ()
        self.__binaryArrayList = []
        self.threshold = threshold


    def appendImage (self, image):
        """ Add image to the __imageList """
        self.__imageList.put (image.copy ())


    def appendImageFromPath (self, imagePath):
        """ Add image to the __imageList from path """
        try:
            with Image.open (imagePath, 'r') as image:
                self.__imageList.put (image.copy ())
        except:
            raise format_exc ()
    

    def firstToBinaryArray (self):
        """ Convert to binary matrix first stored image """
        image = self.__imageList.get ()
        self.__binaryArrayList.append (self.__toBinaryArray (image))


    def allToBinaryArray (self):
        """ Convert to binary matrix all stored images """
        while not self.__imageList.empty ():
            image = self.__imageList.get ()
            self.__binaryArrayList.append (self.__toBinaryArray (image))


    def __toBinaryArray (self, image):
        """ Private method to convert image to binary array """
        # Downscale an image (get R, G, B tuple)
        # Good for small pictures, but really bad for big one.
        image = image.resize ((100, int (image.size[1] * 100 / image.size[0])))
        pixels = image.getdata ()
        # Get binary list based on threshold
        binary = list (map (lambda color: int (sum (color) > self.threshold * 3 // 2), pixels))
        array2d = [binary[i * image.size[0]: (i + 1) * image.size[0]] for i in range (image.size[1])]
        return array2d

    
    def getAllBinaryArrays (self):
        """ Return all stored binary arrays """
        return self.__binaryArrayList

    
    def getBinaryArray (self, index):
        """ Return binary array in selected location (index) """
        if ((index <= len (self.__binaryArrayList)) & (index > -1)):
            return self.__binaryArrayList[index]


    def cleanBinaryArrayList (self):
        """ Remove all stored binary arrays from the list """
        del self.__binaryArrayList[:]


    def printAllBinaryArraysAsMatrix (self):
        """ Print all binary arrays in the list with matrix shape """
        for binArr in self.__binaryArrayList:
            print (self.getBinaryArrayAsMatrix (binArr))


    def getBinaryArrayAsMatrix (self, BinaryArray):
        """ return one selected binary array with matrix shape """
        return "\n".join ("".join (map (str, line)) for line in BinaryArray)


    def countOfImagesInQueue (self):
        """ Number of pictures added to queue """
        return self.__imageList.qsize ()


    def countOfBinarizedImages (self):
        """ Number of binarized pictures """
        return len (self.__binaryArrayList)


    def __str__ (self):
        """ Print information about image controller """
        return """ - Images: {0}\n - ConvertedToBinaryArray: {1}\n - Pending: {2}\n - Threshold: {3}\n""".format (self.__imageList.qsize (), 
            len (self.__binaryArrayList), self.__imageList.qsize () - len (self.__binaryArrayList), self.threshold)