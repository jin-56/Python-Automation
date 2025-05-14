import os
import shutil

#define dictonary of directories and it's accepted extension
directories = {
  "music" : ["mp3","aac","wav"],
  "videos" : ["mp4" "mkv","mov"],
  "images" : ["jpg","jpeg","png"],
  "scripts" : ["py","html"]
}

excep =["organier.py"]
#create dictonaries
for directory in directories:
  os.makedirs(directory,exist_ok=True)

#list our files
files = os.listdir()

#move each files to its respective directories     done
#how to identify if it is a file      done
#how to identify extension
#where does this extension file belongs
#how to move 


for file in files:
  if os.path.isfile(file) and file not in excep:
    extension = file.split(".")[-1]
   #print(extension)
    for folder,extensions in directories.items():
     if extension in extensions:
       shutil.move(file,folder)
       
       
      
