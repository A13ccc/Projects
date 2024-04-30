import datetime, bday_messages


today = datetime.date.today()

my_next_birthday = datetime.date(2025, 1, 22)

days_away = my_next_birthday - today


if my_next_birthday == today:
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {days_away.days} days away!')
