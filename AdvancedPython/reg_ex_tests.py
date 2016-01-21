import re

# \d looks for any integer, same as [0-9]
# {3} specifies how many of a characters you're looking for.
# - nothing more or less than "-" character
# "." matches any character (except newlines)
# "[]" matches anythings in a given set
# [a-zA-z] matches any letter
# [a-z] lowercase latter
# "^" anything not in a given set: [^a1] - matches any character except "a" and "1"
# "*" matches 0 o more of a given character o set
# "+" 1 or more
# "?" 0 or 1
# "a|b" a or b

data = "safwef9wefja;;dkfjweipjfn;f;2349032ufeiq123-123-1234as.kf[aokfs[mw[lmfoeof943853eldfk123-123-1235ldfd"

pattern = re.compile("\d{3}-\d{3}-\d{4}")
match_object = re.search(pattern, data)
print match_object.group(0)
# ??? print match_object.group(1

print match_object.start()
print match_object.end()
data = data[:40] + data[52:]
match_object = re.search(pattern, data)
print match_object.group(0)

