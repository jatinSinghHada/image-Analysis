Image Content Extraction Project
This project extracts text and visual elements from an image, generates an HTML file containing the extracted content, and lists Heroku applications associated with a provided API key.

Prerequisites
Python: Ensure you have Python installed on your system. You can download it from python.org.

Tesseract OCR: Install Tesseract OCR. You can download it. Make sure to note the installation path as you'll need it later.

Required Python Packages: Install the necessary Python packages using pip. You can do this by running the following command in your terminal or command prompt:

sh
Copy code
pip install opencv-python numpy requests beautifulsoup4 pytesseract
Steps to Use the Project
Clone the Repository:

Open your command prompt or terminal.
Navigate to the directory where you want to clone the repository.
Run the following command:
sh
Copy code
git clone <repository_url>
Replace <repository_url> with the URL of your GitHub repository.
Navigate to the Project Directory:

sh
Copy code
cd <repository_name>
Replace <repository_name> with the name of the cloned repository.

Set the Tesseract Path:

Open the image_content_extraction.py file in a text editor.
Locate the following line:
python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Ensure the path matches the installation path of Tesseract OCR on your system.
Set the Image Path:

Ensure the image_path variable points to a valid image file on your system:
python
Copy code
image_path = r'C:\path\to\your\image.png'
Update this path to the location of your image file.
Run the Script:

In your command prompt or terminal, execute the following command:
sh
Copy code
python image_content_extraction.py
Expected Output
The script will extract text and visual elements from the specified image.
An HTML file named output.html will be generated in the project directory containing the extracted content.
The script will list Heroku applications associated with the provided API key in the command prompt or terminal.
Troubleshooting
File Not Found Error: Ensure the paths to the Tesseract executable and the image file are correct.
Module Not Found Error: Make sure all required Python packages are installed. Re-run the pip install command if necessary.
Heroku API Key Error: Ensure the Heroku API key is valid and has the necessary permissions.
Additional Notes
The Tesseract executable path should be correctly set according to your system's installation directory.
The image file should be a valid image format supported by OpenCV (e.g., PNG, JPG).
The Heroku API key should be kept confidential and not shared publicly.
