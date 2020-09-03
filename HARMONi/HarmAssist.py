# Takes Key and creates array with the all tones on the fretboard

import numpy as np

tones = ['A','Ais','B','C','Cis','D','Dis','E','F','Fis','G','Gis']

Steps = [0, 2, 4, 5, 7, 9, 11]
Steps_pent = [0, 2,  4, 7, 9]

def fret_gen (tuning, frets, strings):
    board_array = np.empty((strings, frets), dtype=object)
    board_array[:] = 'x'

    for s in range (strings):
        off1 = tones.index(tuning[s])
 
        for f in range (frets):
        
            off2 = off1 + f
     
            if off2 >= len(tones):
                off2 = off2 - (len(tones)*(off2//len(tones)))

            board_array[s,f] = tones[off2]
    return board_array

def scale_gen(Key):
    Key_index = tones.index(Key)
    tones_transp = []
    Scale = []
    index = 0
    #____TRANSPOSE "TONES"__________________________________
    for n in range(len(tones)):
        index = n + Key_index

        if index >= len(tones):
            index = index - len(tones)

        tones_transp.append(tones[index])
    #____SCALE_______________________________________________
    for n in range(len(Steps)):
        Scale.append(tones_transp[Steps[n]])
    return (Scale)

def penta_gen(Key):
    Steps = [0, 2, 4, 5, 7, 9, 11]
    Key_index = tones.index(Key)
    tones_transp = []
    Penta = []
    index = 0
    #____TRANSPOSE "TONES"__________________________________
    for n in range(len(tones)):
        index = n + Key_index

        if index >= len(tones):
            index = index - len(tones)

        tones_transp.append(tones[index])
        #____PENTATONIC_______________________________________________
    for n in range(len(Steps_pent)):
        Penta.append(tones_transp[Steps_pent[n]])
    
    return (Penta)