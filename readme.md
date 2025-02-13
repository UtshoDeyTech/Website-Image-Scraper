# Byrdie Website Image Scraper

A Python script to automatically download images from Byrdie articles and create organized collections with randomized lists.

## Description

This tool is designed to scrape images from Byrdie article pages, automatically creating folders and downloading images while maintaining the original article structure. It also generates three text files containing randomized lists of the downloaded images.

## Getting Started

### Dependencies

* Python 3.6 or higher
* Required Python packages:
  * requests
  * beautifulsoup4

### Installing

* Clone the repository
```bash
git clone git@github.com:UtshoDeyTech/Website-Image-Scraper.git
```

* Create a virtual environment
```bash
python -m venv env
```

* Activate the virtual environment
```bash
# On Windows:
env\Scripts\activate

# On Unix or MacOS:
source env/bin/activate
```

* Install the required packages
```bash
pip install requests beautifulsoup4
```

### Creating Executable

* Install PyInstaller
```bash
pip install pyinstaller
```

* Create the executable
```bash
pyinstaller --onefile main.py
```

### Usage

#### Running with Python
```bash
python main.py
```

#### Running the Executable
* Double-click the `ImageScraper.exe` file
* When prompted, enter the Byrdie article URL
* Wait for the download process to complete

### Output Structure

```
Article_Title/
├── Image1.jpg
├── Image2.jpg
├── Image3.jpg
├── downloaded_files_1.txt
├── downloaded_files_2.txt
└── downloaded_files_3.txt
```

* Images are saved with their section heading names
* Three text files are generated, each containing all image names in different random orders

## Features

* Automatic folder creation based on article title
* Downloads images with meaningful names based on article sections
* Handles both standard images and embedded media
* Generates three randomized lists of downloaded images
* User-friendly command-line interface
* Error handling for network and file system operations

## Error Handling

The script includes error handling for:
* Invalid URLs
* Network connection issues
* Missing images or content
* File system operations

## Version History

* 0.1
    * Initial Release
    * Basic scraping functionality
    * Image downloading
    * Text file generation

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Help

Common issues and their solutions:

* If the script fails to download images, check your internet connection
* If folder creation fails, ensure you have write permissions in the directory
* If the executable doesn't run, try running it as administrator

## Authors

Utsho Dey
[@github](https://github.com/utshodeytech)

## Acknowledgments

* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests Library](https://requests.readthedocs.io/en/master/)
* [PyInstaller](https://www.pyinstaller.org/)
