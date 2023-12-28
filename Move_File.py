import os
import shutil


from_dir = "C:/Users/ACER/Desktop/Document_Files"  
to_dir = "C:/Users/ACER/Downloads" 


list_of_files = os.listdir(from_dir)

# Print the list of files
print("List of files in the source path:")
print(list_of_files)


for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    print(f"File Name: {name}, Extension: {extension}")




for file_name in list_of_files:
 
    source_path = os.path.join(from_dir, file_name)
    destination_path = os.path.join(to_dir, file_name)

 
    shutil.move(source_path, destination_path)

print("Files moved successfully!")

