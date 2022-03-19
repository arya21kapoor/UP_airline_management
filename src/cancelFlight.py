import sys

createBold = lambda s: '\033[1m' + str(s) + '\033[0m'

flightID = sys.argv[1]

with open('temp.txt', 'r') as fi:
    try:
        records = fi.read().split('\n')
    except:
        print('\nNo flight booking exists for this user')
        sys.exit()

if not records[0]:
    print('\nNo flight booking exists for this user.')
    sys.exit()

bookings = [r.split() for r in records[:-1]]

print("\n{0:10s} {1:10s} {2:10s}".format('Sr.No', 'Seat Type', 'Number of Seats'))
print('-'*35)

for i, b in enumerate(bookings,1):
    print("{0:<10d} {1:10s} {2:10s}".format(i, b[2], b[3]))

print ("\nEnter b to return to main menu\n")

while True:
    try:
        ans = input('Enter serial no. to delete: ')

        if not len(ans):
            print('Wrong input')
            continue

        if ans.lower()[0] == 'b':
            print('Returning to main menu')
            sys.exit()

        ans = int(ans)

        if ans >= 1 and ans <= len(bookings):
            break
        else:
            print('Out of range.')
    except ValueError:
        print('Only integer value required.')
        continue

print('\nFlight ID:', createBold(flightID))
print('Type of Seat: ', createBold(bookings[ans-1][2]))
print('Number of Seats: ', createBold(bookings[ans-1][3]))

confirm = input('\nEnter Yes to confirm cancellation: ')

if len(confirm) <= 0 or confirm[0].lower() != 'y':
    print('\nAborting cancellation')
    print('Returning to main menu')
    sys.exit()

print('Booking will be cancelled in a moment.')

d = ' '.join(bookings[ans-1])

with open('db.txt', 'r') as f:
    records = f.read().split('\n')

records.remove(d)

with open ('db.txt', 'w') as f:
    for r in records:
        f.write(r)
        f.write('\n')

flag = bookings[ans-1][2]
num = int(bookings[ans-1][3])

with open('flights.txt', 'r') as fi:
    flights = fi.read().split('\n')

for i in range(len(flights)):
    if flights[i].split(',')[0] == flightID:
        a = flights[i].split(',')
        if flag == 'Premium':
            a[5] = str(int(a[5]) + num)
        else:
            a[6] = str(int(a[6]) + num)
        flights[i] = ','.join(a)
        break
        

with open('flights.txt', 'w') as f:
    for r in flights:
        f.write(r)
        f.write('\n')

print('\nBooking cancelled successfully')
