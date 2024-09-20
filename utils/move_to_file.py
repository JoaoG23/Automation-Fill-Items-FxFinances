import os

def move_to_file(source, destination):
    try:
        os.rename(source, destination)

        print(f"File moved from {source} to {destination}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
        