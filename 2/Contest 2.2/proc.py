import cv2

# Load the grayscale image
image = cv2.imread("400.png", cv2.IMREAD_GRAYSCALE)

# Convert the image to a list of pixel brightness values
pixel_values = image.flatten().tolist()

# Print the first 10 pixel values as an example
with open("output.txt", "w") as my_file:
    my_file.write(str(pixel_values))