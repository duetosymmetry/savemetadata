from pathlib import Path
import logging
import re

def png_metadata():
    """Document me"""

    try:
        import __main__
        return {"Description": stringify_metadata(__main__.__file__)}
    except:
        logging.warning("Could not read __main__.__file__, perhaps you are running interactively?")
        return {}

def stringify_metadata(path):
    """Document me"""

    path = Path(path)

    magic = "META01;"

    escaped_name = path.name.replace('"', '\\"')
    namestr = f'name="{escaped_name}";'

    with open(path, 'rt') as script_file:
        datastr = script_file.read()

    return magic+namestr+datastr

def extract_metadata_png(path):
    """Document me"""

    try:
        from PIL import Image
    except Exception as e:
        logging.warning("Couldn't import PIL, you need Pillow to extract from PNGs")
        raise e

    im = Image.open(path)

    try:
        desc = im.info['Description']
    except Exception as e:
        raise KeyError("No description set in PNG info")

    meta = extract_metadata_string(desc)

    if meta is None:
        raise ValueError("PNG description field is not formatted as our metadata")

    return meta

def extract_metadata_string(str):
    """Extract the metadata contents from a string"""

    meta_pat_01 = '^META01;name="(.*?)(?<!\\\\)";(.*)$'
    extractor = re.compile(meta_pat_01, flags=re.DOTALL)

    res = extractor.match(str)
    if res is None:
        return None

    filename = res.group(1).replace('\\"','"')
    contents = res.group(2)

    return {"name": filename, "contents": contents}
