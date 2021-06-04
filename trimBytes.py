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
    fp = open(sys.argv[1] + "\\" + filename, "rb")
    data = fp.read()
    fp.close()

    fp = open(sys.argv[1] + "\\" + "_" + filename , "wb")
    fp.write(data[int(sys.argv[2]):-1])
    fp.close()
    print(count,filename)
    
       
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()