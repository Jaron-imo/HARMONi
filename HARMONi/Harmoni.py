# This function is called for the creation of an image "Generated"
# Function needs an INPUT "Key"
# Function loads image "Fretbord.jpg"
# With FretboardAssist and HarmAssist tones of Key are inserted to "Fretboard.jpg"
# Image then saved in directory as "generated.jpg" - return

import cv2
import numpy as np
import FretboardAssist as FbA
import HarmAssist as HA

fretboard = cv2.imread(".\img\Fretboard.jpg", 0)

def CreateFretboardScale(Key):
    Key

def CreateFretboardScale(Key):

#____GLOBAL_VAR______________________________________________
    frets = 16
    strings = 6
    tuning = ['E', 'A', 'D', 'G', 'B', 'E'] 
    tones = ['A','Ais','B','C','Cis','D','Dis','E','F','Fis','G','Gis']
    #Key = "D"
    
#____ARRAY_POSITIONS_________________________________________
    frets_array = FbA.fret_positions(frets = 16, frets_0 = 44, frets_1  = 115, step_size_X = 95)
    strings_array = FbA.string_positions(strings = 6, strings_0 = 45, strings_1 = 101, step_size_Y = 56)

    print (frets_array)
    print (strings_array)

#____FRETBOARD_ARRAY_______________________ 
    board_array = HA.fret_gen(tuning, frets, strings)
    print(board_array)

#____SCALE_GENERATOR_____________________
    scale = HA.scale_gen(Key)
    print("Scale: ",scale)

#____PENTA_GENERATOR_______________________
    penta = HA.penta_gen(Key)
    print("Pentatonic: ",penta)

#_____IMAGE_PROCESSING_____________________
    fretboard = cv2.imread(".\img\Fretboard.jpg", 1)
    for n in range(len(strings_array)):
        for m in range(len(frets_array)):       
            if board_array[n,m] in scale:
                f = int(frets_array[m])
                s = int(strings_array[n])

                if board_array[n,m] in penta:
                    cv2.circle(fretboard, (f,s), 16, (255,0,0), 4)
                else:
                    cv2.circle(fretboard, (f,s), 16, (0,0,255), 4)
                cv2.circle(fretboard, (f,s), 7, (255,255,255), 14)
                note = board_array[n,m]
                cv2.putText(fretboard,note, (f-10,s+4), cv2.FONT_HERSHEY_PLAIN, 1, 0 ,0)    
    #cv2.imshow("HARMONi", fretboard)
    #cv2.waitKey(5000)
    cv2.imwrite(".\img\Generated.jpg", fretboard)
    return(fretboard)

def CreateFretboardAllTones():
    #____GLOBAL_VAR______________________________________________
    frets = 16
    strings = 6
    tuning = ['E', 'A', 'D', 'G', 'B', 'E'] 
    tones = ['A','Ais','B','C','Cis','D','Dis','E','F','Fis','G','Gis']
    #Key = "D"
    
#____ARRAY_POSITIONS_________________________________________
    frets_array = FbA.fret_positions(frets = 16, frets_0 = 44, frets_1  = 115, step_size_X = 95)
    strings_array = FbA.string_positions(strings = 6, strings_0 = 45, strings_1 = 101, step_size_Y = 56)

    print (frets_array)
    print (strings_array)

#____FRETBOARD_ARRAY_______________________ 
    board_array = HA.fret_gen(tuning, frets, strings)
    print(board_array)

#_____IMAGE_PROCESSING_____________________
    fretboard = cv2.imread(".\img\Fretboard.jpg", 1)
    for n in range(len(strings_array)):
        s = int(strings_array[n])
        for m in range(len(frets_array)):
            f = int(frets_array[m])
            note = board_array[n,m]
            cv2.circle(fretboard, (f,s), 16, (255,0,0), 4)
            cv2.circle(fretboard, (f,s), 7, (255,255,255), 14)
            cv2.putText(fretboard,note, (f-10,s+4), cv2.FONT_HERSHEY_PLAIN, 1, 0 ,0)    
    #cv2.imshow("HARMONi", fretboard)
    #cv2.waitKey(5000)
    cv2.imwrite(".\img\Generated.jpg", fretboard)
    return(fretboard)