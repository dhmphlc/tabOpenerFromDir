import os
import webbrowser
import time

folder_path = "path/to/the/folder/where/you/have/files"

print("Tab opening started:")

for filename in os.listdir(folder_path):
    # Get the full path of the file
    ffile_path = os.path.join(folder_path, filename)
        
    query = filename[:-4] # remove the ".txt" extension
    print(query)
    url = f"https://www.google.com/search?q={query}"
    # Open the file in a browser tab
    webbrowser.open_new_tab(url)
    time.sleep(5)

print("Tab opening finished.")