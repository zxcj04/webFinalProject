
with open("test/tmp/test.txt", "r") as fp:

    ori = fp.readlines()

print(ori)

first = "\""
replacement = "\", \""
last = "\""

ori = replacement.join(ori)

ori = first + ori.replace("\n", "") + last

ori = ori.replace("\"\", ", "")

with open("test/tmp/new.txt", "w") as fp:

    fp.write(ori)