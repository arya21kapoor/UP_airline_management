#! /usr/bin/python

import sys

createBold = lambda s: '\033[1m' + str(s) + '\033[0m'

userID = sys.argv[1]
flightID = sys.argv[2]

with open('flights.txt', 'r') as fi:
    records = fi.read().split('\n')

flightInfo = {
        'flightID' : flightID,
        'Flight Carrier' : None,
        'Source': None,
        'Destination' : None,
        'Date' : None,
        'Premium' : None,
        'Economy'  : None
}

for r in records:
    if r.split(',')[0] == flightID :
        l = r.split(',')

        flightInfo['Flight Carrier'] = l[1]
        flightInfo['Source'] = l[2]
        flightInfo['Destination'] = l[3]
        flightInfo['Date'] = l[4]
        flightInfo['Premium'] = int(l[5])
        flightInfo['Economy'] = int(l[6])

        break
        
print(f'1 - Premium Seats ({flightInfo["Premium"]})')
print(f'2 - Economy Seats ({flightInfo["Economy"]})')
print(f'3 - Go back to Main Menu')

while True:
    choice = int(input('\nEnter Choice: '))

    if choice not in [1, 2, 3]:
        print('Wrong option')
    else:
        break
        
if choice == 3:
    sys.exit()

flag = 'Premium' if choice == 1 else 'Economy'

if not flightInfo[flag] > 0:
    print(f'{flag} seats not available')
    print('Going back to Main Menu')
    sys.exit()

print('\nEnter b to return to main menu')
while True:
    try:
        ans = input('\nEnter number of Seats (max 4): ')
        
        if ans == 'b':
            print('Going back to Main Menu')
            sys.exit()
            break
        
        num = int(ans)     
       
        if num < 0 or num > 4:
            print('Wrong number of seats')
        elif flightInfo[flag] < num:
            print(f'Only {flightInfo[flag]} seat(s) are remaining')
        else:
            break
    except (TypeError, ValueError):
        print('Please enter integer value')

print('\nPlease confirm the following details to book the flight: \n')

print('Flight ID =', createBold(flightInfo['flightID']))
print('Flight Carrier =',createBold(flightInfo['Flight Carrier']))
print('Source =', createBold(flightInfo['Source']))
print('Destination =', createBold(flightInfo['Destination']))
print('Date =', createBold(flightInfo['Date']))
print('Type of Seat =', createBold(flag))
print('Number of Seats =', createBold(num))

confirm = input('\nEnter Yes to confirm: ')

if len(confirm) <= 0 or confirm[0].lower() != 'y':
    print('\nCancelling transaction')
    print('Returning to main menu')
    sys.exit()

for i in range(len(records)):
    if records[i].split(',')[0] == flightID:
        a = records[i].split(',')
        if flag == 'Premium':
            a[5] = str(int(a[5]) - num)
        else:
            a[6] = str(int(a[6]) - num)
        records[i] = ','.join(a)
        break
        
with open('flights.txt', 'w') as f:
    for r in records:
        f.write(r)
        f.write('\n')

with open ('db.txt', 'a') as f:
    f.write(f'{userID} {flightID} {flag} {num}')
    f.write('\n')

print('Successful')
