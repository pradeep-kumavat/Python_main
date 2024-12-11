#reading a file
# f = open("7th_myfile.txt","r")
# text = f.read()
# print(text)
# f.close()

#writng a file
#1st way to to do this in this close function is used 
# f= open("7th_myfile2.txt", "w")
# f.write("my name is ram  ")
# f.close()

#2nd way : in this you do not have to use close function
# with open("7th_myfile2.txt", "a") as f:
#     f.write("this is ram  2")

#readline method
# f = open("7th_myfile.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

#writeline mehthod
# f = open("7th_myfile2.txt","w")
# lines = ["line1 \n","line2 \n "]
# f.writelines(lines)
# f.close()

#seek method
# f = open("7th_myfile2.txt","r")
# f.seek(10)
# data = f.read(5)
# print(data)
# f.close()

#truncate method
f = open("7th_myfile2.txt","w")
f.write("hello world !!")
f.truncate(8)
f.close()

with open("7th_myfile2.txt","r") as f:
    print(f.read())



