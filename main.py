# variables for initial output
column_values = ["Code", "Text", "fil", "bcl"]
code_1 = ["Wins", "Panalo na!", "panalo", "gana"]
code_2 = ["Lose", "Talo na!", "talo", "daog"]
code_3 = ["Games", "Laro tayo", "laro", "kawat"]

# static presentation of the initial output
print("----------Start of Orignal Data----------")
print(f"| {column_values[0]}\t\t {column_values[1]}\t\t {column_values[2]}\t\t {column_values[3]}")
print(f"| {code_1[0]}\t\t{code_1[1]}\t{code_1[2]}\t\t{code_1[3]}")
print(f"| {code_2[0]}\t\t{code_2[1]}\t{code_2[2]}\t\t{code_2[3]}")
print(f"| {code_3[0]}\t\t{code_3[1]}\t{code_3[2]}\t\t{code_3[3]}")
print("----------End of Orignal Data----------\n")

# variables for data transformation(Column to Row)

transformed_columns = ["Code", "Culture", "Value"]
fil_bcl_translations_list = [
    {"Code": "Wins", "Values": ["panalo", "gana"], "Culture": ["fil", "bcl"]},
    {"Code": "Lose", "Values": ["talo", "daog"], "Culture": ["fil", "bcl"]},
    {"Code": "Games", "Values": ["laro", "kawat"], "Culture": ["fil", "bcl"]},
    {"Code": "Player", "Values": ["manlalaro", "parakawat"], "Culture": ["fil", "bcl"]}

]

# expected output(Column to row transformation)
print("----------Start of Transformed Data----------")
print(f"{transformed_columns[0]}\t  {transformed_columns[1]}\t  {transformed_columns[2]}")

for items in fil_bcl_translations_list:
    # default value of culture and values is 2
    if len(items['Values']) == 2 and len(items['Culture']) == 2:
        if items["Values"][0] != "" and items["Values"][1] != "" and items["Culture"][0] != "" and items["Culture"][1] != "":
            print(f"{items['Code']}\t\t{items['Culture'][0]}\t\t {items['Values'][0]}")
            print(f"{items['Code']}\t\t{items['Culture'][1]}\t\t {items['Values'][1]}")
        elif items["Values"][0] == "" and items["Values"][1] == "":
            continue
        elif items['Values'][0] == "" or items["Culture"][0] == "":
            print(f"{items['Code']}\t\t{items['Culture'][1]}\t\t {items['Values'][1]}")
        elif items['Values'][1] == "" or items["Culture"][1] == "":
            print(f"{items['Code']}\t\t{items['Culture'][0]}\t\t {items['Values'][0]}")

    # if property is added
    elif len(items['Values']) > 2 and len(items['Culture']) > 2:
        print(f"{items['Code']}\t\t{items['Culture'][0]}\t\t {items['Values'][0]}")
        print(f"{items['Code']}\t\t{items['Culture'][1]}\t\t {items['Values'][1]}")
        print(f"{items['Code']}\t\t{items['Culture'][-1]}\t\t {items['Values'][-1]}")
# dynamic transformation was created however on the dynamic part is not too consistent but, I'll still join
print("----------End of Transformed Data----------")
