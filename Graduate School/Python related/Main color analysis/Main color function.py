#%%
import colour
import numpy as np
def get_main_color(R,G,B):
    sRGB = [R/255,G/255,B/255]
    RGB = np.array(sRGB)
    XYZ = colour.sRGB_to_XYZ(sRGB)
    Lab = colour.XYZ_to_Lab(XYZ)
    LCHab = colour.Lab_to_LCHab(Lab)
    L = int(LCHab[0]);C = int(LCHab[1]);ab = int(LCHab[2])
    print([L,C,ab])
    if C<40:# 1
        if L<10:
            return 'black'
        elif L>90:
            return 'white'
        else:
            return 'gray'
    elif ab<45:# 2
        if L<30:
            return 'brown'
        elif L>70:
            return 'pink'
        else:
            return 'red'
    elif ab<75:# 3
        if L<30:
            return 'brown'
        else:
            return 'orange'
    elif ab<105:# 4
        return 'yellow'
    elif ab<210:# 5
        return 'green'
    elif ab<315:# 6
        return 'blue'
    elif ab>330:# 7
        if L>50:
            return 'pink'
        else:
            return 'purple'
    else:
        return 'purple'
get_main_color(5,5,5)
#%%