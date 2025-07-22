import cv2 
import os

# Define the path to your ASL dataset
dataset_folder = "Data"

# Get a list of subdirectories (each subdirectory represents a different ASL sign)
sign_folders = os.listdir(dataset_folder)

for sign_folder in sign_folders:
    sign_path = os.path.join(dataset_folder, sign_folder)
    
    # Iterate through images in the sign folder
    for img_name in os.listdir(sign_path):
        img_path = os.path.join(sign_path, img_name)
        
        # Read the image
        img = cv2.imread(img_path)
        
        # Process the image if needed (e.g., resizing, normalization, etc.)
        # ...
        
        # Display or save the processed image if desired
        cv2.imshow("Processed Image", img)
        cv2.waitKey(0)

cv2.destroyAllWindows()
