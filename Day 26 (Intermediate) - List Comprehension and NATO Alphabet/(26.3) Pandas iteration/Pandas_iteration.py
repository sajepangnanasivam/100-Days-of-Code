import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


for (key, value) in student_dict.items():
    print(value)

student_dataframe = pd.DataFrame(student_dict)
print(student_dataframe)

# Loop through the Dataframe
for (key, value) in student_dataframe.items():
    print(value)

# Loop through rows of a Dataframe
for (index, row) in student_dataframe.iterrows():
    print(row.score)
    print(row.student)
