tb = ((225, 225, 225), (235, 193, 0), (223, 105, 5))
tv = ((240, 240, 240), (245, 203, 5), (233, 115, 15))

def fCheckBandage(renkDemeti):

    bandage = False
    #renkDemeti[0] = r , renkDemeti[1] = g , renkDemeti[2] = b
    
    if (renkDemeti[1] >= tb[0][1] and renkDemeti[1] <= tv[0][1]):   # item 0 g
        if (renkDemeti[0] >= tb[0][0] and renkDemeti[0] <= tv[0][0]) and (renkDemeti[2] >= tb[0][2] and renkDemeti[2] <= tv[0][2]):
            bandage = True
        else:
            bandage = False

    elif (renkDemeti[1] >= tb[1][1] and renkDemeti[1] <= tv[1][1]): # item 1 g
        if (renkDemeti[0] >= tb[1][0] and renkDemeti[0] <= tv[1][0]) and (renkDemeti[2] >= tb[1][2] and renkDemeti[2] <= tv[1][2]):
            bandage = True
        else:
            bandage = False

    elif (renkDemeti[1] >= tb[2][1] and renkDemeti[1] <= tv[2][1]): # item 2 g
        if (renkDemeti[0] >= tb[2][0] and renkDemeti[0] <= tv[2][0]) and (renkDemeti[2] >= tb[2][2] and renkDemeti[2] <= tv[2][2]):
            bandage = True
        else:
            bandage = False

    else:
        bandage = False

    return bandage

print(fCheckBandage((238,194,4)))