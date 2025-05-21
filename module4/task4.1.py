# Task 4: File Handling
# Create a file named 'sample.txt' and write some text to it.
file1=open('sample.txt','w')    
print("Reading file contents:")
content_s=file1.write('this is a sample text file\n')
content_s=file1.write('it contains multiple lines\n')
file1.close()

try :
    file1=open('sample.txt','r')
    content_s=file1.read()
    print(content_s)
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")
finally:
    file1.close()
