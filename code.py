t=input("Enter no. of files do want to merge\n")
filenames =[]
print "Enter file names"
for i in range(1,t+1)	:
	filenames.append(raw_input())
with open('new.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)