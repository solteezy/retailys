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
    """Works with the filename 'export_full.xml'(which is the name of the exported zip). If a file with this name is present in the *extraction_path* directory,
    the filename is returned. Otherwise the zip is downloaded and extracted to *extraction_path*.

    Args:
        zip_url (str): URL to the zip that is to be processed.
        extraction_path (str, optional): Path where to extract the zip. Defaults to r"./".

    Raises:
        Exception: if the get request fails, the Exception is raised.

    Returns:
        str: Filename, "export_full.xml".
    """
    xml_name = "export_full.xml"

    if xml_name in os.listdir(extraction_path):
        return xml_name

    print("XML file unavailable. Downloading and extracting...")
    req = requests.get(zip_url)
    if not req.ok:
        raise Exception("Request failed.")
     
    with zipfile.ZipFile(io.BytesIO(req.content)) as my_zip:
        my_zip.extractall(extraction_path)

    return xml_name


def count_products(root: ET) -> int:
    """Using findall method and XPath, returns the number of items present in the XML tree.

    Args:
        root (ET): Root of the ElementTree that is to be searched for items.

    Returns:
        int: Number of items present in the ElementTree.
    """
    return len(root.findall(".items/item"))


def product_names(root: ET) -> List[str]:
    """Searches the ElementTree using findall and XPath to find names of the products.

    Args:
        root (ET): Root of the ElementTree.

    Returns:
        List[str]: Returns a list of the names of the items in the XML tree.
    """
    return [item.get("name") for item in root.findall(".items/item")]


def spare_parts(root: ET) -> List[str]:
    """Searches the ElementTree to find spare parts.

    Args:
        root (ET): Root of the ElementTree.

    Returns:
        List[str]: Returns a list of the names of the spare parts in the XML tree. 
    """
    return [item.get("name") for item in root.findall(".items/item/parts/part/item")]


def main():
    """Main function that is run when the script is, uses the *process_zip* to obtain the xml file, then the file is loaded using ElementTree.parse,
    functions are called to obtain the desired results. 
    """
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