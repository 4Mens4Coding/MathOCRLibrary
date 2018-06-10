import pytest
import os
from PIL import Image
from traceback import format_exc
#from Program.ImageProcessing.ImageProcessing import ImageController as IC
from Program.ImageProcessing import ImageController as IC

imContr = IC ()
imageDataPath = os.path.join (os.path.dirname (__file__), "UnitTest_TestData/Data_ImageProcessing.PNG")

#@pytest.fixture(scope="module")
#def imContr():
#    return ImContr()
#@pytest.fixture (autouse=True)
class TestClass_ImageProcessing:
    @pytest.fixture (autouse=True)
    def test_appendImage_countOfImagesInQueue (self):
        count = imContr.countOfImagesInQueue ()
        with Image.open (imageDataPath, 'r') as image:
            imContr.appendImage (image)
        assert imContr.countOfImagesInQueue () == count + 1


    @pytest.mark.smoke
    def test_appendImageFromPath_countOfImagesInQueue (self):
        count = imContr.countOfImagesInQueue ()
        imContr.appendImageFromPath (imageDataPath)
        assert imContr.countOfImagesInQueue () == count + 1


    def test_firstToBinaryArray (self,):
        countImg = imContr.countOfImagesInQueue ()
        countBin = imContr.countOfBinarizedImages ()
        imContr.firstToBinaryArray ()
        assert imContr.countOfImagesInQueue () == countImg - 1
        assert imContr.countOfBinarizedImages () == countBin + 1


    def test_allToBinaryArray (self):
        for i in range (3):
            imContr.appendImageFromPath (imageDataPath)
        countImg = imContr.countOfImagesInQueue ()
        countBin = imContr.countOfBinarizedImages ()
        imContr.allToBinaryArray ()
        assert imContr.countOfImagesInQueue () == 0
        assert imContr.countOfBinarizedImages () == countBin + countImg


    def test_printImageController (self):
        try:
            print (imContr)
        except:
            raise format_exc ()


    def test_printAllBinaryArraysAsMatrix (self):
        try:
            imContr.printAllBinaryArraysAsMatrix ()
        except:
            raise format_exc ()


    def test_getBinaryArray_outOfRange (self):
        assert imContr.getBinaryArray (500) == None


    def test_getBinaryArray_outOfRange (self):
        assert imContr.getBinaryArray (-5) == None


    def test_allToBinaryArray (self):
        IC2 = IC ()
        for i in range (2):
            IC2.appendImageFromPath (imageDataPath)
        IC2.allToBinaryArray ()
        assert IC2.getBinaryArray (0) == IC2.getBinaryArray (1)


    def test_getBinaryArrayAsMatrix (self):
        pass


    def test_getBinaryArrayAsMatrix (self):
        pass


    def test_cleanBinaryArrayList (self):
        imContr.cleanBinaryArrayList ()
        assert imContr.countOfBinarizedImages () == 0