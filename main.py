calculation_to_minutes = 24*60
calculation_to_seconds = 24*60*60
calculation_to_units = 24
name_of_unit = "hours"


def daysToUnits(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_unit}")
    print(custom_message)
      


def daystX(nr_tag, kustom_message):
    
    return f"{nr_tag} tage sind {nr_tag*calculation_to_units} Stunde\n{kustom_message}"
   


# def validateAndExecute():
#     if(user_days_input.isdigit()):
#         user_input_number = int(user_days_input)
#         if user_input_number > 0:
#             daysToUnits(user_input_number, "All good!")
#             daysToUnits(20, "Awesome!")
#             calculated_values_DE =  daystX(user_input_number, "Wonderschön!")  
#             print(calculated_values_DE)  
#         elif user_input_number == 0:
#             print("you've entered zero, please enter a positive number as a correct input")
#     else:
#         print("Stop, this is an invaild user input, please enter a positive number as a correct input")

def validateAndExecute():
    try:
        user_input_number = int(num_of_days_element)
        # we want to do conversion only for positive integers
        if user_input_number > 0:
            daysToUnits(user_input_number, "All good!")
            daysToUnits(20, "Awesome!")
            calculated_values_DE =  daystX(user_input_number, "Wonderschön!")  
            print(calculated_values_DE)  
        elif user_input_number == 0:
            print("you've entered zero, please enter a positive number as a correct input")
    #except will catch the negative value without ValueError in it. With ValueError it doesn't see negative value as an error
    except: 
        print("Stop, this is an invaild user input, please enter a positive number as a correct input")

user_days_input = ""
while user_days_input != 'exit':
    # print(f"20 days are {20*calculation_to_minutes} minutes")
    # print(f"20 days are {20*calculation_to_seconds} seconds")
    user_days_input = input("Hey user, enter a number of days and I will convert it to hours\n")
    for num_of_days_element in user_days_input.split():
        validateAndExecute()


  

