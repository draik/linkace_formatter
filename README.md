# LinkAce Formatter

### Description
[LinkAce](https://www.linkace.org/) is a bookmark manager, allowing for one link to be on multiple lists (folders) 
and tags. When exporting the bookmarks, all of the links are in the same folder; 
no organization maintained when importing the bookmarks. This script will get 
the bookmarks and place them in a formatted entry for Chrome to keep organized.


### Usage
The stand-alone script can be invoked from anywhere, and the optional argument 
is the location of the "LinkAce_export.csv" file. If not specified, it is assumed 
to be in the same directory from which it is ran. The output HTML file will be 
placed in the executed directory as "LinkAce_formatted.html" which can be imported 
directly into Chrome.

```bash
$ ./linkace_formatter.py -h
usage: linkace_formatter.py [filename]

options:
  -h, --help  show this help message and exit
```

