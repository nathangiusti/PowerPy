import Report


def main():
    report = Report.Report('../PBIX/SLS_SRC_VAL.pbix')
    report.rename_table('SLS_SRC', 'Dim Sales Source')
    report.rename_table('SLS_SRC_VAL', 'Fact Sales Source Load Validation')
    report.rename_table('SLS_SRC_VAL_DATA', 'Fact Sales Source Load Validation Data')
    report.publish_pbix('../PBIX/MyNewPBIX.pbix')


if __name__ == "__main__":
    main()