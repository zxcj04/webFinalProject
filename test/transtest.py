
with open("test/tmp/test.txt", "r") as fp:

    ori = fp.readlines()

first = "\""
replacement = "\", \""
last = "\""

ori = replacement.join(ori)

ori = first + ori.replace("\n", "") + last

with open("test/tmp/new.txt", "w") as fp:

    fp.write(ori)