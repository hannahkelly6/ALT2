import csv
#import pandas
import statistics

# Open and Create the file 
csvfile = open("screentimeALT2.csv", "w",newline = '')
print("File Created")
# Create column headers
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['First Name', 'Daily average screentime', 'Daily average screentime (decimal)', 'Screentime (Weekly)', 'Screentime (Weekly)(Decimal)', 'Day most used', 'Most used app'])
print("Columns Created")

# Create rows of data 
csvwriter.writerow(['Zofia', '5hrs 54mins', 5.9, '41hrs 22mins', 41.37, 'Monday', 'Youtube'])
csvwriter.writerow(['Emma', '3hrs 57mins', 3.95, '27hrs 44mins', 27.73, 'Monday', 'Tiktok'])
csvwriter.writerow(['Hannah', '5hrs 49mins', 5.82, '40hrs 45mins', 40.75, 'Monday', 'Tiktok'])
csvwriter.writerow(['Lydia', '3hrs 26mins', 3.43, '10hrs 21mins', 10.35, 'Monday', 'Instagram'])
csvwriter.writerow(['Ysabella', '5hrs 31mins', 5.52, '32hrs 00mins', 32, 'Saturday', 'Instagram'])
csvwriter.writerow(['Ella', '2hrs 21mins', 2.35, '16hrs 22mins', 16.37, 'Saturday', 'Snapchat'])
csvwriter.writerow(['Lianne', '4hrs 47mins', 4.78, '19hrs 8mins', 19.13, 'Wednesday', 'Snapchat'])
csvwriter.writerow(['Mia', '5hrs 33mins', 5.55, '38hrs 54mins', 38.9, 'Friday', 'Tiktok'])
csvwriter.writerow(['Eve', '10hrs 53mins', 10.88, '76hrs 17mins', 76.28, 'Monday', 'Youtube'])
csvwriter.writerow(['Haseena', '7hrs 25mins', 7.42, '29hrs 43mins', 29.72, 'Monday', 'Snapchat'])
csvwriter.writerow(['Juleanne', '8hrs 00mins', 8, '30hrs 00mins', 30, 'Monday', 'Google Chrome '])

print("Data Created")
# Close the file
csvfile.close()
print("closed after created rows")

#read and print the file in a loop
file = open("screentimeALT2.csv","r")
for x in file:
  print(x)
file.close()

"""
# Open the file read it and print the first 2 rows
csvfile = open("screentimeALT2","r")
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
line = csvfile.readline()
print(line, "readline4")
line = csvfile.readline()
print(line, "readline5")
line = csvfile.readline()
print(line, "readline6")
line = csvfile.readline()
print(line, "readline7")
line = csvfile.readline()
print(line, "readline8")
line = csvfile.readline()
print(line, "readline9")
line = csvfile.readline()
print(line, "readline10")
line = csvfile.readline()
print(line, "readline11")
line = csvfile.readline()
print(line, "readline12")
csvfile.close()
print("closed after printing rows")
"""
