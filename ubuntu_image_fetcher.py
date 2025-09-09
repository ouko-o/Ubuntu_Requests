"""
Ubuntu-Inspired Image Fetcher

Description:
    A Python program that fetches images from the internet and saves them locally,
    inspired by Ubuntu principles of community, respect, and sharing.
"""

import requests
import os
from urllib.parse import urlparse


def fetch_image(url: str) -> None:
    """
    Fetches an image from a given URL and saves it into the 'Fetched_Images' directory.

    Args:
        url (str): The image URL provided by the user.

    Returns:
        None
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image with a timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename found, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error: {e}")
    except requests.exceptions.ConnectionError:
        print("✗ Connection error: Unable to connect to the internet.")
    except requests.exceptions.Timeout:
        print("✗ Timeout error: The request took too long.")
    except requests.exceptions.RequestException as e:
        print(f"✗ Request failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get image URL from user
    url = input("Please enter the image URL: ").strip()

    if url:
        fetch_image(url)
        print("\nConnection strengthened. Community enriched.")
    else:
        print("✗ No URL entered. Please try again.")


if __name__ == "__main__":
    main()
