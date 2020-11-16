def rgbExclusion(image, channel):
    red_img = np.array(np.zeros(image.shape), dtype='i')
    green_img = np.array(np.zeros(image.shape), dtype='i')
    blue_img = np.array(np.zeros(image.shape), dtype='i')
    red_channel = image[:,:,0]
    green_channel = image[:,:,1]
    blue_channel = image[:,:,2]
    red_img[:,:,0] = red_channel
    green_img[:,:,1] = green_channel
    blue_img[:,:,2] = blue_channel
    excluded_img = image.copy()
    if (channel == 'red'):
        excluded_img[:,:,0] = np.zeros([image.shape[0], image.shape[1]])
    elif (channel == 'green'):
        excluded_img[:,:,1] = np.zeros([image.shape[0], image.shape[1]])
    elif (channel == 'blue'):
        excluded_img[:,:,2] = np.zeros([image.shape[0], image.shape[1]])
    return  red_img, green_img, blue_img, excluded_img
