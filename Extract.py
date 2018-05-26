'''
Extractor utility for windows
Creator: Shubham Tambere
 Script location:-   C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\SendTo\
'''
import os
from sys import argv, exit
import ctypes
import time
import tarfile
from zipfile import ZipFile

Extentions=[ 'zip', 'tar','gz']



def extract_tar(fileName, extractLocation=None):
    extractLocation = fileName.rsplit('\\',1)[0]
    print("Extracting...")
    tar = tarfile.open(fileName+'.'+'tar.gz')
    tar.extractall(extractLocation)
    tar.close()

def extract_zip(fileName, extractLocation=None):
    extractLocation = fileName.rsplit('\\',1)[0]
    #ctypes.windll.user32.MessageBoxA(0, "Unzipping at:"+extractLocation, "Error", 1)
    print("Extracting...")
    zip = ZipFile(fileName+'.'+'zip')
    zip.extractall(extractLocation)

def api_extract(fileName,extention):
    if(fileName.endswith('.tar')):
        fileName=fileName[:-4]
        extention='tar'
    methods={
        'zip':extract_zip,
        'tar':extract_tar
    }
    methods[extention](fileName)


def process(completeFileName):
    fileNameList = completeFileName.rsplit('.',1)
    print fileNameList
    fileName=fileNameList[0]
    extention=fileNameList[1]
    if extention not in Extentions:
        ctypes.windll.user32.MessageBoxA(0, "Extention not supported!", "Error", 1)
        exit(1)
    return fileName,extention


def main():
    completeFileName=argv[1]
    #fileName, ext = process(completeFileName)
    fileName,extention=process(completeFileName)
    api_extract(fileName,extention)


if __name__ == '__main__':
    main()
