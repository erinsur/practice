import datetime
import math

def get_birth_month_and_year(user_age):
    # todays date
    today = datetime.datetime.now()

    # user's decimal age -> split into year and month
    year, month = divmod(user_age, 1)
    month = math.floor((month) * 12)


    year_born = int(today.strftime("%Y")) - year
    month_born = int(today.strftime("%m")) - month

    if month_born <= 0:
        year_born -= 1
        month_born += 12

   
    user_birthday = datetime.datetime(int(year_born), int(month_born), 1)

    print(f'You are born in {user_birthday.strftime("%B")} of {user_birthday.strftime("%Y")}')


def get_decimal_age (month, year):
    # todays date
    today = datetime.datetime.now()

    # 2025- 2005 = 20
    year_age = int(today.strftime("%Y")) - year

    month_age = int(today.strftime("%m")) - month

    if month_age <= 0:
        year_age -= 1
        month_age += 12
    
    month_age  = round(month_age / 12, 1)

    print(f"Your age is {month_age + year_age}")

get_birth_month_and_year(199.9)
get_decimal_age(9,1914)