import pandas as pd

data = pd.read_csv('cuisines.csv')
data.columns = ['name', 'image_url', 'description', 'cuisine', 'course', 'diet','prep_time', 'ingredients', 'instructions']
data=data.head(500)

name_data = data["name"].tolist()
image_url_data =data["image_url"].tolist()
description_data = data["description"].tolist()
cuisine_data = data["cuisine"].tolist()
course_data = data["course"].tolist()
diet_data = data["diet"].tolist()
prep_time_data = data["prep_time"].tolist()
ingredients_data = data["ingredients"].tolist()
instructions_data = data["instructions"].tolist()

# NAME
print(name_data)

# 2 IMAGE URL
print(image_url_data)

# 3 DESCRIPTION
print(description_data)

# 4 CUISINE
print(cuisine_data)
cuisine_set_data = set(cuisine_data)

print(len(cuisine_data)," -  number of cuisines from index")
print(len(cuisine_set_data)," - Total cuisines in dataset\n below are as follows : \n")
print(cuisine_set_data)


# 5 COURSE
print(course_data)
course_set_data = set(course_data)

print(len(course_data)," -  number of course from index")
print(len(course_set_data)," - Total course in dataset\n below are as follows : \n")
print(course_set_data)

# 6 DIET
print(diet_data)
diet_set_data = set(diet_data)

print(len(diet_data)," -  number of diet from index")
print(len(diet_set_data)," - Total diet in dataset\n below are as follows : \n")
print(diet_set_data)

# 7 PREP TIME
print(prep_time_data)
prep_time_set_data = set(prep_time_data)

print(len(prep_time_data)," -  number of prep time from index")
print(len(prep_time_set_data)," - Total prep time in dataset\n below are as follows : \n")
print(prep_time_set_data)

# 8 INGREDIENTS
print(ingredients_data)
ingredients_set_data = set(ingredients_data)

print(len(ingredients_data)," -  number of ingredients from index")
print(len(ingredients_set_data)," - Total ingredients in dataset\n below are as follows : \n")
print(ingredients_set_data)

# 9 INSTRUCTIONS
print(instructions_data)

# Dataframe
df = pd.DataFrame({"Name": name_data, "Image Url": image_url_data, "Description": description_data, "Cuisine": cuisine_data, "Course": course_data, "Diet": diet_data, "Prep Time": prep_time_data,"Ingredients": ingredients_data, "Instructions": instructions_data })
df['Ingredients'] = df['Ingredients'].str.strip()  # removing usless characters or spaces from "Ingredients"

print(df)

df.to_csv('New Cuisine data.csv', index = False)

df.isnull().sum()

df.info()
df.describe()

