import re
import base64
import os

# File paths
DOC_PATH = r"c:\GCP\Google-Gen-AI-Capstone-Project\TravelPlannerAgent\TECHNICAL_DOCUMENTATION.md"
SCREENSHOTS_DIR = r"c:\GCP\Google-Gen-AI-Capstone-Project\TravelPlannerAgent\output_screenshots"

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

import urllib.parse

def replace_images_with_base64(match):
    alt_text = match.group(1)
    image_url = match.group(2)
    
    # Extract filename from URL (handle both file:/// and relative paths)
    if image_url.startswith("file:///"):
        filename = os.path.basename(image_url)
    elif "output_screenshots" in image_url:
        filename = os.path.basename(image_url)
    else:
        return match.group(0) # Skip if not recognized
    
    # Decode URL encoding (e.g., %20 -> space)
    filename = urllib.parse.unquote(filename)
        
    image_path = os.path.join(SCREENSHOTS_DIR, filename)
    
    if not os.path.exists(image_path):
        # Try adding .png if missing (as seen in one error)
        if os.path.exists(image_path + ".png"):
            image_path += ".png"
        else:
            print(f"Warning: Image file not found: {image_path}")
            return match.group(0)
        
    print(f"Embedding {filename}...")
    base64_str = image_to_base64(image_path)
    return f"![{alt_text}](data:image/png;base64,{base64_str})"

try:
    with open(DOC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to find markdown images: ![alt](url)
    # Updated to handle parentheses in filenames by matching until .png)
    new_content = re.sub(r'!\[(.*?)\]\((.*?\.png)\)', replace_images_with_base64, content)

    with open(DOC_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully embedded images as base64.")

except Exception as e:
    print(f"Error: {e}")
