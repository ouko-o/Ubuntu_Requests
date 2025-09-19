Ubuntu-Inspired Image Fetcher 🖼️

"I am because we are" – Ubuntu Philosophy

This project is a Python-based image fetcher inspired by the Ubuntu principles of community, respect, sharing, and practicality.
It allows users to download images from the web, store them in an organized directory, and handle errors gracefully.

✨ Features

✅ Fetches images from one or more URLs

✅ Creates a Fetched_Images directory if it does not exist

✅ Extracts filenames automatically from URLs (fallback: downloaded_image.jpg)

✅ Saves images in binary mode for proper storage

✅ Handles network errors gracefully (no crashes)

✅ Checks HTTP headers (Content-Type) to ensure files are valid images

✅ Prevents duplicate downloads using MD5 hashing

✅ Encourages mindful use of shared resources, aligned with Ubuntu values

🛠️ Requirements

Python 3.x

Libraries:

requests

Install dependencies:

pip install requests

🚀 Usage

Run the script:

python ubuntu_image_fetcher.py


You will see:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web


Enter one or more image URLs (separated by commas):

Please enter one or more image URLs (separated by commas): 
https://example.com/ubuntu-wallpaper.jpg, https://example.com/logo.png


Example Output:

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ Successfully fetched: logo.png
✓ Image saved to Fetched_Images/logo.png

Connection strengthened. Community enriched.
