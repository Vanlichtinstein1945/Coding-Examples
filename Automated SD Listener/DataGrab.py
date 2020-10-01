import os, glob
from datetime import datetime

def grab_vpo(agency, CI):
    print('Beginning triage\n')
    temp_state = ""
    temp_agency = ""
    count = 0
    starting = True
    for letter in agency:
        if count == 0 and letter == " ":
            count += 1
            starting = False
        elif starting == True:
            temp_state += letter
        elif count == 1 and letter != " ":
            temp_agency += letter
        elif count == 1 and letter == " ":
            break
    agency_state = temp_state.lower()
    agency_name = temp_agency.lower()
    if agency_state == "ok":
        list_of_files = glob.glob('P:\\project\\vpo\\ok\\okstate\\ok' + str(agency_name) + 'vpo\\ftphome\\kellpro_ftp_import\\source_archive\\*')
        latest_file = max(list_of_files, key=os.path.getctime)
        print('Last file import ' + datetime.fromtimestamp(os.path.getmtime(latest_file)).strftime('%Y-%m-%d %H:%M:%S') + '\n')
        f = open('P:\\project\\vpo\\ok\\okstate\\ok' + str(agency_name) + 'vpo\\ftphome\\kellpro_ftp_import\\log\\vpo_ftp.log', "r")
        contents = f.read().splitlines()
        i = 0
        for line in reversed(contents):
            if i == 0:
                print('Logs look good: \n\n"' + line)
            else:
                print(line)
            i += 1
            if "Starting" in line:
                if not i < 5:
                    print('"')
                    break
    elif agency_state == "wi":
        temp_list = []
        count = 0
        copy = False
        temp_str = ""
        for i in CI:
            temp_list += i
        for i in temp_list:
            if copy == True and i != ':':
                temp_str += i
            if i == ":" and count == 0:
                copy = True
                count += 1
            elif i == ":" and count == 1:
                copy = False
                count += 1
        agency_number = temp_str
        config_file = ('P:\\project\\vpo\\wi\\wistate\\ftphome\\counties\\' + str(agency_number) + '\\config.prop')
        print('Config.prop still up to date as of ' + datetime.fromtimestamp(os.path.getmtime(config_file)).strftime('%Y-%m-%d %H:%M:%S') + '\n')
        getrecords_logs = glob.glob('P:\\project\\vpo\\wi\\wistate\\ftphome\\counties\\' + str(agency_number) + '\\log\\getRecords\\*')
        latest_getrecord = max(getrecords_logs, key=os.path.getctime)
        getrecord_log = open(latest_getrecord)
        gr_logs = getrecord_log.read().splitlines()
        i = 0
        for line in reversed(gr_logs):
            if i == 0:
                print('GetRecords log looks good: \n\n"' + line)
            else:
                print(line)
            i += 1
            if "[BEGIN]" in line:
                if not i < 5:
                    print('"\n\n\n')
                    break
        prerun_logs = glob.glob('P:\\project\\vpo\\wi\\wistate\\ftphome\\counties\\' + str(agency_number) + '\\log\\prerun\\*')
        latest_prerun = max(prerun_logs, key=os.path.getctime)
        prerun_log = open(latest_prerun)
        pr_logs = prerun_log.read().splitlines()
        i = 0
        for line in reversed(pr_logs):
            if i == 0:
                print('Prerun log looks good: \n\n"' + line)
            else:
                print(line)
            i += 1
            if "BEGIN" in line:
                if not i < 5:
                    print('"')
                    return None
    else:
        print("Only OK and WI VPOs are built in currently.\n")

def grab_ae(username, password):
    print("Only VPOs are implemented\n")

def grab_dfr(username, password):
    print("Only VPOs are implemented\n")
