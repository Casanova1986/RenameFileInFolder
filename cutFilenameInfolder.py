# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
import sys

# Function to rename multiple files
def main():
  print(sys.argv)
  print(sys.argv[1])

  for count, foldername in enumerate(os.listdir(sys.argv[1])):
    subFolder = sys.argv[1] + "\\" + foldername
    for count, subname in enumerate(os.listdir(subFolder)):
        print(count,subname)
        if("meta" in subname):
            os.remove(subFolder + "\\" + subname)
        else:
            if(len(subname.split(".")) > 2):
                os.rename(subFolder + "\\" + subname, subFolder + "\\" + subname.split(".")[0] + "."+subname.split(".")[2])

 
           
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()