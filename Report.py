import json
import time

import zipfile

import Section


class Report:

    def __init__(self, power_bi_file_location: str):
        self.zip_file = zipfile.ZipFile(power_bi_file_location)
        self.layout = json.loads(self.zip_file.read('Report/Layout').decode('utf-16-le'))

        self.sections = []
        for section in self.layout['sections']:
            self.sections.append(Section.Section(self, section))
        self.ordinal_counter = len(self.sections) - 1

    def publish_pbix(self, save_file_location: str) -> None:
        section_json = []
        for section in self.sections:
            section_json.append(section.export_section_json())
        self.layout['sections'] = section_json

        with zipfile.ZipFile(save_file_location, 'w') as zout:
            for item in self.zip_file.infolist():
                if item.filename == 'Report/Layout':
                    zout.writestr(item, json.dumps(self.layout).encode('utf-16-le'))
                elif item.filename == '[Content_Types].xml':
                    content = self.zip_file.read(item.filename).decode('utf-8')
                    content = content.replace("<Override PartName=\"/SecurityBindings\" ContentType=\"\" />", "")
                    zout.writestr(item, content)
                elif item.filename == 'SecurityBindings':
                    continue
                else:
                    zout.writestr(item, self.zip_file.read(item.filename))

    def get_sections(self) -> [Section.Section]:
        return self.sections

    def add_section(self, display_name: str, *, width=1280, height=720) -> None:
        section_json = {'name': "ReportSection" + str(time.time_ns()), 'displayName': display_name, 'filters': [],
                        'ordinal': self.ordinal_counter, 'visualContainers': [], 'config': "{}", 'displayOption': 1,
                        'width': width, 'height': height}
        self.ordinal_counter += 1
        new_section = Section.Section(self, section_json)
        self.sections.append(new_section)
        return new_section


