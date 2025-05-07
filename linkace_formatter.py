#! /usr/bin/env python

import argparse
import csv
from pathlib import Path

bookmarks = {"Other Bookmarks": []}
bookmarks_file = Path("LinkAce_formatted.html")


def add_bookmark(folder, url, title):
    """Add the entry into the appropriate bookmark folder"""
    # If not in a list, use the default Chrome folder
    if not folder:
        folder = "Other Bookmarks"
    if folder not in bookmarks:
        bookmarks[folder] = [(url, title)]
    else:
        bookmarks[folder].append((url, title))


def organize_list_to_folder(linkacecsv):
    """Read the CSV export from LinkAce and categorize by list.
    Lists in LinkAce are folders in Chrome.
    """
    with Path(linkacecsv).open("r") as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip the header in the CSV file
        next(csvreader)
        for entry in csvreader:
            url = entry[2]
            title = entry[3]
            folder = entry[15]

            # Check if link has multiple lists
            if "," in folder:
                folders = folder.split(",")
                for folder in folders:
                    add_bookmark(folder, url, title)
            else:
                add_bookmark(folder, url, title)


def output_bookmarks():
    """Output the organized bookmarks to a file.
    Recreating the file as Chrome's own export file.
    """
    output_header = ("<!DOCTYPE NETSCAPE-Bookmark-file-1>\n"
                     '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n'
                     "<TITLE>Bookmarks</TITLE>\n"
                     "<H1>Bookmarks</H1>\n"
                     "<DL><p>\n")
    with bookmarks_file.open("a") as output_file:
        output_file.write(output_header)
        for folder in bookmarks:
            folder_header = f"<DT><H3>{folder}</H3>\n<DL><p>\n"
            output_file.write(folder_header)
            for entry in bookmarks[folder]:
                url = entry[0]
                title = entry[1]
                entry_link = f'<DT><A HREF="{url}">{title}</A>\n'
                output_file.write(entry_link)
            output_file.write("</DL><p>\n")
        output_file.write("</DL><p>")


if __name__ == "__main__":
    csv_parser = argparse.ArgumentParser(usage="%(prog)s [filename]")
    csv_parser.add_argument("input_file",
                            default="LinkAce_export.csv",
                            help=argparse.SUPPRESS,
                            nargs="?")
    csv_arg = csv_parser.parse_args()
    input_file = Path(csv_arg.input_file)
    if not Path(input_file).exists():
        csv_parser.print_help()
    else:
        organize_list_to_folder(input_file)
    output_bookmarks()
