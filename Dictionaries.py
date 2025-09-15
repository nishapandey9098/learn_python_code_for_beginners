"""Jan -> January
Feb -> February
Mar -> March
Apr -> April
May -> May      
Jun -> June
Jul -> July
Aug -> August   
Sep -> September
Oct -> October      
Nov -> November
Dec -> December """
 
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])  # This will print "November"
print(monthConversions.get("Dec"))  # This will print "December"    