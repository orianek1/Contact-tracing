# Oriane Kacoutie
# Date: 2020-12-06
# Description: Contact tracing
# this program is to trace the people that have been in contact with a sick person or not


import sys
import os
from formatList import*

#Part 1
def recordContact(file):
    #create a dictionary to store the data in the file
    nameDictionary = {}

#this is to loop into the lines of the file
    for line in file:
        # this code removes whitespace
        line= line.strip()
        #this line store elements seperated by coma
        line= line.split(",")
        #the first person in the list
        person=line[0]
        #this is for the variables in teh list that comes after the first element
        values= line[1:]
        #This is to sort out the elements present in the list
        values.sort()
    #It adds patient to the dictionary and list of contact
        nameDictionary[person]= values

    return nameDictionary



#Part 2
#this is the function that will allow us to define patient zero
def patientZero(nameDictionary):

#creating a list for patient zero
    patientZeroList=[]
    #this code loops throught the keys in the list
    for keys in nameDictionary.keys():
        #this is a count function to add up the number of patient zero in the originial list
        count = 0
        #this code loops throught the values in the list
        for values in nameDictionary.values():
           #this is to check if a key item is present in the values or not
            if keys not in values:
                count += 1
                #this is to add the key value that is not present in the values
                if count == len(nameDictionary.values()):
                    #this is to add the key item that are patient zero to the new list for patient zero
                    patientZeroList.append(keys)
    return (patientZeroList)


#Part3
#this is the function that will help us define if there is a zombie in the vaues
def potentialZombies(nameDictionary):
    res3=[]

#creating a list for potential zombies
    potentialZombiesList=[]
#this code loos throught the values in the list
    for values in nameDictionary.values():
        #this is the count funtion to count the number of zombies in the list
        count = 0
        #this code is to loop through the keys in the list
        for keys in nameDictionary.keys():
            #this is to check if a key item is present in the values
            if keys not in values:
                count +=1
                #this is to add the key item that are potential zombies to the new list created
                if count == len(nameDictionary.keys()):
                   potentialZombiesList.append(values)
                for i in potentialZombiesList:
                    if i not in res3:
                        res3.append(i)
    return (res3)



#Part 4
#this is the function to define the people that are not in the zombie list or patient zero list
def neither(nameDictionary):


#creating a list for neither a zombie or patient zero
    neitherList=[]
#this is to loop throught the keys in the dictionary
    for keys in nameDictionary.keys():
        #if the key is not present in the patient zero list and potentiel zombie it is added to the new list
        if keys not in patientZero(nameDictionary) and  keys not in potentialZombies(nameDictionary):
            neitherList.append(keys)
    return (neitherList)


#part 5
#this is the function to define the most viral people in the list
def mostViral(nameDictionary):
    # this is the list where the most viral people will go but it has diplucates
    mostViralList=[]
    max_infected=0
    #this is the list that will remove the duplicates from the most viral list and store it there
    res=[]
    # I got this code from https://stackoverflow.com/questions/27210042/how-do-you-find-which-key-in-a-dictionary-has-the-longest-list-of-values/27219157
    #the code ends at line 111
#This is to loop through the key present in the dictionary
    for keys in nameDictionary.keys():
        #this is to check the lengh of the values present in the key
        viral_len= len(nameDictionary[keys])
        #this is to loop through the values present in the dictionary
        for values in nameDictionary.values():
            #if the the person appears multiple multiple time in the list
            #it will be added to the new list as the most viral
            if viral_len >= max_infected:
                max_key= keys
                max_infected=viral_len
                mostViralList.append(max_key)
                #this is to go throught the item in the new list and remove the duplicates and put them in another list
                #this is so they will only appear once
                for i in mostViralList:
                    if i not in res:
                        res.append(i)
    return (res)


#part 6
# this is the function to define the most tastiest people in the list
def tastiest(nameDictionary):

    # new list of people thst are the most infected
    tastiestList = []
#this is a new list v=creates wher all the sick people present in the dictionary will be store
    all_sick = []
    #this is to loop throught the values present in the dictionary
    for values in nameDictionary.values():
        for item in values:
            all_sick.append(item)

    # I got the code to count the frequency on https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
    #the code ends at line 146
    #To create an empty dictionary
    frequency_sickPeople={}
#this is to loop through the people in the new list with all the sick people
    for item in all_sick:
#this is to count the frequency at which the elelemtn is present in teh dictionary
        if (item in frequency_sickPeople):
            frequency_sickPeople[item] += 1
        else:
            frequency_sickPeople[item] = 1

    #this is to find the larger frequency
    max_frequency = 0

    for values in frequency_sickPeople.values():
        if values > max_frequency:
            max_frequency = values

    for key in frequency_sickPeople:
        if frequency_sickPeople[key] == max_frequency:
            tastiestList.append(key)

    return (tastiestList)




#Part 7
#this is not done but all the code above works

def distance(nameDictionary):
    #this is the new list that will store the name of evryone in the key of the dictionary
    everyNameList=[]

    for keys in nameDictionary.keys():
        everyNameList.append(keys)
    for values in nameDictionary.values():
        for name in values:
            if name not in everyNameList:
                everyNameList.append(name)

    #this is the dictionary that will contain the heights
    heightDictionary= {}
    for name in everyNameList:
        #this is to set everyone including the potential zombies to 0
        heightDictionary[name] = 0


    changed = True
    while changed:
        changed= False
        #this is to loop through everyone that is infected
        for p1 in nameDictionary:
            #this is to loop through everyone they came in contact with
            for p2 in nameDictionary[p1]:
                if heightDictionary[p1] <= heightDictionary[p2]:
                    heightDictionary[p1] = heightDictionary[p2] + 1
                    changed = True
    return heightDictionary





def main():
    # this code is to read the file
    if (len(sys.argv)==2):
        filename = sys.argv[1]
        print(filename)
    else:
        filename =input("Enter the filename")


#open the file
    if os.path.exists(filename):
         file= open(filename)
    else:
         sys.stderr.write("file does not exist")
         sys.exit(1)

    nameDictionary = recordContact(file)



#for part 1 to print the results
    print("Contact Records:")
    for keys in nameDictionary.keys():
        print("%s had contact with %s" % (keys, formatList(nameDictionary[keys])))

#for part 2 to print the results

    print("Patient Zero(s): %s" % (formatList(patientZero(nameDictionary))))
#for part 3
    print("Potential Zombies: %s" % (formatList(potentialZombies(nameDictionary))))

# part 4
    print("Neithter Patient Zero or Potential Zombie: %s" %(formatList(neither(nameDictionary))))
# Part 5
    print ("Most Viral People: %s"%(formatList(mostViral(nameDictionary))))
#part 6
    print ("Tastiest: %s" %(formatList(tastiest(nameDictionary))))
#part 7
    print("Heights:")
    print((distance(nameDictionary)))


main()





