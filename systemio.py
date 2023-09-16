'''read from a file'''
text = open("sample.txt", "r")

for i in text:
    print(i)

text.close()

'''write to an existing file and read from it.'''
text = open("sample.txt", "w")
text.writelines("My name is Gar")
text.close()

text = open("sample.txt", "r")
print(text.readline())

'''x is to create a file. But w would create a file if it doesn't exist'''
text = open("sample2.txt", "w")
text.write("This is sample2 that was just created")
text.close()

text = open("sample2.txt", "r")
print(text.readline())
text.close()


'''Delete a file'''
import os
os.remove('sample1.txt')