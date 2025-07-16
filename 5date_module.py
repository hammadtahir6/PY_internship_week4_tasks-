from datetime import datetime


birth_input = input("Enter your birth date : ")
birth_date = datetime.strptime(birth_input, "%Y-%m-%d")
today= datetime.now()
age = today.year - birth_date .year
days_lived = (today - birth_date).days
print(age)
print(days_lived)