import glob, os, shutil

x = range(1, 104) # adjust range number of gernerated folders
for i in x:
    source_dir = 'C:/Users/sieczaa/Desktop/Restored/recup_dir.'+str(i) #localization of restored folders
    dst = 'C:/Users/sieczaa/Desktop/Restored/Pictures' #desitnation where to move files 
    files = glob.iglob(os.path.join(source_dir, "*.jpeg")) #extension which search to, works with every extension
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dst)
