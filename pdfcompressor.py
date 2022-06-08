from __future__ import print_function
import os
import subprocess
import sys

def main(fileName = None, outputName = None):
    
    n = len(sys.argv)
    print("Total arguments passed:", n)
    

    if n > 1:
        fileName = sys.argv[1]
    elif n > 2:
        outputName = sys.argv[2]
    
    elif outputName:
        outputName = outputName
    
    else:
        outputName = fileName.replace(".pdf", "COMPRESSED_FILE.pdf")

    print(fileName)

    size = os.path.getsize(fileName)
    print (size)
    #226613869 - this is how many bytes Albany is
    #20000000 - this is the 20 mb limit for emails in outlook
    if size >= 20000000:
        print("COMPRESSING... ")
        arg1 = '-sOutputFile=' + outputName 
        p = subprocess.Popen(['C:/Program Files/gs/gs9.56.0/bin/gswin64c.exe',
                            '-sDEVICE=pdfwrite', 
                            '-dCompatibilityLevel=1.4',     
                            '-dPDFSETTINGS=/screen', '-dNOPAUSE', 
                            '-dBATCH', '-dQUIET',str(arg1), fileName ], 
                            stdout=subprocess.PIPE)
        print (p.communicate())
        return outputName
    
    else:
        return fileName

if __name__ == "__main__":
    main()
