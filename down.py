import urllib.request
import os


urlPilar = "http://vriunap.pe/repositor/docs/d{:08d}-Proy.pdf"
initialRange = 0
endRange = 90_000

currentPath = os.getcwd()


for i in range(initialRange, endRange):
    try:
        # print(f"downlodin {i}")
        iUrl = urlPilar.format(i)
        iFile = os.path.join(currentPath, "d{:08d}-Proy.pdf".format(i))
        # print(iUrl)
        print(iFile)
        urllib.request.urlretrieve(iUrl, iFile)
    except Exception as e:
        print(e)



