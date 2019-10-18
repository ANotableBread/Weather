import csv
from datetime import datetime

def print_results(writer, list):
    list.reverse()
    writer.write("start: ")
    writer.write(str(list[0]))
    writer.write("; end: ")
    writer.write(str(list[-1]))
    writer.write("; max: ")
    writer.write(str(max(list)))
    writer.write("; min: ")
    writer.write(str(min(list)))
    writer.write('\n')

def process_csv(reader, writer):
    read = csv.reader(reader)
    read.next()
    reset_date = True
    initial_date, current_date = 0, 0
    foster, oak, street = [], [], []

    for row in read:
        # I'm assuming that each day has at least 2 entries; this should only fail when a day has just one entry
        if reset_date:
            initial_date = datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p').date()
            current_date = initial_date
            reset_date = False
        else:
            current_date = datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p').date()
        # Print when the date changes
        if current_date != initial_date:
            writer.write("Date: ")
            writer.write(str(initial_date))
            writer.write('\n')
            # Make sure that the station reported for that day
            if foster:
                writer.write("Foster Street; ")
                print_results(writer, foster)
            if oak:
                writer.write("Oak Street; ")
                print_results(writer, oak)
            if street:
                writer.write("63rd Street; ")
                print_results(writer, street)

            del foster[:]
            del oak[:]
            del street[:]
            reset_date = True

        if row[0].startswith('6'):
            street.append(float(row[2]))
        elif row[0].startswith('F'):
            foster.append(float(row[2]))
        else:
            oak.append(float(row[2]))

    # The loop won't print the values of the final day, so print it here
    writer.write("Date: ")
    writer.write(str(initial_date))
    writer.write('\n')

    if foster:
        writer.write("Foster Street; ")
        print_results(writer, foster)
    if oak:
        writer.write("Oak Street; ")
        print_results(writer, oak)
    if street:
        writer.write("63rd Street; ")
        print_results(writer, street)