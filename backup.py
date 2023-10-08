import shutil

source = r"C:\Users\danie\Documents\pythonvired\requirements.txt"

destination = r"C:\Users\danie\Documents\flaskvired"

try:
    shutil.copy(source,destination)
    print("File copied successfully")

except:
    print("error occured while copying")