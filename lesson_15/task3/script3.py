import xml.etree.ElementTree as ET
import logging

# Налаштування логера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_incoming_by_number(xml_path, target_number):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            timing = group.find('timingExbytes')
            incoming = timing.find('incoming') if timing is not None else None

            if number is not None and number.text == str(target_number):
                result = incoming.text if incoming is not None else "No <incoming> value found"
                logging.info(f"group/number = {target_number} → timingExbytes/incoming = {result}")
                return result

        logging.info(f"group/number = {target_number} not found in XML.")
        return None

    except Exception as e:
        logging.error(f"Error while parsing XML: {e}")

# 🔍 Виклик функції
find_incoming_by_number("groups.xml", 2)