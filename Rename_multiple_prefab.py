# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
import sys

# Function to rename multiple files
def main():
  print(sys.argv)
  print(sys.argv[1])


  for count, subname in enumerate(os.listdir(sys.argv[1])):
    print(count,subname)
    if("atlas.prefab" in subname):
        os.rename(sys.argv[1] + "\\" + subname, sys.argv[1]  + "\\" + subname.split(".")[0] + ".atlas.txt")
    elif(".json.prefab" in subname):
        os.rename(sys.argv[1] + "\\" + subname, sys.argv[1]  + "\\" + subname.split(".")[0] + ".json")
  
           
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()