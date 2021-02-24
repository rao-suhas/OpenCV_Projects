# -*- coding: utf-8 -*-
import cv2
import numpy as np

def motion_blur(image, axis=90, kernel_size=15):
    
    '''
    This function takes an input image, orientation of blur & kernel size
    Applies a custom kernel on image, made from the input arguments &
    Returns the motion blurred image
    Note:
        Vertical : 90
        Horizontal : 0
        Diagonal : 45
    '''
    
    size = (kernel_size, kernel_size)
    blur_img = None
    
    if axis == 90:
        # Initialize vertical kernel
        kernel_v = np.zeros(size)
        # Fill the middle row of the kernels
        kernel_v[:, int((kernel_size-1)/2)] = np.ones(kernel_size)
        # Normalize the kernels
        kernel_v /= kernel_size
        kernel = kernel_v
        # Apply custom motion blur filter
        blur_img = cv2.filter2D(image, -1, kernel)
    elif axis == 0:
        # Initialize horizontal kernel
        kernel_h = np.zeros(size)
        # Fill the middle row of the kernels
        kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)
        # Normalize the kernels
        kernel_h /= kernel_size        
        kernel = kernel_h
        # Apply custom motion blur filter
        blur_img = cv2.filter2D(image, -1, kernel)
    elif axis == 45:
        # Diagonal motion blur
        kernel_diag = np.flipud(np.eye(kernel_size))
        kernel_diag /= kernel_size
        kernel = kernel_diag
        # Apply custom motion blur filter
        blur_img = cv2.filter2D(image, -1, kernel)
    
    return blur_img
    
    


# Load the image
image = cv2.imread('test_test.png')

# Copy the image
img_copy = np.copy(image)

# Call the custom made motion blur function
blur_img = motion_blur(img_copy, axis=90)

# Display original and blurred images side by side
cv2.imshow("image comparison", np.hstack((img_copy, blur_img)))

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
