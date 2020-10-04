import urllib.request
import os

urlPilarBorrador = "https://vriunap.pe/repositor/docs/d00004111-Borr.pdf"
urlPilarBorrador = "https://vriunap.pe/repositor/docs/d{:08d}-Borr.pdf"
urlConstancias = "https://vriunap.pe/repositor/docs/d00005217-Borr.pdf"


# urlPilar = "http://vriunap.pe/repositor/docs/d{:08d}-Proy.pdf"
initialRange = 0
endRange = 90_000

currentPath = os.getcwd()

for i in range(initialRange, endRange):
    try:
        # print(f"downlodin {i}")
        iUrl = urlPilarBorrador.format(i)
        iFile = os.path.join(currentPath, "d{:08d}-Borr.pdf".format(i))
        # print(iUrl)
        print(iFile)
        urllib.request.urlretrieve(iUrl, iFile)
    except Exception as e:
        print(e)
