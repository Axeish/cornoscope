import xml.etree.ElementTree as ET

def parse_xml_file(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    horoscope_data = []

    for sign in root.findall('sign'):
        data = {
            'sign': sign.find('name').text,
            'description': sign.find('description').text,
            'start_date': sign.find('start_date').text,
            'end_date': sign.find('end_date').text,
            'element': sign.find('element').text if sign.find('element') is not None else 'Unknown',
            'color': sign.find('color').text if sign.find('color') is not None else 'Unknown',

        }

        if None in data.values():
            raise ValueError("Missing required field in XML file.")

        horoscope_data.append(data)


    return horoscope_data
