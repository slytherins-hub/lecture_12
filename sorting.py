import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
        return data


def selection_sort(data_list, direction):
    if not data_list:
        return -1

    if direction:
        i = 0
        while i < len(data_list):
            n = i
            while n < len(data_list):
                if data_list[n] < data_list[i]:
                    data_list[n], data_list[i] = data_list[i], data_list[n]
                n += 1
            i += 1
    else:
        i = 0
        while i < len(data_list):
            n = i
            while n < len(data_list):
                if data_list[n] > data_list[i]:
                    data_list[n], data_list[i] = data_list[i], data_list[n]
                n += 1
            i += 1

    return data_list


def main():
    data = read_data("numbers.csv")
    print(data["series_1"])
    print(selection_sort(data["series_1"], True))
    print(selection_sort(data["series_1"], False))
    print(data)


if __name__ == '__main__':
    main()
