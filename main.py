import requests
from bs4 import BeautifulSoup
import sys
import os
from urllib.parse import urlparse
import random

def clean_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename.strip()

def create_folder(soup):
    try:
        header = soup.find('h1', id='article-heading_1-0')
        if not header:
            print("Header with id 'article-heading_1-0' not found. Using 'downloaded_images' as folder name.")
            folder_name = 'downloaded_images'
        else:
            folder_name = clean_filename(header.text.strip())
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")
        else:
            print(f"Using existing folder: {folder_name}")
            
        return folder_name
    except Exception as e:
        print(f"Error creating folder: {e}")
        return 'downloaded_images'
    
def download_image(image_url, filename, folder_name):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        
        ext = os.path.splitext(urlparse(image_url).path)[1]
        if not ext:
            ext = '.jpg'
        
        clean_name = clean_filename(filename)
        full_filename = os.path.join(folder_name, f"{clean_name}{ext}")
        
        with open(full_filename, 'wb') as f:
            f.write(response.content)
        print(f"Image successfully downloaded as: {full_filename}")
        return clean_name  # Return only the filename without extension
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def save_filenames_to_txt(filenames, folder_name):
    try:
        # Create three separate lists with all filenames
        first_file = filenames.copy()
        second_file = filenames.copy()
        third_file = filenames.copy()
        
        # Shuffle each list independently
        random.shuffle(first_file)
        random.shuffle(second_file)
        random.shuffle(third_file)
        
        # Save to three different files
        for index, file_list in enumerate([first_file, second_file, third_file], 1):
            txt_path = os.path.join(folder_name, f'downloaded_files_{index}.txt')
            with open(txt_path, 'w', encoding='utf-8') as f:
                for filename in file_list:
                    f.write(f"{filename}\n")
            print(f"Filenames saved to: {txt_path}")
    except Exception as e:
        print(f"Error saving filenames to txt: {e}")
        
def scrape_webpage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        folder_name = create_folder(soup)
        downloaded_files = []  # Array to store successful downloads
        
        i = 1
        while True:
            div_id = f'list-sc-item__content_{i}-0'
            main_div = soup.find('div', id=div_id)
            
            if not main_div:
                print(f"\nNo more divs found after {i-1} iterations.")
                break
                
            print(f"\nProcessing div #{i}: {div_id}")
            
            img_placeholder = main_div.find('div', class_='img-placeholder')
            image_url = None
            
            if img_placeholder:
                img_tag = img_placeholder.find('img')
                if img_tag and img_tag.get('data-src'):
                    image_url = img_tag['data-src']
            
            if not image_url:
                embedded_media = main_div.find('a', class_='EmbeddedMedia')
                if embedded_media:
                    img_tag = embedded_media.find('img', class_='EmbeddedMediaImage')
                    if img_tag and img_tag.get('src'):
                        image_url = img_tag['src']
            
            if image_url:
                heading_span = main_div.find('span', class_='mntl-sc-block-heading__text')
                if heading_span:
                    filename = heading_span.text.strip()
                    print(f"Found image URL: {image_url}")
                    print(f"Using filename: {filename}")
                    downloaded_file = download_image(image_url, filename, folder_name)
                    if downloaded_file:  # If download was successful
                        downloaded_files.append(downloaded_file)
                else:
                    print(f"Heading text not found in div #{i}")
            else:
                print(f"Image not found in div #{i} (checked both img-placeholder and EmbeddedMedia)")
            
            i += 1

        # After all downloads are complete, save filenames to txt files
        if downloaded_files:
            save_filenames_to_txt(downloaded_files, folder_name)
        else:
            print("\nNo files were downloaded successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Please enter the URL to scrape: ")
    
    scrape_webpage(url)

if __name__ == "__main__":
    main()