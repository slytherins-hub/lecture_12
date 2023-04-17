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


def bubble_sort(data_list):
    if not data_list:
        return -1

    swaped = True
    i = 0
    while swaped and i < 1000:
        swaped = False
        n = 0
        while n < len(data_list):
            if n+1 < len(data_list) and data_list[n] > data_list[n+1]:
                data_list[n], data_list[n+1] = data_list[n+1], data_list[n]
                swaped = True
            n += 1
        i += 1

    return data_list


def main():
    data = read_data("numbers.csv")
    print("series_1:", data["series_1"])
    print("Selection Sort upwards on series_1:", selection_sort(data["series_1"], True))
    print("Selection Sort downwards on series_1:", selection_sort(data["series_1"], False))

    print("\n series_2:", data["series_2"])
    print("Bubble Sort on series_2:", bubble_sort(data["series_2"]))
    #print("\n", data)


if __name__ == '__main__':
    main()
