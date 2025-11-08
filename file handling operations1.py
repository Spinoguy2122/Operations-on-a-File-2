with open('codingal.txt','w') as file:
    file.write("Hi i am Penguin and I am 1 yr old.")
file.close()

with open('codingal.txt','r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()