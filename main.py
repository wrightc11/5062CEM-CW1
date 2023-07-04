from PIL import Image
import cv2
import numpy as np

def text_to_binary(text):
    # Convert text to binary representation
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary


def encode_text_in_image(image_path, text):
    # Open the image
    image = Image.open(image_path).convert("RGB")

    # Convert text to binary
    binary_text = text_to_binary(text)

    # Check if the image has enough capacity to hold the text
    pixel_count = image.width * image.height
    required_pixels = len(binary_text)
    if required_pixels > pixel_count:
        raise ValueError("Image does not have enough capacity to hold the text.")

    # Iterate over each pixel and encode the text
    encoded_pixels = []
    binary_index = 0
    for pixel in image.getdata():
        # Convert the pixel values to a list
        r, g, b = list(pixel)

        # Modify the least significant bit of each channel
        if binary_index < required_pixels:
            r = (r & 0xFE) | int(binary_text[binary_index])
            binary_index += 1
        if binary_index < required_pixels:
            g = (g & 0xFE) | int(binary_text[binary_index])
            binary_index += 1
        if binary_index < required_pixels:
            b = (b & 0xFE) | int(binary_text[binary_index])
            binary_index += 1

        # Append the modified pixel to the encoded pixels list
        encoded_pixels.append((r, g, b))

    # Update the image with the encoded text
    encoded_image = Image.new("RGB", image.size)
    encoded_image.putdata(encoded_pixels)

    # Save the encoded image as a separate copy
    encoded_image_path = image_path.split(".")[0] + "_encoded.jpg"
    encoded_image.save(encoded_image_path)
    print("Text encoded successfully in the image:", encoded_image_path)


def lsb_analysis(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Extract the blue channel as it contains the LSBs
    blue_channel = image[:, :, 0]

    # Extract the LSBs by applying a bitwise AND operation with 1
    lsb_bits = np.bitwise_and(blue_channel, 1)

    # Reshape the array to a 1D vector
    lsb_bits = lsb_bits.flatten()

    # Check if the LSBs are altered
    if np.any(lsb_bits):
        print("Image has been tampered with (LSBs altered).")
    else:
        print("Image is intact (LSBs not altered).")


# Main program
image_path = input("Enter the path to the image file: ")  # Path to the image file
text = input("Enter the text to be encoded: ")  # Text to be encoded

# Encode text in the image
encode_text_in_image(image_path, text)

# Perform LSB analysis on the image
lsb_analysis(image_path)
