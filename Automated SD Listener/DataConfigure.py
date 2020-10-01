######################################################
#                                                    #
#             Automated SD Restore Editor            #
#                                                    #
######################################################

import io, pandas
from xlwt import Workbook

def CreateExcel(file):
    initial_file = io.open(file, 'r', encoding='utf-8')
    extracted_data = initial_file.readlines()

    excel_document = Workbook()

    excel_sheet = excel_document.add_sheet("Sheet1", cell_overwrite_ok=True)

    for i, row in enumerate(extracted_data):
        for j, val in enumerate(row.replace('\n', '').split('\t')):
            excel_sheet.write(i, j, val)

    excel_document.save('configured_excel.xls')

def CreateTicketList(base_table, max_length, first_time = False):
    global full_incident_list

    if first_time:
        full_incident_list = []

    temp_incident = get_incident_number(base_table, max_length)
    full_incident_list.append(temp_incident)
    if not max_length + 76 > len(base_table):
        CreateTicketList(base_table, max_length+76)
    for entry in full_incident_list:
        if entry == "":
            temp_num = full_incident_list.index(entry)
            del full_incident_list[temp_num]
    return full_incident_list

def get_incident_number(table, line):
    raw_incident_number = table.iloc[line]

    incident_number_list = []
    temp_str = ""
    start_number = False
    count = 0

    for i in raw_incident_number:
        for x in i:
            incident_number_list.append(x)
    for i in incident_number_list:
        if start_number:
            if i == "]":
                start_number = False
            else:
                temp_str += str(i)
        else:
            if i == "[":
                count += 1
            if i == "[" and count == 2:
                start_number = True

    return temp_str
