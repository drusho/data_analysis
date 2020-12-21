import datetime as dt

random_date = "12/24/2020"
random_date = dt.datetime.strptime(random_date, "%m/%d/%Y")

day = random_date.day
month = random_date.month
year = random_date.year


rearrange_date = "{}/{}/{}".format(year, month, day)
print(rearrange_date)
