# PoE-Lab Compass Fetcher
A simple script to fetch lab compass files from <https://poelab.com> easily.

## Usage:

Open up the command line in the folder with the .exe file by click the path line and typing "cmd", then pressing Enter [example](https://prnt.sc/lp6kks)

Then simply type the name of the file and hit enter to download today's lab file, or add arguments like shown below for more options.

```text
fetch-map.exe [-h] [-date DATE] [-lab LAB] [-format FORMAT] [-dir DIR]
OR
python fetch-map.py [-h] [-date DATE] [-lab LAB] [-format FORMAT] [-dir DIR]

optional arguments:
  -h, --help      show this help message and exit
  -date DATE      the date of the lab to fetch a compass file for (format:
                  yyyy-mm-dd, default: today's date)
  -lab LAB        the lab tier (default: uber)
  -format FORMAT  python string format for the file's name (default:
                  {:s}-{:s}-{:s}-{:s}.json)
  -dir DIR        the directory in which the lab file would be saved in
                  (default: current working directory)

```
