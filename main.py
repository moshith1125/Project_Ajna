import cv2
from PIL import Image
from pytesseract import pytesseract 
from gtts import gTTS
import os

# Open the default camera
cap = cv2.VideoCapture(0)

# Wait for the camera to warm up
cv2.waitKey(1000)

# Capture a frame from the camera
ret, frame = cap.read()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Text Detection', frame)

    # Wait for key press and check if ESC is pressed
    if cv2.waitKey(1) == 32:
        break
# Check that the frame was captured successfully
if ret:
    
    # Save the frame as a PNG image
    cv2.imwrite('image.jpg', frame)

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

image = Image.open('image.jpg')
ProText = pytesseract.image_to_string(image)

# print the extracted text
print(ProText)

my_text = ProText
language = 'en'
tts = gTTS(text=my_text, lang=language, slow=False)
filename = input("Please enter a filename for your audio file: ")

# Check if the file extension is valid
valid_extensions = [".mp3", ".wav", ".ogg"]
if not any(filename.endswith(ext) for ext in valid_extensions):
    filename += ".mp3" 
# Default extension is .mp3

# Get the full path of the file
file_path = os.path.abspath(filename)
tts.save(file_path)
os.system(file_path)