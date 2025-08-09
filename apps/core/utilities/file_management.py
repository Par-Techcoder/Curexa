import os
import hashlib
from django.conf import settings

def save_uploaded_file(uploaded_file, subfolder=""):
    """
    Saves an uploaded file to a designated subfolder under static/images
    If subfolder is not provided (or empty), the file is saved directly under /static/images/.
    
    Args:
        uploaded_file: In-memory uploaded file.
        subfolder (str): The folder name where the file will be saved.
    
    Returns:
        str: The relative URL path to the saved file.
    """
    if not uploaded_file:
        return ''

    # Determine the target directory based on whether a subfolder is provided.
    if subfolder:
        target_dir = os.path.join(settings.BASE_DIR, 'static', 'images', subfolder)
    else:
        target_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Generate an MD5 hash for the file content.
    md5_hash = hashlib.md5()
    for chunk in uploaded_file.chunks():
        md5_hash.update(chunk)
    file_hash = md5_hash.hexdigest()

    # Get file extension and create a new file name.
    _, ext = os.path.splitext(uploaded_file.name)
    new_file_name = f"{file_hash}{ext}"
    file_path = os.path.join(target_dir, new_file_name)

    # Write file if it doesn't exist yet.
    if not os.path.exists(file_path):
        uploaded_file.seek(0)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

    # Return the relative path for use in your models or templates.
    if subfolder:
        return f'/static/images/{subfolder}/{new_file_name}'
    else:
        return f'/static/images/{new_file_name}'
