from PIL import Image
from queue import Queue
from traceback import format_exc

class ImageController:
    """ Des: Image processing class
        Inf: Valentinas                                 6/9/2018 """
    def __init__ (self, threshold = 255):
        self.__imageList = Queue ()
        self.__processedImagesList = []
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
        self.__processedImagesList.append (self.__toBinaryArray (image))


    def allToBinaryArray (self):
        """ Convert to binary matrix all stored images """
        while not self.__imageList.empty ():
            image = self.__imageList.get ()
            self.__processedImagesList.append (self.__toBinaryArray (image))


    def __toBinaryArray (self, image):
        """ Private method to convert image to binary array """
        # Downscale an image (get R, G, B tuple)
        # Good for small pictures, but really bad for big one.
        image = image.resize ((100, int (image.size[1] * 100 / image.size[0])))
        width, height = image.size
        pixels = image.getdata ()
        # Get binary list based on threshold
        binary = list (map (lambda color: int (sum (color) < self.threshold * 3 // 2), pixels))
        array2d = [binary[i * width: (i + 1) * width] for i in range (height)]
        return array2d

    
    def getProcessedImagesList (self):
        """ Return all stored processed image arrays """
        return self.__processedImagesList

    
    def getProcessedImage (self, index):
        """ Return processed image matrix in selected location (index) """
        if ((index <= len (self.__processedImagesList)) & (index > -1)):
            return self.__processedImagesList[index]


    def cleanProcessedImagesList (self):
        """ Remove all stored processed image arrays from the list """
        del self.__processedImagesList[:]


    def printProcessedImagesListAsMatrix (self):
        """ Print all processed images in the list with matrix shape """
        for binArr in self.__processedImagesList:
            print (self.getProcessedImagesListAsMatrix (binArr))
            print ("-----------------------------------")


    def getProcessedImagesListAsMatrix (self, ProcessedImageArray):
        """ return one selected processed image array with matrix shape """
        return "\n".join (''.join ('{:5}'.format (value) for value in row) for row in ProcessedImageArray)


    def firstToPixelMatrix (self):
        """ Convert first stored image to pixel matrix with values from 0 to 1 """
        image = self.__imageList.get ()
        self.__processedImagesList.append (self.__toPixelMatrix (image))

    def allToPixelMatrix (self):
        """ Convert all stored images to pixel matrix with values from 0 to 1 """
        while not self.__imageList.empty ():
            image = self.__imageList.get ()
            self.__processedImagesList.append (self.__toPixelMatrix (image))


    def __toPixelMatrix (self, image):
        """ Private method to convert image to pixel matrix with values from 0 to 1 """
        image = image.resize ((100, int (image.size[1] * 100 / image.size[0])))
        width, height = image.size
        pixels = list (image.getdata ())
        data = []
        for pixel in pixels:
            grays = pixel[0] * 299 / 1000 + pixel[1] * 587 / 1000 + pixel[2] * 114 / 1000
            data.append ("{0:.2f}".format (-grays / 255 + 1))
        return [data[offset:offset + width] for offset in range (0, width * height, width)]


    def countOfImagesInQueue (self):
        """ Number of pictures added to queue """
        return self.__imageList.qsize ()


    def countOfProcessedImages (self):
        """ Number of processed pictures """
        return len (self.__processedImagesList)


    def __str__ (self):
        """ Print information about image controller """
        return """ - Images: {0}\n - ProcessedImages: {1}\n - Pending: {2}\n - Threshold: {3}\n""".format (self.__imageList.qsize (), 
            len (self.__processedImagesList), self.__imageList.qsize () - len (self.__processedImagesList), self.threshold)