"""
Retailys coding test 2023
Samuel Šoltés
27.7.2023  

https://www.astramodel.cz/b2b/export.pdf
"""

import requests, zipfile, io, os
from typing import List
from xml.etree import ElementTree as ET

def process_zip(zip_url : str, extraction_path : str = r"./") -> str:

    xml_name = "export_full.xml"

    if xml_name in os.listdir(os.getcwd()):
        return xml_name

    print("XML file unavailable. Downloading and extracting...")
    req = requests.get(zip_url)
    if not req.ok:
        raise Exception("Request failed.")
     
    with zipfile.ZipFile(io.BytesIO(req.content)) as my_zip:
        my_zip.extractall(extraction_path)
        # xml_name = my_zip.infolist()[0].filename

    return xml_name

def count_products(root: ET) -> int:
    return len(root.findall(".items/item"))


def product_names(root: ET) -> List[str]:
    return [item.get("name") for item in root.findall(".items/item")]


def spare_parts(root: ET):
    return [item.get("name") for item in root.findall(".items/item/parts/part/item")]


def main():
    
    zip_source = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"

    filename = process_zip(zip_source)

    xml_tree = ET.parse(filename)
    root = xml_tree.getroot()

    # 1) how many products there are    
    product_count = count_products(root)
    print(f"There is {product_count} products in the XML file.")
    
    # 2) print product names
    item_names = product_names(root)
    for name in item_names:
        print(name)
    
    # 3) print spare parts
    spares = spare_parts(root)
    for name in spares:
        print(name)


if __name__ == "__main__":
    main()