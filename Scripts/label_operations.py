import os

def count_files(directory):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        return 0
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def delete_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(directory)
total = 0 

def check_and_delete(directory, minimum_files):
    global total
    deleted_subdirectories = []
    retained_subdirectories = []

    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            file_count = count_files(subdir_path)
            if file_count < minimum_files:
                delete_directory(subdir_path)
                deleted_subdirectories.append((subdir_path, file_count))
            else:
                retained_subdirectories.append((subdir_path, file_count))
    
    print("Deleted subdirectories:")
    for subdir, file_count in deleted_subdirectories:
        print(f"{subdir} (File Count: {file_count})")
    
    print("Retained subdirectories:")
    for subdir, file_count in retained_subdirectories:
        print(f"{subdir} (File Count: {file_count})")
        total = total + file_count

# Example usage
directory_path = "E:/June/temp/test"
minimum_files = 20

check_and_delete(directory_path, minimum_files)

print("total retained files : " , total)
