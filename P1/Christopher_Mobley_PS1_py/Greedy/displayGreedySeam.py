# from energy_image import energy_image
# from find_greedy_vertical_seam import find_greedy_vertical_seam
# from find_greedy_horizontal_seam import find_greedy_horizontal_seam
# from scipy.misc import imread

def displayGreedySeam(im,seam,type):
    from scipy.misc import imread
    import matplotlib.pyplot as plot

    input_color_image = imread(im)
    nth_row, nth_column = input_color_image.shape[0], input_color_image.shape[1]

    plot.imshow(input_color_image)

    if type == 'VERTICAL':
        plot.plot(seam, xrange(0, nth_row),'r')
    elif type == 'HORIZONTAL':
        plot.plot(xrange(0, nth_column), seam, 'r')
    else:
        print("Invalid seamDirection. The valid inputs for seamDirection are HORIZONTAL or VERTICAL.")
    plot.show()

# displayGreedySeam('inputSeamCarvingPrague.jpg',find_greedy_vertical_seam(energy_image(imread('inputSeamCarvingPrague.jpg'))),'VERTICAL')
# displayGreedySeam('inputSeamCarvingPrague.jpg',find_greedy_horizontal_seam(energy_image(imread('inputSeamCarvingPrague.jpg'))), 'HORIZONTAL')