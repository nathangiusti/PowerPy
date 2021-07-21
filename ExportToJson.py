import json
import sys
import zipfile

# Usage
# python ExportToJson.py [pbix file location] [output file location]
# Ex: python ExportToJson.py Folder/MyPbixFile.pbix MyReportJson.json


def main():

    file_location = sys.argv[1]
    output_path = sys.argv[2]

    zf = zipfile.ZipFile(file_location)
    data = json.loads(zf.read('Report/Layout').decode('utf-16-le'))
    data['config'] = json.loads(data['config'])
    for section in data['sections']:
        for visual_container in section['visualContainers']:
            for key in ['config', 'filters', 'query', 'dataTransforms']:
                if key in visual_container.keys():
                    visual_container[key] = json.loads(visual_container[key])
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
