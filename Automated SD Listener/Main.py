######################################################
#                                                    #
#             Automated SD Restore Editor            #
#                                                    #
######################################################


import pandas, os, sys, getpass, time
import WebDriver, DataConfigure, DataGrab
from pathlib import Path


if __name__ == "__main__":
    data = pandas.read_excel(r'Data.xlsx')
    ldap_username = data.iloc[0]['Username']
    ldap_password = data.iloc[0]['Password']

    user = getpass.getuser()
    exported_tickets = ("C:\\Users\\" + str(user) + "\\Downloads\\export.xls")

    if Path(exported_tickets).is_file():
        os.remove(exported_tickets)
    if Path('configured_excel.xls').is_file():
        os.remove('configured_excel.xls')

    WebDriver.LoginToServiceDesk(ldap_username, ldap_password, first_time = True)

    time.sleep(3)

    DataConfigure.CreateExcel(exported_tickets)

    raw_data = pandas.read_excel('configured_excel.xls')

    all_restore = DataConfigure.CreateTicketList(raw_data, 433, first_time = True)

    first_time = True

    for incident in all_restore:
        WebDriver.LoginToServiceDesk(ldap_username, ldap_password)
        WebDriver.OpenIncident(incident)
        print("Incident # " + str(incident))
        is_vine3 = WebDriver.GrabIncidentInformation(ldap_username, ldap_password)
        if is_vine3 == "Yes":
            print("Is Vine 3, only Classic Vine VPOs are implemented\n")
        time.sleep(3)

    os.remove(exported_tickets)
    os.remove('configured_excel.xls')

    print("\nFinished collecting incident data and processing operations")

    WebDriver.Finish()
    sys.exit()
