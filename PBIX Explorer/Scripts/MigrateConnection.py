import Report

"""
Copies the connection of CONNECTION_SOURCE_PBIX_PATH to CONNECTION_DESTINATION_PBIX_PATH. 
Saves new PBIX to NEW_PBIX_PATH
"""

CONNECTION_SOURCE_PBIX_PATH = '../PBIX/Test_Poc_report.pbix'
CONNECTION_DESTINATION_PBIX_PATH = '../PBIX/DSM_Mix.pbix'
NEW_PBIX_PATH = '../PBIX/DSM_Mix_2.pbix'


def main():

    destination = Report.Report(CONNECTION_DESTINATION_PBIX_PATH)
    source = Report.Report(CONNECTION_SOURCE_PBIX_PATH)
    destination.connection = source.connection
    destination.publish_pbix(NEW_PBIX_PATH)


if __name__ == "__main__":
    main()
