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


def selection_sort(numbers_list):
    """

    :param numbers_list:
    :return:
    """
    for i in range(len(numbers_list)):

        min_idx = i
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[min_idx] > numbers_list[j]:
                min_idx = j

        numbers_list[i], numbers_list[min_idx] = numbers_list[min_idx], numbers_list[i]

    return numbers_list


def main():
    read_data('numbers.csv')


if __name__ == '__main__':
    main()
