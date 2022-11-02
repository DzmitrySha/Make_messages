# Make messages

Make messages from special .xlsx file with table of last names, parent names, child names and template message. Returns a list of unique messages with every pair of parent and child names inside.


## Instructions

**Install/uninstall package:**

`make package-install`
`make package-uninstall`

**Run help:**

`make-messages -h`

**Run script with default settings (save in current folder):** 

`make-messages <xlsx_filepath>`

**Run script with user settings (save in exists output specified folder):** 

`make-messages --output <exist_folder_path> <xlsx_filepath>`

or

`make-messages -o <exist_folder_path> <xlsx_filepath>`

