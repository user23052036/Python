#basic- commands
#indexing in python is 0based and -1 represents last char
# [i:] -> extracting ith charecter to the last charecter
# [:i] -> extracting from 0th charecter to the (i-1) charecter

string = input("Enter your string: ")
print("Last element: ",string[4:])
print("Second to last element: ",string[:4])
print(string[5:10:4])

#reverse the string
rev = string[::-1]
print(rev)



#--------------------------------------------

greeting = "hello Souvik"
print("1. ",greeting)
print("2. ",len(greeting))
print("3. ",greeting[0])
print("4. ",greeting[-1]) #printing the last indx val

greeting = greeting.replace("Souvik","Souvik Mandal")
print("5. ",greeting)

string1 = "hello"
string2 = "world"
print("1. ",string1,string2)

cost = float(35.43)
print("Bar tab = $",cost)


