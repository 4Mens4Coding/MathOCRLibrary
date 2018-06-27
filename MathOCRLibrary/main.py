from glob import iglob
from ImageProcessing import ImageController
#from ImageProcessing.ImageProcessing import ImageController
import sys
from PIL import Image

def main ():
    """ Des: This is our main program
        Inf: Author                        last_modification_time """
    ImController = ImageController (400)
    trainingDataLocation = iglob ("*/TrainingData/test/*.png")
    for imagePath in trainingDataLocation:
        ImController.appendImageFromPath (imagePath)
    ImController.allToPixelMatrix ()
    ImController.printProcessedImagesListAsMatrix ()
    ImController.cleanProcessedImagesList ()

if __name__ == "__main__":
    main ()