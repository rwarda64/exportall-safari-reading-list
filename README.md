# exportall-safari-reading-list

This Python script exports items from your Safari Reading List into a simplified JSON format. Each exported item includes the title, URL, and the date it was added to the Reading List. This tool is especially useful for backing up your reading list or for processing the list with other tools or scripts.

## Features
* Extracts reading list items directly from Safari's Bookmarks.plist.
* Outputs a clean JSON file containing the title, URL, and addition date of each item.
* Simple and easy to use, with minimal dependencies.

## Requirements
* Python 3.x
* Access to the ~/Library/Safari/Bookmarks.plist file (typically requires a macOS environment with Safari installed).

## Dependencies
Before running the script, ensure you have Python installed on your system. The script uses standard libraries available in Python 3, so no additional installations are required.

## Usage
1. Clone this repository or download the script to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
`python safari_reading_list_exporter.py`
By default, the script will read the Bookmarks.plist from the standard location `(~/Library/Safari/Bookmarks.plist)` and output the *safari_reading_list.json* in the current directory.

## Custom Usage
The script can be modified to specify a different input file or output destination by changing the following parameters in the export_reading_list and write_reading_list_to_json function calls within the if __name__ == "__main__": block at the bottom of the script:

* **`fname_bookmarks`**: Path to your Bookmarks.plist file.
* **`fname_out`**: Desired path and name for the output JSON file.

## Contributing
Contributions to enhance this script, fix bugs, or improve documentation are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is open-source and available under the MIT License.
