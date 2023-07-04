# 5062CEM-CW1

This Code uses image steganography by encoding text into an image using the least significant bit (LSB) technique by iterating over the RGB Values. It also provides a method to analyze an image for tampering using LSB analysis.

---------------------

- Python 3
- PIL
- OpenCV
- NumPy
------------------

follow these steps to utilise this code:

1. Place the image file you want to use for encoding in the same directory as the cocde.
3. Enter the path to the image file when prompted.
4. Enter the text you want to encode into the image.
5. The script will encode the text into the image using the LSB technique and save the encoded image as a separate copy with "_encoded" appended to the filename.
6. The script automatically analyse's this new file for any changes to the LSB values to see if it has been tampered with.

