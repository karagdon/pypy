#opening,writing,closing a file
my_list = [i**2 for i in range(1,11)]
my_file = open("output.txt", "r+")

# Add your code below!
for number in my_list:
    my_file.write(str(number) + "\n")
my_file.close()

###

# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()
read_file.close()
# Try to read from the file
print read_file.read()


# With/AS #

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

#See if it is closed#
with open("text.txt", "w") as my_file:
	my_file.write("Success!")
	if my_file.closed == 1:
	    my_file.close()
	    
print my_file.closed
	