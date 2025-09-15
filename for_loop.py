for letter in "Giraffe Academy":
    print(letter)
    
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
    
for index in range(10):
    print(index)

for index in range(3,10):
    print(index)

friends = ["Jim", "Karen", "Kevin", "Oscar", "Toby"]
for index in range(len(friends)):
    print(friends[index]) 

for index in range(5):
    if friends[index]=="Oscar":
        print("Found Oscar!")
        break
    print(friends[index])  
    
    