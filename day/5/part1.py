file = open('input.txt', 'r')

# F,L = 0 - B,R = 1
boarding_passes = [i.replace('F', '0').replace('B', '1').replace(
    'L', '0').replace('R', '1').strip() for i in file.readlines()]

highest_seat_ID = 0
def calc_seat_id(row, col): return (row * 8) + col

for boarding_pass in boarding_passes:
    #First 7 chars row no. - Last 3 chars col no.
    row, col = int(boarding_pass[0:7], 2), int(boarding_pass[7:10], 2)
    if calc_seat_id(row, col) > highest_seat_ID:
        highest_seat_ID = calc_seat_id(row, col)

print(f'Highest seat ID : {highest_seat_ID}')



