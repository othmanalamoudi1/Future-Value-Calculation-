import locale
def welcome_print():
    print ( ''' 
    Welcome to the future value calculator 
    Based on an intial invesment, an "effective interest rarte, 
    and a number of yours, Calculates the future value of an invesmnet 
    with interest applied using a simpl eand compounded annual interest rate. 
    A table of results displays the future values of the user's investment year by year.

    Enter 'x' to exit at any time 
    ''')

def get_valid_input (prompt, min, max):
    #Construct the prompt message by embedding the min/ max in it 
    full_prompt = f'{prompt} ({min:n} -{max:n})? '
    #create a variable to track if we are in range and start false so 
    #we will loop through and ask at least once 
    value_in_range = False
    #
    #
    while not value_in_range:
        #
        raw_anwser= input (full_prompt)
        #
        if raw_anwser.lower()=='x':
            exit()
        #
        user_value = int (raw_anwser)
        value_in_range= min <= user_value <=max
        if not value_in_range:
            print('that is not in range, try again...')
        #return the valid value  from the user now the loop is done
        return user_value

def interest_rate (prompt,min, max):
    full_prompt = f'{prompt} ({min:n} -{max:n})? '
    value_in_range = False
    while not value_in_range:
        # 
        raw_anwser = input(full_prompt)
        if raw_anwser.lower()=='x':
            exit()
        #otherwise convert ut ti a number and check if the number is in range. 
        interest_rate = float(raw_anwser)
        value_in_range = 1 <= interest_rate <=100
        if not value_in_range:
            print('this is not in range, try')
    return interest_rate

def num_of_years (prompt,min,max):
    full_prompt = f'{prompt} ({min:n} -{max:n})? '
    value_in_range = False
    while not value_in_range:
        # 
        raw_anwser = input(full_prompt)
        if raw_anwser.lower()=='x':
            exit()
        #otherwise convert ut ti a number and check if the number is in range. 
        number_of_year = int(raw_anwser)
        value_in_range = 1 <= number_of_year <=50
        if not value_in_range:
            print('this is not in range, try')
    return number_of_year

# first we must call the function to get the title and descreiption
welcome_print()
# call the funtion to get the value for out intitial investment 
investment = get_valid_input('what is the initial investment in US$', 1, 100000)
rate_interest = interest_rate ('what is the interest rate as percentage (1-100)?',1,100)
year_num = num_of_years ('how many years of investment (1-50)?',1,50)
#-------------------------------------------


print (''' 
Period            FV Simple            FV Compounded
------------------------------------------------------
''')
for year in range(1, year_num+1):
    year_label = 'Year ' + str(year)
    simple_value = format (investment * (1+ rate_interest/100 * year),".2f")
    compund_Value = format (investment * (1+ rate_interest/100) ** year,".2f")

    print (f'{year_label:<8} {simple_value:>17}{compund_Value:>17}')
    





