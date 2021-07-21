import Report


def main():
    report = Report.Report('PBIX/TestFile.pbix')
    report.add_section('My new section')
    sections = report.get_sections()
    sections[0].rename_section('I did it')
    section = report.get_sections()[0]
    slicer = section.get_visuals_by_type('slicer')[0]
    slicer.set_slicer_value('Zarya')
    report.publish_pbix('PBIX/MyNewPBIX.pbix')


if __name__ == "__main__":
    main()