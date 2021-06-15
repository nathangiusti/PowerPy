import json
import os
import shutil

import zipfile

import Section


class Report:

    def __init__(self, power_bi_file_location, working_folder='temp'):
        file_name = os.path.splitext(os.path.basename(power_bi_file_location))[0]
        self.folder = working_folder + '/' + file_name
        with zipfile.ZipFile(power_bi_file_location, 'r') as zip_ref:
            zip_ref.extractall(self.folder)
        with open(self.folder + '/Report/Layout', encoding='utf-16-le') as f:
            self.layout = json.loads(f.readlines()[0])
        self.sections = []
        for section in self.layout['sections']:
            self.sections.append(Section.Section(self, section))

    def publish_pbix(self, save_file_location):
        section_json = []
        for section in self.sections:
            section_json.append(section.section_json)
        self.layout['sections'] = section_json
        with open(self.folder + '/Report/Layout', "w", encoding='utf-16-le') as f:
            json.dump(self.layout, f)
        dir = os.path.splitext(save_file_location)[0]
        ext = os.path.splitext(save_file_location)[1]
        with open(self.folder + '/[Content_Types].xml') as f:
            content = f.readlines()[0]
            content = content.replace("<Override PartName=\"/SecurityBindings\" ContentType=\"\" />", "")

        with open(self.folder + '/[Content_Types].xml', "w") as f:
            f.write(content)

        os.remove(self.folder + "/SecurityBindings")

        shutil.make_archive(dir, 'zip', self.folder)
        ext = '.pbix' if len(ext) == 0 else ext
        if os.path.exists(dir + ext):
            os.remove(dir + ext)
        os.rename(dir + ".zip", dir + ext)

    def get_sections(self):
        return self.sections
