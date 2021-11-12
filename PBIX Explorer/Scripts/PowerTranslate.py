
import openpyxl
import sys

# PowerTranslate.io is a great site for converting between languages in a dashboard.
# To manually translate a PBIX you must fill out an excel template.
# If the dashboard is updated you must use a new translation file.

# Usage
# python ExportToJson.py [pbix file location] [output file location]
# Ex: python ExportToJson.py Folder/MyPbixFile.pbix MyReportJson.json


def main():

    original = 'TestFiles/translations.xlsx'  # sys.argv[1]
    updated = 'TestFiles/translations_new.xlsx'  # sys.argv[2]
    output = 'TestFiles/translations_new_new.xlsx'
    original_wbs = openpyxl.load_workbook(filename=original).active
    updated_wb = openpyxl.load_workbook(filename=updated)
    updated_wbs = updated_wb.active
    i = 2
    wb_dict = {}
    while original_wbs['A' + str(i)].value is not None:
        wb_dict[original_wbs['A' + str(i)].value] = original_wbs['B' + str(i)].value
        i += 1

    i = 2
    while updated_wbs['A' + str(i)].value is not None:
        key = updated_wbs['A' + str(i)].value
        if key in wb_dict.keys():
            updated_wbs['B' + str(i)] = wb_dict[key]
        i += 1

    updated_wb.save('TestFiles/translations_new_new.xlsx')

if __name__ == "__main__":
    main()