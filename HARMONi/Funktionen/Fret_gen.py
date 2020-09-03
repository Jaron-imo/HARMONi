import cv2
import numpy as np

def fret_generator(tuning, frets, strings):
    tones = ['A','Ais','B','C','Cis','D','Dis','E','F','Fis','G','Gis']
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
