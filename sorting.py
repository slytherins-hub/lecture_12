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

    with open(file_path) as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
        return data

def selection_sort(values):
    n = len(values)
    for i in range(n):
        min_idx = i
        for num_idx in range(i+1, n):
            if values[num_idx] < values[min_idx]:
                min_idx = num_idx
        values[i], values[min_idx] = values[min_idx], values[i]
    return values


def main():
    pass

def selection_sort_2(values):
    go = 0
    while go != len(values):
        i = 0
        for index, value in enumerate(values):
            if value == min(values[i:]):
                values[i], values[index] = values[index], values[i]
                i += 1
            else:
                pass
        go += 1
    return values

def bubble_sorting_2(values):
    index = 0
    go = 0
    while go != len(values):
        if values[index] > values[index+1]:
            values[index], values[index+1] = values[index+1], values[index]
            index += 1

        if index == (len(values) - 2):
            go += 1
            index = 0
        else:
            index += 1
            pass
    return values

if __name__ == '__main__':
    my_data = read_data('numbers.csv')
    print(my_data['series_2'])
    values = my_data['series_2'].copy()
    values_2 = my_data['series_1'].copy()
    values_3 = my_data['series_3'].copy()
    print(selection_sort(values))
    print('\n')
    print(values_2)
    print(selection_sort_2(values_2))
    print('\n')
    print(values_3)
    print(bubble_sorting_2(values_3))


    '''
        minimum = 100
        for index, value in enumerate(values):
            if value <= minimum:
                minimum = value
                minimum_index = index
            else:
                pass



        i = 0
    
        for index, value in enumerate(values):
            if value == min(values[i:]):
                values[i], values[index] = values[index], values[i]
                i += 1
            else:
                pass
        return values
        '''

