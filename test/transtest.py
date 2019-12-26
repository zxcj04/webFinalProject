
with open("test/tmp/test.txt", "r") as fp:

    ori = fp.read()

ori = ori.split("\n")

print(ori)