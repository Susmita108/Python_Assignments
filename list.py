'''
1- write a program which takes single input from user contaning first name,last name and age as comma separated
value and display then in 3 lines in given format below.
example user input : Susmita,Jana,23
output:
First name is Susmita
last name is Jana
Susmita is 23 years old
'''

# f_name,l_name,age = input("Enter your first name,last name,age by separating a comma: ").capitalize().split(",")
# print(f"First name is {f_name}")
# print(f"last name is {l_name}")
# print(f"{f_name} is {age} years old")

'''
2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]

combined the 2 list and diplay the same without using extend method
'''

# list1 = [1,3,4]
# list2 = [2,4,6]
# list1.append(list2[0])
# list1.append(list2[1])
# list1.append(list2[2])
# print(list1)

'''
3- given a list list1=[1,2,3,4,5,6,7,8]
diplay a new list which contains only odd position index values from above list
'''

# list1=[1,2,3,4,5,6,7,8]
# len_list1 = len(list1)
# new_list = list1[1:len_list1:2]
# print(new_list)

'''
4- ipl= ['CSK','MI','KKR','LSG','PBKS']
take a ipl team name as input from user and display a list of all elements from that name.
example : input : KKR
output : ['KKR','LSG','PBKS']
'''

# ipl= ['CSK','MI','KKR','LSG','PBKS']
# team = input(('Enter a team name: '))
# location = ipl.index(team)
# new_list = ipl[location: ]
# print(new_list)

'''

5- ipl= ['CSK','MI','KKR','LSG','PBKS']
take a ipl team name as input from user and display a list of all elements except input one
example : input : KKR
output : ['CSK','MI','LSG','PBKS']
'''
# name = input("Enter a team name from ipl: ")
# ipl= ['CSK','MI','KKR','LSG','PBKS']
# location = ipl.index(name)
# ipl.pop(location)
# print(ipl)

'''
6- ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . replace the index elementof list with 
new value and display the same
example : input : 2,SRH
output : ['CSK','MI','SRH','LSG','PBKS']

'''
# ipl= ['CSK','MI','KKR','LSG','PBKS']
# index, team_name = input("Enter the index, team name which you want to insert(separrated by coma): ").split(',')
# index = int(index)
# ipl.pop(index)
# ipl.insert(index, team_name)
# print(ipl)

'''
7- ipl= ['CSK','MI','KKR','LSG','PBKS']
take ipl team name as user input. display True if the team exists else display False.
'''
# ipl= ['CSK','MI','KKR','LSG','PBKS']
# team_name = input("team_name: ")
# print(team_name in ipl)

'''
8-ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
Display the old list , new list,length of original and new list

example : input : 2,SRH
output : 
old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6
'''
ipl= ['CSK','MI','KKR','LSG','PBKS']
index,new_team = input().split(',')
new_list = ipl.copy()
index = int(index)
new_list.insert(index,new_team)
print("length of old list", len(ipl))
print("New List",new_list)
print("length of new list", len(new_list))