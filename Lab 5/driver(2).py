from Theater import *

#Driver to test the Theater class
def main():
    #Tests constructor
    local_theater = Theater(20, 20)

    #Tests __str__()
    print("Original size of theater:")
    print(local_theater)

    #Tests set_size
    local_theater.set_size(10, 20)
    print("Smaller size of theater:")
    print(local_theater)

    #Tests sell_seat
    print("Selling one ticket:  Seat 5 on Row 3")
    if local_theater.sell_seat(3, 5):
        print(local_theater)
    else:
        print("Seat has already been sold")
        print(local_theater)

    #Tests to make sure that a seat may not be sold more than once
    print("Shouldn't be able to sell the ticket again.")
    if local_theater.sell_seat(3, 5):
        print(local_theater)
    else:
        print("Seat has already been sold")
        print(local_theater)

    #Sell lots of seats
    count = 1
    while count <= 5:
        count2 = 1
        while count2 <= 8:
            if local_theater.sell_seat(count, count2):
                print("Sold: ", count, count2)
            else:
                print("Didn't sell: ", count, count2)
            count2 += 1
        count += 1

    print("Small theater after selling lots of tickets:")
    print(local_theater)
    return

main()
