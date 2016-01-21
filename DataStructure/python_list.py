string_list = ["we", "are", "the", "knights", "who", "say", "ni"]

print string_list[2]
string_list.remove("the")
print string_list[2]
print string_list
string_list[2] = "the"
print string_list
string_list.append("knights")
print string_list
string_list.pop()
print string_list

list = [11, 12, 13]
print list
new_list = [i ** 2 for i in list]
print new_list
