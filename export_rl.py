import subprocess
import plistlib
from typing import List, Dict
import json
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class ReadingListItem:
    def __init__(self, item_dict: Dict):
        self.title = item_dict.get('URIDictionary', {}).get('title', 'No Title')
        self.url_string = item_dict.get('URLString', '')
        self.date_added = item_dict.get('DateAdded', datetime.now())

    def to_dict(self):
        return {
            "title": self.title,
            "URLString": self.url_string,
            "DateAdded": self.date_added.strftime("%Y-%m-%d %H:%M:%S")
        }

def export_reading_list(
    fname_bookmarks: str = "~/Library/Safari/Bookmarks.plist", 
    tmp_plist_fname: str = "tmp.plist"
    ) -> List[ReadingListItem]:

    try:
        command = f"cp {fname_bookmarks} {tmp_plist_fname}"
        logger.debug(f"Making temporary copy of reading list: {command}")
        run_command(command)

        with open(tmp_plist_fname, 'rb') as f:
            res = plistlib.load(f)
        
        rlist = find_dicts_with_rlist_keys_in_dict(res)
        logger.debug(f"You have: {len(rlist)} items in your reading list")

        ritems = [ReadingListItem(r) for r in rlist]
        
    finally:
        command = f"rm -f {tmp_plist_fname}"
        logger.debug(f"Removing tmp file: {command}")
        run_command(command)

    logger.debug("Done.")
    return ritems

def write_reading_list_to_json(ritems: List[ReadingListItem], fname_out: str):
    with open(fname_out, 'w') as f:
        rjson = [item.to_dict() for item in ritems]
        json.dump(rjson, f, indent=3)
    logger.info(f"Wrote reading list to JSON file: {fname_out}")

def run_command(command: str) -> str:
    output = subprocess.check_output(command, shell=True, text=True)
    return output

def find_dicts_with_rlist_keys_in_dict(base_dict: Dict) -> List:
    ret = []

    for key, val in base_dict.items():
        if key == "Children":
            for child_dict in val:
                ret += find_dicts_with_rlist_keys_in_dict(child_dict)
        elif key == "ReadingList":
            ret.append(base_dict)
            break
        
    return ret

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    reading_items = export_reading_list()
    write_reading_list_to_json(reading_items, 'safari_reading_list.json')

