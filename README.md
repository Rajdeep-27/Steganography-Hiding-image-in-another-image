# Steganography-Hiding-image-in-another-image
Python code to hide an image in another and also extract the hidden image from the merged image which was generated.
# Environment
Linux
# Requirements
1. Python3
2. OpenCV

# Description
The source code contains two subroutines: to merge two images and to extract the hidden image from the merged output.

1. To merge the images type the following on terminal
$python3 steganography.py -m img1.png,img2.png,img3.png
img1.png: name(with proper path) of the image in which img2.png will be hidden
img2.png: name(with proper path) of the image to be hidden
img3.png: specify the name which you want to give to the output

2. To extract type the following on terminal
$python3 steganography.py -e img3.png,img4.png
img3.png: input image(merged output of two images)
img4.png: specify the name which you want to give to the extracted output image(which was hidden while merging)

# Note:
for '.png' images only.


