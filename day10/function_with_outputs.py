 # Function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide vaild inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"
f_name = input("What is Yor Name ?")
l_name = input("What last name?")

formated_string = format_name(f_name, l_name)
print(formated_string)
 