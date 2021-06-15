class Section:
    def __init__(self, parent, section_json):
        self.parent = parent
        self.section_json = section_json

    def rename_section(self, new_name):
        self.section_json['displayName'] = new_name
