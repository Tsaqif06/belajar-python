hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins += dura
hour += mins // 60

mins %= 60
hour %= 24

print(hour, ":" , mins, sep="")