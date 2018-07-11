def make_tags(x,y):
    print('<{}>{}</{}>'.format(x,y,x))
make_tags(x = 'i', y = 'Yay')
make_tags(x = 'i', y = 'Hello')
make_tags(x = 'cite', y = 'Yay')

def oddoreven(num):
    if num % 2 == 0:
        print ('Even')
    else:
        print ('Odd')
oddoreven(num = 27)

def sleepin(day):
    if day == "Saturday" or "Sunday":
        print ('You can sleep in.')
    else:
        print ("You can't sleep in and have to go to work.")
sleepin (day = "Saturday")
