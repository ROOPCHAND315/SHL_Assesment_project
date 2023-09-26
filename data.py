import pandas as pd

# df = pd.read_excel("C:/Users/callM/Downloads/Parsed_FE Interviews_Cleaned.xlsx")
df = pd.read_excel(r"C:\Users\callM\Downloads\Parsed_FE Interviews_Cleaned.xlsx")

# Initialize an empty list to store project data
project_data = []

# Iterate through the rows of the DataFrame and convert data
for index, row in df.iterrows():
    project = {
        "title": row["Project.Title"],
        "technologies": row["Project.Technologies"],
        "frontend": row["Technical_Skillset.Frontend"],
        "backend": row["Technical_Skillset.Backend"],
        "databases": row["Technical_Skillset.Databases"],
        "infrastructure": row["Technical_Skillset.Infrastructre"],
    }
    project_data.append(project)

# Print the converted project_data list
for project in project_data:
    print(project)
