# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
import sys
  # python Rename_multiple_asser.py '#directory'
# Function to rename multiple files
def main():
  print(sys.argv)
  print(sys.argv[1])


  for count, subname in enumerate(os.listdir(sys.argv[1])):
    print(count,subname)
    if("atlas.prefab" in subname):
        os.rename(sys.argv[1] + "\\" + subname, sys.argv[1]  + "\\" + subname.split(".")[0] + ".atlas.txt")
    # elif(".json.prefab" in subname):
    #     os.rename(sys.argv[1] + "\\" + subname, sys.argv[1]  + "\\" + subname.split(".")[0] + ".json")
    elif(".skel.prefab" in subname):
        os.rename(sys.argv[1] + "\\" + subname, sys.argv[1]  + "\\" + subname.split(".")[0] + ".skel.bytes")
           
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()