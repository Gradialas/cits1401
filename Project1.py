'''This is a program to read the data from a csv file of university students' performance and 
then return specific stastitical aspects of the marks of the students and their ranking
(minimum, maximum, average, standard deviations and correlation) '''
#Project1
#CITS1401
#Author: Anshul Kotha
#Student ID: 22653683

#Ranking Functions To Call Later In main()

def rank_simple(numbers):
    output = [0] * len(numbers)
    for i, x in enumerate(sorted(range(len(numbers)), key=lambda y: numbers[y], reverse=True)):
        output[x] = i+1
    return output

#Transposes Data

def transpose(listing_1):
    listing_2 = []
    for i in range(len(listing_1[0])): 
        row =[] 
        for item in listing_1: 
            # Appending to a new list with values and index positions.
            # i contains index position and item contains values.
            row.append(item[i]) 
        listing_2.append(row) 
    return listing_2




def main(filename):
    f = open(filename, "r")
    
    #Reading the file
    temp = []
    for line in f:
        mainData = line.split(",")       #Splitting the data in csv
        mainList = mainData[2:-1]    #Removing the /n last element and first 2 columns
        mainList.append(mainData[len(mainData)-1][:-1])   #row of marks
        temp.append(mainList)
        
    
    f.close()
    
    #Converting All Values to float
    temp = temp[1:]
    tempnew = []
    
    for list in temp:
        list = [float(i) for i in list]
        tempnew.append(list)
    temp = tempnew  
    del(tempnew) #Deletion for efficiency.
    
    #Addition of total marks obtained by each student
    sumtotal = 0
    for list in temp:
        for x in list:
            sumtotal += x
        list.append(sumtotal)
        sumtotal = 0
        
    val = len(temp[0]) #Gives numbers of columns required
    
    #Minimum marks
    mn = [val*100]*val
    #Maximum marks
    mx = [0]*val
    #Addition of total marks in a subject of all students
    #Then calculates minimum and maximum marks
    sumlist = [0]*val
    
    for list in temp:
        for x in range(0,len(list)):
            
            sumlist[x] += list[x]
            
            if(mn[x] > list[x]):
                mn[x] = list[x]
            
            if(mx[x] < list[x]):
                mx[x] = list[x]
    
    #Calculates Average Marks
    
    avg = []
    
    tempval = len(temp)
    for i in sumlist:
        i = round(i/tempval,4)
        avg.append(i)
    
    
    #Calculates Standard Deviation
    std = [] 
    
    for k in range(0,len(temp[0])): 
        tempvar = 0
        tempstd = 0
        for i in temp:
            tempvar += pow(i[k]-avg[k],2)/len(temp)
        tempstd = tempvar**0.5
        tempstd = round(tempstd, 4)
        std.append(tempstd)
    
    #Ranking Numbers
    """To make ranking easier, I will first transpose the list
    which will make inner lists have values of only one subject"""
    
    temp2 = transpose(temp)
    ranklist = []
    
    for x in range(0,len(temp2)):
        ranklist.append(rank_simple(temp2[x]))
        
        
    #Calculates the differences
    
    d2 = ranklist[:-1]
    d = []
    dfinal = []
    
    list2 = ranklist[len(ranklist)-1]
    
    for x in range(0,len(d2)):
        list1 = d2[x]
        d = []
        zip_object = zip(list1,list2)
        for list1_i, list2_i in zip_object:
            d.append((list1_i-list2_i)**2)
        dfinal.append(d)
    
    dfinal.append([0]*len(dfinal[0]))
    #This adds a final row full of zeros for the last element of the output
    
    #Calculating summation of difference
    sumd = []
    for list in dfinal:
        sumd.append(sum(list))
        
    #Calculating Correlation for each subject vs total marks
    cor = []
    n = len(dfinal[0])
    denom = n*((n**2)-1)
    for num in sumd:
        tempvalue = round((6*num)/denom,4)
        cor.append(round(1-tempvalue,4))
    
    return mn,mx,avg,std,cor 
    
    
        




