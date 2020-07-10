'''This program applies Benford's Law over numerical data from a csv file and returns
the distribution of digits (the frequency of digits in a sublist [1,2,3,4,5,6,7,8,9,0]
where each index corresponds to the frequency of that leading digit. In addition, this
program also regularises the distribution based on its booleon (default = false).
(minimum, maximum, average, standard deviations and correlation) '''

#Project1
#CITS1401
#Author: Anshul Kotha
#Student ID: 22653683

"""Main function, will first run an if-else check on regularise if it's boolean or not, then and handle any error."""
def main(filename,no_places,regularise = False):
    if no_places <= 0:
        print("Enter an integer value that is greater than 0 for no_places")
        return []
    if regularise == True or regularise == False:
        #Handling possible errors while calling main.
        try:
            AnalyzedData = get_AnalyzedData(filename)
        except FileNotFoundError:
            print("File wasn't found. Please input the correct correct filename")
            return []
        except OSError:
            print("Please input a valid filename which is a string.")
            return []
        except TypeError:
            print("Please enter a string value, not variable")
            return []
        else: 
            try:
                return get_Frequency(AnalyzedData,no_places,regularise)
            except TypeError:
                print("Please provide valid integer for no_places")
                return []
    else:
        print("Provide a Boolean Value for regularise, no numbers. Only True or False")
        return []

"""Using a Try Except function to extract numerical data only."""
def numerical_values(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
"""This function extracts only integers in the form of strings for further processing."""
def get_AnalyzedData(filename):
    f = open(filename,"r")
    #Reading the file
    Numerical = []
    for row in f:
        main_data = row.split(",")
        #All values are split by commas
        main_list = main_data[:-1]
        #This removes the last value along with \n
        main_list.append(main_data[len(main_data)-1][:-1])
        #Data lost along with \n is recovered
        newlist = [x for x in main_list if numerical_values(x)]
        #List comprehension to extract only numerical values (integers and float values)
        for i in newlist:
            Numerical.append(i)
    f.close()
    
    truncated_decimals = []
    for each_value in Numerical:
        #Stores only integers in "truncated_decimals" via type conversions.
        each_value = float(each_value)
        each_value = int(each_value)
        each_value = str(each_value)
	each_value = abs(each_value)
        truncated_decimals.append(each_value)
    
    return truncated_decimals
    
"""This function returns the final output of the program by storing digit frequencies in their respective indexes"""
def get_Frequency(truncated_decimals,no_places,regularise):
    n = no_places
    templist = []
    #Creating an empty list and calculating frequency for each number through while loop.  
    while(n > 0):
        digit_templist = []
        for num in truncated_decimals:
            if len(num) >= n:
                digit_templist.append(int(num[n-1]))                
        
        frequencies = [0]*10
        digit = []
        for i in range(0,10):
            frequencies[i - 1] = digit_templist.count(i)
            digit.append(i)
        templist.append(frequencies)
        n -= 1
    templist.reverse()
    final_output = templist

    #Checks for the regularise argument boolean type, and gives output accordingly.
    if regularise == True:
        final_percentages = getRegularise(final_output)
        return final_percentages
    else:
        return final_output

"""This function returns nested lists in percentages of the sum total of their respective nestedlist."""
def getRegularise(final_counts):
    standard_size = len(final_counts)
    size_of_counts = [0]*standard_size
    #Lists of 0s
    for lists in range(standard_size):
        #Iterations of lists, and calculates sum of respective list is storing it in size_counts 
        size_of_counts[lists] = sum(final_counts[lists])
        length_of_numbers = len(final_counts[lists])
        for numbers in range(length_of_numbers):
            #Iterates through each number and converts it into a percentage.
            #Uses if statement to skip lists that sum to 0. 
            if (size_of_counts[lists] != 0):
                final_counts[lists][numbers] = (final_counts[lists][numbers])/(size_of_counts[lists])
            #Rounding Numbers after calculation
            final_counts[lists][numbers] = round(final_counts[lists][numbers],4)
    #Returns value back to get_Frequency()
    return final_counts




    
    
    


