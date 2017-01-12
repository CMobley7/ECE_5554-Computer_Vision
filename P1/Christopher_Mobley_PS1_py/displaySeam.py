# from energy_image import energy_image
# from cumulative_minimum_energy_map import cumulative_minimum_energy_map
# from find_optimal_vertical_seam import find_optimal_vertical_seam
# from find_optimal_horizontal_seam import find_optimal_horizontal_seam
# from scipy.misc import imread

def displaySeam(im,seam,type):
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

# displaySeam('inputSeamCarvingPrague.jpg',find_optimal_vertical_seam(cumulative_minimum_energy_map(energy_image(imread('inputSeamCarvingPrague.jpg')), 'VERTICAL')),'VERTICAL')
# displaySeam('inputSeamCarvingPrague.jpg',find_optimal_horizontal_seam(cumulative_minimum_energy_map(energy_image(imread('inputSeamCarvingPrague.jpg')), 'HORIZONTAL')),'HORIZONTAL')