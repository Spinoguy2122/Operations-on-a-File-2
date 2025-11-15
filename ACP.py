file = open('Codingal.txt','r')
print(file.read())
file.close()

with open('Codingal.txt','w') as file:
    file.write("Hi i am Penguin and I am 1 yr old.")
file.close()

file = open('Codingal.txt','a')
file.write(" Hi! I am Penguin and I am 1 yr old.")
file.close()

outputFile = open('Codingal.txt', 'w')
inputFile = open('CodingalUpdated.txt', 'r')
lines_seen_so_far = set()
print("Eliminating duplicating lines")
for line in inputFile:

    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
inputFile.close()
outputFile.close()