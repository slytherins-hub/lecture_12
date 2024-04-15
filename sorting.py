import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return data: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {}

    with open(file_path, "r") as file_obj:
        reader = csv.DictReader(file_obj)

        for row in reader:

            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))

    return data


def selection_sort(numbers, direction='ascending'):
    """
    Sort all elements of the sequence according to the principles of Selection Sort.
    :param numbers: (list) sequence of numbers
    :param direction: (str) direction of sorting, 'ascending' or 'decending'
    :return numbers: (list) sorted sequence of numbers according to descending param
    """
    for i in range(len(numbers)):

        min_idx = i
        max_idx = i

        if direction == 'ascending':

            for j in range(i + 1, len(numbers)):
                if numbers[min_idx] > numbers[j]:
                    min_idx = j

            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

        elif direction == 'descending':

            for j in range(i + 1, len(numbers)):
                if numbers[max_idx] < numbers[j]:
                    max_idx = j

            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

        else:
            print('Please select "descending" or "ascending" option for selection_sort(number_list,___')
            quit()

    return numbers


def main():
    read_data('numbers.csv')


if __name__ == '__main__':
    main()
