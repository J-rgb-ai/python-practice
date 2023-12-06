#Problem : Recieve miles and convert to kilometres
#kilometers =  miles * 1.60934
#Enters Miles 5
#5 miles equals 8.04 kilometres


#Ask the user  to input miles and assign it to he miles variable
miles = input('enter the number: ')

#Convert from strring to integer
miles = int(miles)

#Perfom calculation by multiplying 1.60934
kilometers = miles * 1.60934

#iPrint the results using format
print("{} * {} = {}".format(miles, 1.60934, kilometers))
