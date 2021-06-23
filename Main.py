import Report


def main():
    report = Report.Report('PBIX/TestFile.pbix')
    report.add_section('My new section')
    sections = report.get_sections()
    sections[0].rename_section('I did it')
    report.publish_pbix('PBIX/MyNewPBIX.pbix')


if __name__ == "__main__":
    main()