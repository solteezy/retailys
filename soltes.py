"""
Retailys coding test 2023
Samuel Šoltés
27.7.2023  

"""

import requests, zipfile, io

def process_zip(zip_url : str, extraction_path : str = r"./") -> str:

    req = requests.get(zip_url)
    if not req.ok:
        raise Exception("Request failed.")
     
    with zipfile.ZipFile(io.BytesIO(req.content)) as my_zip:
        my_zip.extractall(extraction_path)
        xml_name = my_zip.infolist()[0].filename

    return xml_name

def count_products():
    pass


def product_names():
    pass


def spare_parts():
    pass


def main():
    # 1) how many products there are
    # 2) print product names
    # 3) print spare parts

    pass
    zip_source = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"

    process_zip(zip_source)


if __name__ == "__main__":
    main()