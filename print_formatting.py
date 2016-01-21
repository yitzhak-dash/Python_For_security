# print "%[format_character]" % (corresponding data)

str1 = "this a string"
str2 = " a string too"
print str1 + str2

str1 = "Our number is: "
str2 = 5
# print str1 + str2 exception: cannot concatenate 'str' and 'int' objects
str1 = "Our number is: %d"
print str1 % (str2)
print str1 + str(str2)
str1 = "Our number is: "
print str1 + str(str2)

str1 = int(raw_input("Your number is: "))
str2 = int(raw_input("Your number is: "))
str3 = int(raw_input("Your number is: "))
print "You entered: %d\t%d\t%d" % (str1, str2, str3)
