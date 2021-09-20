import os
import shutil

# Download_folder = "C:\\Users\XXXX\\XXXX\" username

ext_text = ['.docx', '.txt', '.doc', '.pdf', '.pptx', '.xlsx']
ext_compress = ['.zip', '.rar']
ext_img = ['.png','.jpg', '.jpeg', '.gif', '.svg']
ext_vid = ['.mp4', '.mov', '.webm' ]


for f in os.listdir(Download_folder):
    filename, file_ext = os.path.splitext(f)


    try:
        if not file_ext:
            pass

       #Match the Foldernames 
        elif file_ext in (ext_compress):
            shutil.move(
                os.path.join(Download_folder, f'{filename}{file_ext}'),
                os.path.join(Download_folder, 'Archivos rar', f'{filename}{file_ext}'))
       
       
        elif file_ext in (ext_img):
            shutil.move(
                os.path.join(Download_folder, f'{filename}{file_ext}'),
                os.path.join(Download_folder, 'Imagenes', f'{filename}{file_ext}'))
        
      
        elif file_ext in (ext_text):
            shutil.move(
                os.path.join(Download_folder, f'{filename}{file_ext}'),
                os.path.join(Download_folder, 'Archivos doc', f'{filename}{file_ext}'))
        
        elif file_ext in (ext_vid):
            shutil.move(
                os.path.join(Download_folder, f'{filename}{file_ext}'),
                os.path.join(Download_folder, 'Videos', f'{filename}{file_ext}'))

        else:
            shutil.move(
                os.path.join(Download_folder, f'{filename}{file_ext}'),
                os.path.join(Download_folder, 'Otros', f'{filename}{file_ext}'))                        

    except (FileNotFoundError, PermissionError)        :
        pass