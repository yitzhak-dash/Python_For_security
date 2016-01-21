# open(name[, mode[, buffering]]) - same thing as the file()
#       name - filename
#       mode - how you are opening the file.
#           a. Common Options: w (write), r(read),a(append)
#           b. you can add a '+' to your option, which allows read/write to be done with the same object
#           c. buffering - determines the file buffer size.(usually unnecessary)
# file.write(string) - prints the string to the file, there is no return
# file.read([bufsize]) - read up to the "bufsize" numbers of bytes from the file. If run without the "bufsize" option, read the entire file
# file.close() - close the file and destroy the file object

file_obj = open("test.txt", "w+")
file_obj.write("we are the knights who say ni")
file_obj.close()
file_obj = open("test.txt", "a+")

print file_obj.read()
file_obj.close()
print file_obj
