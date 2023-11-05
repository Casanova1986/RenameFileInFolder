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
    try:
      fp = open(sys.argv[1] + "\\" + filename, "r")
      data = fp.read(1)
      fp.close()
      if(data == "{"):
        try:
          os.rename(sys.argv[1] + "\\" + filename, sys.argv[1]  + "\\" + filename.split(".")[0].split(" ")[0] + ".json")
        except:
          print("ERR1:",filename,data)
      else:
        try:
          os.rename(sys.argv[1] + "\\" + filename, sys.argv[1]  + "\\" + filename.split(".")[0].split(" ")[0] + ".atlas.txt")
        except:
          print("ERR2:",filename,data)
    except:
      print("ERR3:",filename,data)
    


    # fp = open(sys.argv[1] + "\\" + "_" + filename , "wb")
    # fp.write(data[int(sys.argv[2]):-1])
    # fp.close()
    # print(count,filename)
    
       
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()