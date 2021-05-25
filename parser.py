import csv
import datetime
from collections import Counter

#Possible Addition

alfa=[]
bravo=[]
charlie=[]
delta=[]
echo=[]
foxtrot=[]
golf=[]
hotel=[]

fourc=[]
threec=[]
twoc=[]
firstie=[]

allOffences=[]
classone=[]
classtwo=[]

def printCompany(company):
    returnString=""
    for i in range(len(company)):
        returnString=returnString+company[i]+"\n"
    return returnString
def addToCompany(row):
    if (row[8] == "A"):
        alfa.append(editString)
    elif(row[8] == "B"):
        bravo.append(editString)
    elif (row[8] == "C"):
        charlie.append(editString)
    elif (row[8] == "D"):
        delta.append(editString)
    elif (row[8] == "E"):
        echo.append(editString)
    elif (row[8] == "F"):
        foxtrot.append(editString)
    elif (row[8] == "G"):
        golf.append(editString)
    elif (row[8] == "H"):
        hotel.append(editString)
def addToClass(row):
    if(row[7]=="2025"): # will change to 2025 once those excel docks are pushed
        fourc.append(row)
    elif(row[7]=="2024"):
        threec.append(row)
    elif(row[7]=="2023"):
        twoc.append(row)
    elif(row[7]=="2022"):
        firstie.append(row)
def addToOffence(row):
    offences=row[5].split(",")
    #print(offences)
    for i in range(len(offences)):
        #print(offences)
        print(offences[i])

        if(offences[i][0]=="1"):
                classone.append(row)
        elif(offences[i][0]=="2"):
                classtwo.append(row)

        allOffences.append(offences[i])

def commonOffences(offences):
    occurence_count = Counter(offences)

    return occurence_count.most_common(5)
def allTheOffences(offences):
    occurence_count = Counter(offences)

    return occurence_count.most_common(100)



def parseListEntry(firstList):
    yogangyear="20"
    yogangday=""
    yogangmonth=""


    yogangday = firstList[1]  # Dates format of 3 input lists wont change so these can be hard coded
    yogangyear = yogangyear+firstList[2]
    for i in range(len(firstList)):
        # Format is Month -> Day -> Year

        if (i == 0): #these however cannot be hard coded
            if (firstList[i] == "01"):
                yogangmonth = "JAN"
            elif (firstList[i] == "02"):
                yogangmonth = "FEB"
            elif (firstList[i] == "03"):
                yogangmonth = "MAR"
            elif (firstList[i] == "04"):
                yogangmonth = "APR"
            elif (firstList[i] == "05"):
                yogangmonth = "MAY"
            elif (firstList[i] == "06"):
                yogangmonth = "JUN"
            elif (firstList[i] == "07"):
                yogangmonth = "JUL"
            elif (firstList[i] == "08"):
                yogangmonth = "AUG"
            elif (firstList[i] == "09"):
                yogangmonth = "SEP"
            elif (firstList[i] == "10"):
                yogangmonth = "OCT"
            elif (firstList[i] == "11"):
                yogangmonth = "NOV"
            elif (firstList[i] == "12"):
                yogangmonth = "DEC"


        return yogangday+" "+yogangmonth+" "+yogangyear

# csv file name
filename = "C:\\Users\\Noah Soto\\Downloads\\apr21CSV.csv"
#filename=input("Enter full path to the excel document containing restricted cadet info: ")
# initializing the titles and rows list
fields=["Dates","Cadet Code","Class Year", "Name"]
rows = []

#Create an output file
outfile = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

f = open(outfile, "w")
###


# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        rows.append(row)

    # get total number of rows



for row in rows[:62]:


    editString=""
    theFinalFirstDate=""
    theFinalFinalDate=""
    #Serving time in the format of DATES TO BE SERVED NAME
    servingTime=str(row[0])
    #Get rid of the usless A thanks regis unless that actually means something hah
    newServingTime = servingTime.replace('A', '')
    newServingTime = newServingTime.replace('R', '')

    # Now to parse the DD-MM-YY format into DD MONTH YYYY

    editList=newServingTime.split(') (')
    #print(editList)
    if(len(editList)>1):
        month=""
        day=""
        year="2021"
        first=""
        final=""
        firstDate=[]

        yogangmonth=""
        yogangday=""
        yogangyear=""


        for i in range(len(editList)):
            firstDate=firstDate+editList[i].split(" ")
        first=firstDate[1]
        final=firstDate[-1]

        firstList=first.split("-")
        finalList=final.split("-")

        theFinalFirstDate=parseListEntry(firstList)
        theFinalFinalDate=parseListEntry(finalList)
    else:
        #we know theres only 1 index cos it aint greater then 0
        editList=editList[0].split(" ")

        #print(editList)
        first = editList[1]
        final = editList[-1]

        firstList = first.split("-")
        finalList = final.split("-")

        theFinalFirstDate = parseListEntry(firstList)
        theFinalFinalDate = parseListEntry(finalList)




     #Easy $$$$



    editString=theFinalFirstDate+" to "+theFinalFinalDate+" for "+row[9]
    editString=editString.replace(")","")
    #print(editString)
    #print(row[5])
    #Add to company
    addToCompany(row)
    addToClass(row)
    addToOffence(row)

print(commonOffences(allOffences))
print(classone)

    #f.write(editString+"\n")
f.write("---At a Glace ---\n")
f.write("Firsties Restricted: "+ str(len(firstie))+"\n")
f.write("Second Class Restricted: "+ str(len(twoc))+"\n")
f.write("Third Class Restricted: "+ str(len(threec))+"\n")
f.write("Fouth Class Restricted: "+ str(len(fourc))+"\n")
f.write("Class One Offences: "+str(len(classone))+"\n")
f.write("Class Two Offences: "+str(len(classtwo))+"\n")
f.write("Most common offences" + str(commonOffences(allOffences))+"\n")
f.write("-----ALFA ("+str(len(alfa))+")-----\n")
f.write(printCompany(alfa))
f.write("--------------\n")
f.write("-----BRAVO ("+str(len(bravo))+")----\n")
f.write(printCompany(bravo))
f.write("--------------\n")
f.write("-----CHARLIE ("+str(len(charlie))+")--\n")
f.write(printCompany(charlie))
f.write("--------------\n")
f.write("-----DELTA ("+str(len(delta))+")----\n")
f.write(printCompany(delta))
f.write("--------------\n")
f.write("-----ECHO ("+str(len(echo))+")-----\n")
f.write(printCompany(echo))
f.write("--------------\n")
f.write("-----FOXTROT ("+str(len(foxtrot))+")----\n")
f.write(printCompany(foxtrot))
f.write("--------------\n")
f.write("-----GOLF ("+str(len(golf))+")-----\n")
f.write(printCompany(golf))
f.write("--------------\n")
f.write("-----HOTEL ("+str(len(hotel))+")-----\n")
f.write(printCompany(hotel))
f.write("--------------\n")
f.write("Total Offence count:  " + str(allTheOffences(allOffences)))

