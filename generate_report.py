#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    # f = open(csv_file_location)
    # reader = csv.DictReader(f) # DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.

    #We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object. Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. We will now register a dialect empDialect.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True) #The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('employees.csv')
# print(employee_list)

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
            department_list.append(employee_data['Department'])  
        department_data = {}
        for department_name in set(department_list):
            department_data[department_name] = department_list.count(department_name)
        return department_data
    
dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()
write_report(dictionary, 'report.txt')