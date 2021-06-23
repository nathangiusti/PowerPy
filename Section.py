import Visual


class Section:

    def __init__(self, parent, section_json):
        self.parent = parent
        self.section_json = section_json
        self.visuals = []
        for visual in section_json['visualContainers']:
            self.visuals.append(Visual.Visual(self, visual))

    def rename_section(self, new_name):
        self.section_json['displayName'] = new_name
