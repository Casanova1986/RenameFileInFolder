# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
# python .\RenamAllSubFolder_Asset.py E:\Resource\AeonEcho-Assets-Extract\Assets\autobuildpet\assetbundles\herobg
import os
import sys

# Function to rename multiple files
def main():
  print(sys.argv)
  print(sys.argv[1])

  for count, filename in enumerate(os.listdir(sys.argv[1])):
    subFolder = sys.argv[1] + "\\" + filename
    for count, subname1 in enumerate(os.listdir(subFolder)):
        subFolder2 = subFolder + "\\" + subname1
        for count, subname in enumerate(os.listdir(subFolder2)):
            print(count,subname)
            if("atlas.bytes" in subname):
                os.rename(subFolder2 + "\\" + subname, subFolder2 + "\\" + subname.split(".")[0] + ".atlas.txt")
            # elif(".skel.asset" in subname):
            #     os.rename(subFolder2 + "\\" + subname, subFolder2 + "\\" + filename.split(".")[0] + ".skel.bytes")
      

 
           
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()