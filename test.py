dict_list = []
new_dict_list_with_matches = []

weights = {
        'Smoking,Drinking':7,
        'Pets':4,
        'EarlyBed':3,
        'gender':2
    }




def mass_prefrence(n):
    

    for i in range(n):
        prefrence = {}

        a = input("Enter user name-> ")
        prefrence['name'] = a
        
        a = input("Do you like your partner to smoke,drink?-> y/n ")
        if (a == "y"):
            prefrence["Smoking,Drinking"] = 1
        else:
            prefrence["Smoking,Drinking"] = 0

        a = input("Do you like your partner have pets?-> y/n ")
        if (a == "y"):
            prefrence["Pets"] = 1
        else:
            prefrence["Pets"] = 0

        a = input("Do you like your partner to be a early riser?-> y/n ")
        if (a == "y"):
            prefrence["EarlyBed"] = 1
        else:
            prefrence["EarlyBed"] = 0

        a = input("Do you like your partner to be of same gender?-> y/n ")
        if (a == "y"):
            prefrence["gender"] = 1
        else:
            prefrence["gender"] = 0

        dict_list.append(prefrence)

def match_or_not(prefrence1,prefrence2,threshold=0):
    total_score = 0
    for key,values in prefrence1.items():
        if key in weights:
            weight_score = (values == prefrence2[key]) * weights[key]
            total_score += weight_score

    match_score = total_score / 16.0


    new_key_value_1 = prefrence2["name"] + "_match"
    new_key_value_2 = prefrence1["name"] + "_match"

    prefrence1[new_key_value_1] = match_score
    prefrence2[new_key_value_2] = match_score

    new_dict_list_with_matches.append(prefrence1)
    new_dict_list_with_matches.append(prefrence2)

def calculate_and_show():
    for i in range(len(dict_list)):
        for j in range(i+1,len(dict_list)):
            match_or_not(dict_list[i],dict_list[j])

    for data in new_dict_list_with_matches:
        for key,values in data.items():
            print(f"{key} : {values}")
    
        
    



if __name__ == '__main__':
    a = input("enter how many users you wish to add-> ")
    mass_prefrence(int(a))
    calculate_and_show()

    






    
        

        


