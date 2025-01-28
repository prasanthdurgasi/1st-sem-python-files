with open("hi.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

f = open("out.txt","r")
print(f.read())