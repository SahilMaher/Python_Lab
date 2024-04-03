import zipfile
import os
op=input("Enter Operation 1.Zip \n 2.unZip")


def zip_file(file_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))

def unzip_file(zip_name, extract_to):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)



if(op=='zip'):
    filename=input("enter File Name")
    file_to_zip = filename
    zip_file(file_to_zip, filename)
    print(f"{file_to_zip} has been zipped to {filename}")



if(op=='unzip'):
    file2=input("enterFile name with (.zip)")
    
    zipped_file = fil

    extract_to_directory = 'unzipped_files'
    os.makedirs(extract_to_directory, exist_ok=True)
    unzip_file(zipped_file, extract_to_directory)
    print(f"{zipped_file} has been unzipped to {extract_to_directory}")
