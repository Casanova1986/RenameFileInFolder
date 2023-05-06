# Pythono3 code to rename multiple 
# files in a directory or folder
  

# trimBytes all file in folder

# x = first bytes want to trim
# python trimBytes.py '#directory' x


# importing os module
import os
import sys

# Function to rename multiple files
def main():
  print(sys.argv)
  print(sys.argv[1])

  for count, filename in enumerate(os.listdir(sys.argv[1])):
    fp = open(sys.argv[1] + "\\" + filename, "rb")
    data = fp.read(100)
    idx = data.index(bytes('U','ascii'))
    fp.close()


    fTrim = open(sys.argv[1] + "\\" + filename, "rb")
    dataTrim = fTrim.read()
    fTrim.close()

    print(count,filename,data,idx)
    fp = open(sys.argv[1] + "\\" + filename , "wb")
    fp.write(dataTrim[idx:-1])
    fp.close()
    print(count,filename)

  # for count, filename in enumerate(os.listdir(sys.argv[1])):
  #   fp = open(sys.argv[1] + "\\" + filename, "rb")
  #   data = fp.read()
  #   fp.close()

    
    
       
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()