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

#task 4.2
data=input("Enter the data to be written in the file: ")
file1=open('output.txt','a')
content_s=file1.write(data)
file1.write('\n')
print("Data written to the file successfully.")

add_data=input("Do you want to add more data? (yes/no): ")
if add_data.lower() == 'yes':
    data=input("Enter the data to be added: ")
    file1.write(data)
    file1.write('\n')
    print("Data added to the file successfully.")
else:
    print("Data not added to the file.")
file1=open('output.txt','r')
content_s=file1.read()
print("Updated file contents:\n", content_s)
file1.close()
