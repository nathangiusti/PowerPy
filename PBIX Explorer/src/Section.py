import copy
import json

import Report
import Visual


class Section:

    def __init__(self, parent: Report, section_json):
        self.parent = parent
        self.section_json = section_json
        self.visuals = []
        for visual in section_json['visualContainers']:
            self.visuals.append(Visual.Visual(self, visual))

    def rename_section(self, new_name: str) -> None:
        self.section_json['displayName'] = new_name

    def get_visuals_by_type(self, visual_type: str) -> [Visual]:
        ret_arr = []
        visual_type = visual_type.lower()
        for visual in self.visuals:
            if visual.get_visual_type() == visual_type:
                ret_arr.append(visual)
        return ret_arr

    def export_section_json(self) -> json:
        ret_json = []
        for visual in self.visuals:
            ret_json.append(visual.export_visual_json())
        self.section_json['visualContainers'] = ret_json
        return copy.deepcopy(self.section_json)


