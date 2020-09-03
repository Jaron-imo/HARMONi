# generates an array with the coordinates of the dots on the fretboard image

import numpy as np

def fret_positions(frets, frets_0, frets_1, step_size_X):
    
    frets_array = np.zeros([frets])

    frets_array[0] = frets_0
    frets_array[1] = frets_1

    for n in range(2,frets):
        frets_array[n] = frets_array[n-1] + step_size_X

    return(frets_array)

def string_positions(strings, strings_0, strings_1, step_size_Y):

    strings_array = np.zeros([strings])
    strings_array_flip = np.zeros([strings])

    strings_array[0] = strings_0
    strings_array[1] = strings_1

    for n in range(2,strings):
        strings_array[n] = strings_array[n-1] + step_size_Y

    for n in range(len(strings_array)): #Flip the Array, so Strings start from bottom
        strings_array_flip[n] = strings_array[(len(strings_array)-n)-1]

    return(strings_array_flip)
