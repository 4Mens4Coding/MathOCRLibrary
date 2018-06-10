""" Des: This is our main program
    Inf: Author                        last_modification_time """

from glob import iglob, glob
#from ImageProcessing import ImageController
from ImageProcessing.ImageProcessing import ImageController
import sys
from PIL import Image

def main ():
    threshold = 255
    ImController = ImageController (threshold)
    jjj = glob ("*/*/TrainingData/test/*.png")
    trainingDataLocation = iglob ("*/*/TrainingData/test/*.png")

    # open image from file system
    for imagePath in trainingDataLocation:
        with Image.open (imagePath, 'r') as image:
            BinArray = ImController.appendImage (image)

    trainingDataLocation = iglob ("*/*/TrainingData/test/*.png")
    for imagePath in trainingDataLocation:
        ImController.appendImageFromPath (imagePath)

    print (ImController)
    ImController.firstToBinaryArray ()
    ImController.allToBinaryArray ()
    ImController.getAllBinaryArrays ()
    temp = ImController.getBinaryArray (1)
    ImController.printBinaryAsMatrix (temp)
    ImController.printAllBinaryArrayAsMatrix ()
    ImController.cleanBinaryArray ()


if __name__ == "__main__":
    main ()