import cv2
import numpy as np
import operator
import os
from googletrans import Translator

# module level variables ##########################################################################
MIN_CONTOUR_AREA = 30
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30
IMAGE_NAME = "ocr_samples/othertext3.PNG"
###################################################################################################

class ContourWithData():

    # member variables ############################################################################
    npaContour = None           # contour
    boundingRect = None         # bounding rect for contour
    intRectX = 0                # bounding rect top left corner x location
    intRectY = 0                # bounding rect top left corner y location
    intRectWidth = 0            # bounding rect width
    intRectHeight = 0           # bounding rect height
    fltArea = 0.0               # area of contour

    def calculateRectTopLeftPointAndWidthAndHeight(self):               # calculate bounding rect info
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight

    def checkIfContourIsValid(self):                            # this is oversimplified, for a production grade program
        if self.fltArea < MIN_CONTOUR_AREA: return False        # much better validity checking would be necessary
        return True

# Custom characters dictionary
russianChars = {
    192: "А",
    193: "Б",
    194: "В",
    195: "Г",
    196: "Д",
    197: "Е",
    168: "Ё",
    198: "Ж",
    199: "З",
    200: "И",
    201: "Й",
    202: "К",
    203: "Л",
    204: "М",
    205: "Н",
    206: "О",
    207: "П",
    208: "Р",
    209: "С",
    210: "Т",
    211: "У",
    212: "Ф",
    213: "Х",
    214: "Ц",
    215: "Ч",
    216: "Ш",
    217: "Щ",
    218: "Ъ",
    219: "Ы",
    220: "Ь",
    221: "Э",
    222: "Ю",
    223: "Я"
}

allContoursWithData = []                # declare empty lists,
validContoursWithData = []              # we will fill these shortly

try:
    npaClassifications = np.loadtxt("12-2-1520-classifications.txt", np.float32)                  # read in training classifications
except:
    print("error, unable to open 12-2-1520-classifications.txt, exiting program\n")
    os.system("pause")
    exit()

try:
    npaFlattenedImages = np.loadtxt("12-2-1520-flattened_images.txt", np.float32)                 # read in training images
except:
    print("error, unable to open 12-2-1520-flattened_images.txt, exiting program\n")
    os.system("pause")
    exit()

# reshape numpy array to 1d, necessary to pass to call to train
npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))
kNearest = cv2.ml.KNearest_create()  # instantiate KNN object
kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

imgTestingNumbers = cv2.imread(IMAGE_NAME)          # read in testing image

if imgTestingNumbers is None:                           # if image was not read successfully
    print("error: image not read from file \n\n")        # print error message to std out
    os.system("pause")                                  # pause so user can see error message
    exit()                                              # and exit function (which exits program)

imgGray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)       # get grayscale image
imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)                    # blur

# filter image from grayscale to black and white
imgThresh = cv2.adaptiveThreshold(imgBlurred,                           # input image
                                  255,                                  # make pixels that pass the threshold full white
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # use gaussian rather than mean, seems to give better results
                                  cv2.THRESH_BINARY_INV,                # invert so foreground will be white, background will be black
                                  11,                                   # size of a pixel neighborhood used to calculate threshold value
                                  2)                                    # constant subtracted from the mean or weighted mean

imgThreshCopy = imgThresh.copy()        # make a copy of the thresh image, this in necessary b/c findContours modifies the image

npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,             # input image, make sure to use a copy since the function will modify this image in the course of finding contours
                                             cv2.RETR_EXTERNAL,         # retrieve the outermost contours only
                                             cv2.CHAIN_APPROX_SIMPLE)   # compress horizontal, vertical, and diagonal segments and leave only their end points

for npaContour in npaContours:                             # for each contour
    contourWithData = ContourWithData()                                             # instantiate a contour with data object
    contourWithData.npaContour = npaContour                                         # assign contour to contour with data
    contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)     # get the bounding rect
    contourWithData.calculateRectTopLeftPointAndWidthAndHeight()                    # get bounding rect info
    contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)           # calculate the contour area
    allContoursWithData.append(contourWithData)                                     # add contour with data object to list of all contours with data

for contourWithData in allContoursWithData:                 # for all contours
    if contourWithData.checkIfContourIsValid():             # check if valid
        validContoursWithData.append(contourWithData)       # if so, append to valid contour list

# Need to group by line somehow, then sort each line by left to right position
validContoursWithData.sort(key = operator.attrgetter("intRectY")) # First sort by Y position

# Next find max distance y between two in sorted list
maxDiffY = 0
prevRectY = validContoursWithData[0].intRectY
first = True
for contour in validContoursWithData:
    if first:
        first = False
    else:
        diffY = contour.intRectY - prevRectY
        if diffY > maxDiffY:
            maxDiffY = diffY
        prevRectY = contour.intRectY

# Now use max difference to differentiate lines
lineDiffLimit = maxDiffY / 3
contourLines = [[]]
prevRectY = validContoursWithData[0].intRectY
first = True
lineNum = 0
for contour in validContoursWithData:
    if first:
        contourLines[lineNum].append(contour)
        first = False
    else:
        diffY = contour.intRectY - prevRectY
        if diffY > lineDiffLimit:
            contourLines.append([])
            lineNum += 1
        contourLines[lineNum].append(contour)
        prevRectY = contour.intRectY

# Now sort each line by x position
for contourLine in contourLines:
    contourLine.sort(key = operator.attrgetter("intRectX"))

strFinalString = "" # declare final string
for contourLine in contourLines: # for each contour line
    for contourWithData in contourLine: # for each contour in this line
        # draw a green rect around the current char
        cv2.rectangle(imgTestingNumbers,                                        # draw rectangle on original testing image
                      (contourWithData.intRectX, contourWithData.intRectY),     # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth, contourWithData.intRectY + contourWithData.intRectHeight),      # lower right corner
                      (0, 255, 0),              # green
                      2)                        # thickness

        imgROI = imgThresh[contourWithData.intRectY : contourWithData.intRectY + contourWithData.intRectHeight,     # crop char out of threshold image
                           contourWithData.intRectX : contourWithData.intRectX + contourWithData.intRectWidth]

        imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))  # resize image, this will be more consistent for recognition and storage

        npaROIResized = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT)) # flatten image into 1d numpy array

        npaROIResized = np.float32(npaROIResized) # convert from 1d numpy array of ints to 1d numpy array of floats

        retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized, k = 1)     # call KNN function find_nearest

        cv2.imshow("imgTestingNumbers", imgTestingNumbers)  # show input image with green boxes drawn around found digits
        cv2.waitKey(0)  # wait for user key press to continue

        # Print textual results
        npaResultInt = int(npaResults[0][0])
        strCurrentChar = russianChars[npaResultInt]
        print(str(npaResultInt) + ": " + strCurrentChar)

        strFinalString = strFinalString + strCurrentChar # append current char to full string

print("\n" + strFinalString + "\n")  # show the full string

# Sample translation
# translator = Translator()
# translation = translator.translate("Образец русских слов")
# print(translation.text)

cv2.destroyAllWindows()             # remove windows from memory
