import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup
import base64
import os

# Heroku API URL and API Key
HEROKU_API_URL = 'https://api.heroku.com'
HEROKU_API_KEY = 'HRKU-acfde531-3007-468b-be5d-10ba7233cfe5'

def extract_text_from_image(image_path):
    return "Sample extracted text from image."

def segment_visual_elements(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    visual_elements = []
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        visual_element = image[y:y+h, x:x+w]
        element_path = f'visual_element_{i}.png'
        cv2.imwrite(element_path, visual_element)
        visual_elements.append(element_path)
    
    return visual_elements

def generate_html(text_content, visual_elements):
    soup = BeautifulSoup('<html><head><title>Extracted Content</title><style>body {font-family: Arial, sans-serif; margin: 0; padding: 20px;} .content {margin-bottom: 40px;} .text-container {white-space: nowrap;} .text {display: inline-block; font-size: 24px; line-height: 1.6; margin-right: 20px;} .visual {margin-bottom: 20px;} .visual img {max-width: 100%; height: auto;}</style></head><body></body></html>', 'html.parser')
    body = soup.body
    
    div_text = soup.new_tag('div', **{'class': 'content text-container'})
    for text in text_content.split('\n'):
        if text.strip():  
            p_text = soup.new_tag('p', **{'class': 'text'})
            p_text.string = text
            div_text.append(p_text)
    body.append(div_text)
    
    for element_path in visual_elements:
        div_visual = soup.new_tag('div', **{'class': 'content visual'})
        img = soup.new_tag('img', src=element_path)
        div_visual.append(img)
        body.append(div_visual)

    with open('output.html', 'w') as file:
        file.write(str(soup))


def list_heroku_apps():
    url = f"{HEROKU_API_URL}/apps"
    headers = {
        'Authorization': f'Bearer {HEROKU_API_KEY}',
        'Accept': 'application/vnd.heroku+json; version=3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        apps = response.json()
        for app in apps:
            print(f"App Name: {app['name']}")
    else:
        print(f"Failed to retrieve apps: {response.status_code}")
        print(response.text)

def main(image_path):
    try:
        text_content = extract_text_from_image(image_path)
        visual_elements = segment_visual_elements(image_path)
        generate_html(text_content, visual_elements)
        
        print("HTML file generated successfully as 'output.html'")
        list_heroku_apps()
        
    except Exception as e:
        print(f"An error occurred: {e}")

image_path = r'C:\Users\DELL\images.jpg'    #path of image stored locally on a desktop
main(image_path)