import Report


TEAM_LIST_ARR = [
    'ATLANTA REIGN',
    'BOSTON UPRISING',
    'CHENGDU HUNTERS',
    'DALLAS FUEL',
    'FLORIDA MAYHEM',
    'GUANGZHOU CHARGE',
    'HANGZHOU SPARK',
    'HOUSTON OUTLAWS',
    'LONDON SPITFIRE',
    'LOS ANGELES GLADIATORS',
    'LOS ANGELES VALIANT',
    'NEW YORK EXCELSIOR',
    'PARIS ETERNAL',
    'PHILADELPHIA FUSION',
    'SAN FRANCISCO SHOCK',
    'SEOUL DYNASTY',
    'SHANGHAI DRAGONS',
    'TORONTO DEFIANT',
    'VANCOUVER TITANS',
    'WASHINGTON JUSTICE'
]


def main():
    report = Report.Report('../PBIX/OWL ELO.pbix')
    report.publish_pbix('../PBIX/MyNewPBIX.pbix')


if __name__ == "__main__":
    main()