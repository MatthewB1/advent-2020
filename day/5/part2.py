import numpy

file = open('input.txt', 'r')

# F,L = 0 - B,R = 1
boarding_passes = [i.replace('F', '0').replace('B', '1').replace(
    'L', '0').replace('R', '1').strip() for i in file.readlines()]


def calc_seat_id(row, col): return (row * 8) + col


def adjacent_seats_present(seatno):
    seat_below = int(seatno, 2) - 1
    seat_above = int(seatno, 2) + 1

    seat_below_bin = str(numpy.base_repr(seat_below, 2)).zfill(10)
    seat_above_bin = str(numpy.base_repr(seat_above, 2)).zfill(10)

    if seat_below_bin in boarding_passes and seat_above_bin in boarding_passes:
        return True

    return False


MIN_PASS = 0
MAX_PASS = 1023

for i in range(MIN_PASS, MAX_PASS + 1):
    binary_repr = str(numpy.base_repr(i, 2)).zfill(10)
    if binary_repr not in boarding_passes:
        if adjacent_seats_present(binary_repr):

            row = int(binary_repr[0:7], 2)
            col = int(binary_repr[7:10], 2)
            print(f'Found your seat! : {calc_seat_id(row, col)}')

        
