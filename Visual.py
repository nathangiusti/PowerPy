import json
import Section


class Visual:

    def __init__(self, parent: Section, visual_json: json):
        self.parent = parent
        self.visual_json = visual_json
        for key in ['config', 'filters', 'query', 'dataTransforms']:
            if key in self.visual_json.keys():
                self.visual_json[key] = json.loads(self.visual_json[key])

    def export_visual_json(self) -> json:
        return_json = self.visual_json
        for key in ['config', 'filters', 'query', 'dataTransforms']:
            if key in return_json.keys():
                return_json[key] = json.dumps(return_json[key])
        return return_json

    def get_visual_type(self):
        return self.visual_json['config']['singleVisual']['visualType']

    def set_slicer_value(self, value: str) -> None:
        if self.get_visual_type() != 'slicer':
            raise Exception('set_slicer_value only applicable to slicer visuals')

        value = "'{}'".format(value)
        self.visual_json['dataTransforms']['objects']['general'][0]['properties']['filter']['filter']['Where'][0][
            'Condition']['In']['Values'][0][0]['Literal']['Value'] = value
        self.visual_json['config']['singleVisual']['objects']['general'][0]['properties']['filter']['filter']['Where'][0][
            'Condition']['In']['Values'][0][0]['Literal']['Value'] = value
        print('done')
