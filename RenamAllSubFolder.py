# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
import sys

# Function to rename multiple files
def main():
  print(sys.argv)
  print(sys.argv[1])

  for count, filename in enumerate(os.listdir(sys.argv[1])):
    subFolder = sys.argv[1] + "\\" + filename
    for count, subname in enumerate(os.listdir(subFolder)):
        print(count,subname)
        if("atlas" in subname):
            os.rename(subFolder + "\\" + subname, subFolder + "\\" + subname.split(".")[0] + ".atlas.txt")
        elif(".skel.asset" in subname):
            os.rename(subFolder + "\\" + subname, subFolder + "\\" + subname.split(".")[0] + ".skel.bytes")
        # elif(".png" in subname):
        #     print(subFolder + "\\" + subname, subFolder + "\\" + subname.split(".")[0])
        # else:
        #     os.remove(subFolder + "\\" + subname)

 
           
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()