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
        }
        horoscope_data.append(data)

    return horoscope_data
