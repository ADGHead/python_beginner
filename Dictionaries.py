# A dictionary is a special structure in python that is used to store key value pairs

month_conversions = {
    "Jan" : "January",
    "Feb" : "Febuary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(month_conversions["Nov"])
print(month_conversions.get("Dec"))
print(month_conversions. get("Crack", "Not a valid key"))
#print({**month_conversions})
for v in month_conversions.values():
    print(v)