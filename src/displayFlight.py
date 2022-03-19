import sys

flightID = sys.argv[1]
createBold = lambda s: '\033[1m' + str(s) + '\033[0m'

class FlightBookingInfo:
    def __init__(self, seat_type, num_seats):
        self.seat_type =  seat_type
        self.num_seats = num_seats

bookings = []
info = {'Flight Carrier' : None, 'Source' : None, 'Destination' : None, 'Date' : None}

with open('temp.txt', 'r') as fi:
    try:
        records = fi.read().split('\n')
    except:
        print('\nNo flight booking exists for this user')
        sys.exit()

if not records[0]:
    print('\nNo flight booking exists for this user.')
    sys.exit()

records = [r.split() for r in records[:-1]]
bookings = [FlightBookingInfo(r[2], r[3]) for r in records]


with open('flights.txt', 'r') as fi:
    flights = fi.read().split('\n')

for f in flights:
    if f.split(',')[0] == flightID :
        l = f.split(',')
        info['Flight Carrier'] = l[1]
        info['Source'] = l[2]
        info['Destination'] = l[3]
        info['Date'] = l[4]
        break
print()
print('Flight ID =', createBold(flightID))
print('Flight Carrier =', createBold(info['Flight Carrier']))
print('Source = ', createBold(info['Source']))
print('Destination = ', createBold(info['Destination']))
print('Date = ', createBold(info['Date']))

print()

print("\n{0:10s} {1:10s} {2:10s}".format('Sr.No', 'Seat Type', 'Number of Seats'))
print('-'*35)

for i, b in enumerate(bookings,1):
    print("{0:<10d} {1:10s} {2:10s}".format(i, b.seat_type, b.num_seats))
