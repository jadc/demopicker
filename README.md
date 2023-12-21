# Demo Picker
A python script that randomly selects students, prioritizing students who have been selected the least.

Given a submissions zip, it will create a demo list (txt file) in the demos directory (default './demos'). With this demo list, you can copy and paste it into a spreadsheet to be able to mark students who have performed their demo. 

When it is time to create a demo list for the next lab, simply run the script again (on a different submission zip) and it will create a new demo list (in the same directory) that prioritizes students who have performed the least number of demos before. 

In order for this to work, you must keep the previous demo list text files in the demos directory.

## Usage
```
usage: demopicker.py [-h] [-p PROPORTION] [-d DIR] zip

positional arguments:
  zip                   submissions zip (from 'Download All Submissions' in eClass)

options:
  -h, --help            show this help message and exit
  -p PROPORTION, --proportion PROPORTION
                        proportion of students that should demo (default 1/3)
  -d DIR, --dir DIR     directory to store demo lists (default './demos')
```