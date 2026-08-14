from PIL import Image
import numpy as np

###creates a vertical slice of an image:)
def slice_vertically(im,start,warstwa):
    vert_list = []
    for j in range(start,warstwa): ###from all the horizontal layers
        vert_slice = []
        for i in range(len(im)): ###add
            vert_slice.append(im[i][j])
        vert_list.append(vert_slice)
    return vert_list

def connect_slices(slices): ###used to connect the slices back, creates a fragment of an image
    transposed_slices_list = []
    for i in range(len(slices)): 
        transposed_slices_list.append([]) ### we prep by appending as many empty lists as we have rows             

    for row in range(len(slices[0])):
        for bit in range(len(slices)):
            transposed_slices_list[bit].append(slices[bit][row])
    transposed_slices_list = np.array(transposed_slices_list)
    rec = Image.fromarray(transposed_slices_list)
    return(np.rot90(np.fliplr(rec)))

def is_space(slice): ###must get vertical slices!!!! checks for space between letters
    if 0 in slice:
        return False
    else:
        return True

def separate_letters(image):
    to_ret = []
    sliced_im = slice_vertically(image,0,len(image[0])) ## funkcja dostaje kawalki ktore nie sa jeszcze pociete!!! dlatego dopiero im[0] daje dlugosc zdjecia
    warstwa_count = -1 ###koniec przekazanego obrazu
    last_cut = 0 ###poczatek przekazanego obrazu
    can_cut = False
    for warstwa in sliced_im: ### przeszukujac warstwy
        warstwa_count = warstwa_count + 1 #### zwieksz koniec do zespolenia potem
        space = is_space(warstwa)
        if space and can_cut: ### jesli znajdzie spacje
            to_ret.append((connect_slices(slice_vertically(image,last_cut,warstwa_count)))) ###przekaz obraz od poczatku do konca
            last_cut = warstwa_count ###zupdateuj poczatek
            can_cut = False
        elif space == True and can_cut == False:
            last_cut = warstwa_count + 1
        else:
            can_cut = True
    return to_ret