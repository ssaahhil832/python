
#task 4.2
# This program appends data to a file and reads the updated contents.
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
