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
    print(count,filename)
    if("atlas" in filename):
        os.rename(sys.argv[1] + "\\" + filename, sys.argv[1] + "\\" + filename[0:7] + ".atlas.txt")
    elif(".png" in filename):
        os.rename(sys.argv[1] + "\\" + filename, sys.argv[1] + "\\" + filename[0:7] + ".png")
    elif(".prefab" in filename):
        os.rename(sys.argv[1] + "\\" + filename, sys.argv[1] + "\\" + filename[0:7] + ".json")
       
  eff = sys.argv[1] + "\\eff"
  for count, filename in enumerate(os.listdir(eff)):
    print(count,filename)
    if("atlas" in filename):
        os.rename(eff + "\\" + filename, eff + "\\" + filename[0:7] + ".atlas.txt")
    elif(".png" in filename):
        os.rename(eff + "\\" + filename, eff + "\\" + filename[0:7] + ".png")
    elif(".prefab" in filename):
        os.rename(eff + "\\" + filename, eff + "\\" + filename[0:7] + ".json")
           
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()