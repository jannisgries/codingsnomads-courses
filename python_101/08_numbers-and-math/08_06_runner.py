# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

miles_ran = 10
km_ran = miles_ran * 1.6
minutes_ran = 30.5
km_per_minute = km_ran / minutes_ran
km_per_hour = km_per_minute * 60
print("average speed: " + str(km_per_hour)+ "km/h")