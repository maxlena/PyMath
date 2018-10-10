
def import_all():
    import sys
    import os

    
# Extract Method is not working

def download_data():
    import requests
    import zipfile
    import shutil, os

    # Download data; save as CSV
    request = requests.get("https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U")
    with open("survey2018.zip", "wb") as file:
        file.write(request.content)

    ## Extract ZIP to Folder
    with zipfile.ZipFile("survey2018.zip") as zip:
        zip.extractall("survey2018")

    ## Move CSV to patent folder; delete Folder and Zip
    shutil.move("survey2018/survey_results_public.csv", "survey2018.csv")
    shutil.rmtree("survey2018")
    os.remove("survey2018.zip")

download_data()

