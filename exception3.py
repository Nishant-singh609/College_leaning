f=open("text.txt","w")
f.write("hello nishant")
f.close()
print("Read the file")

f=open("text.txt","r")
constant =f.read()
print(constant)
f.close()

f=open("text.txt","a")
f.write("\n new line added")
f.close()
print("added data")

with open("text.tex","w") as f:
    f.write("name ")

