import os


pathFiles = os.getcwd()




for root, dirs, files in os.walk(pathFiles):
    for name in files:
        if name.upper().endswith(".PDF"):
            print(os.path.join(root, name))
            # open file
            













