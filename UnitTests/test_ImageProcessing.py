import pytest
import os
from PIL import Image
from traceback import format_exc
from MathOCRLibrary.ImageProcessing import ImageController as IC

imContr = IC ()
imageDataPath = os.path.join (os.path.dirname (__file__), "UnitTest_TestData/Data_ImageProcessing.PNG")

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
        countBin = imContr.countOfProcessedImages ()
        imContr.firstToBinaryArray ()
        assert imContr.countOfImagesInQueue () == countImg - 1
        assert imContr.countOfProcessedImages () == countBin + 1


    def test_allToBinaryArray (self):
        for i in range (3):
            imContr.appendImageFromPath (imageDataPath)
        countImg = imContr.countOfImagesInQueue ()
        countBin = imContr.countOfProcessedImages ()
        imContr.allToBinaryArray ()
        assert imContr.countOfImagesInQueue () == 0
        assert imContr.countOfProcessedImages () == countBin + countImg


    def test_getBinaryArray_outOfRange (self):
        assert imContr.getProcessedImage (500) == None


    def test_getBinaryArray_outOfRange (self):
        assert imContr.getProcessedImage (-5) == None


    def test_firstToPixelMatrix (self,):
        countImg = imContr.countOfImagesInQueue ()
        countBin = imContr.countOfProcessedImages ()
        imContr.firstToPixelMatrix ()
        assert imContr.countOfImagesInQueue () == countImg - 1
        assert imContr.countOfProcessedImages () == countBin + 1


    def test_allToPixelMatrix (self):
        for i in range (3):
            imContr.appendImageFromPath (imageDataPath)
        countImg = imContr.countOfImagesInQueue ()
        countBin = imContr.countOfProcessedImages ()
        imContr.allToPixelMatrix ()
        assert imContr.countOfImagesInQueue () == 0
        assert imContr.countOfProcessedImages () == countBin + countImg


    def test_getProcessedImage_withBinaryArray (self):
        IC2 = IC ()
        for i in range (2):
            IC2.appendImageFromPath (imageDataPath)
        IC2.allToBinaryArray ()
        assert IC2.getProcessedImage (0) == IC2.getProcessedImage (1)


    def test_allToPixelMatrix_withPixelMatrix (self):
        IC2 = IC ()
        for i in range (2):
            IC2.appendImageFromPath (imageDataPath)
        IC2.allToPixelMatrix ()
        assert IC2.getProcessedImage (0) == IC2.getProcessedImage (1)


    def test_getBinaryArrayAsMatrix_withBinaryArray (self):
        pass


    def test_getBinaryArrayAsMatrix_withPixelMatrix (self):
        pass


    def test_cleanProcessedImagesList (self):
        imContr.cleanProcessedImagesList ()
        assert imContr.countOfProcessedImages () == 0
