#!/usr/bin/env python3
import shutil
from pathlib import Path
import logging
import argparse

'''
    New.py creates new files for Advent of Code for each run.
    Define a template in the User Configuration, using 00 for day numbers.
'''

# START User configuration
DEFAULT_PY_TEMPLATE = 'day00.py'
DEFAULT_TXT_TEMPLATE = 'day00-input.txt'
DEBUG = False
# END User configuration

def setup_logging(debug):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')

def make_new_day(py_template, txt_template):
    py_template_path = Path(py_template)
    txt_template_path = Path(txt_template)

    if not py_template_path.exists():
        logging.error(f'Cannot find {py_template}. Exiting')
        return

    if not txt_template_path.exists():
        logging.error(f'Cannot find {txt_template}. Exiting')
        return

    logging.debug('Found template files')

    for day in range(1, 26):
        day_str = f"{day:02}"
        day_py_file = py_template_path.name.replace('00', day_str)
        day_txt_file = txt_template_path.name.replace('00', day_str)
        day_py_path = py_template_path.parent / day_py_file
        day_txt_path = txt_template_path.parent / day_txt_file

        logging.debug(f'Looking for {day_py_file}')

        if not day_py_path.exists():
            logging.info(f'Creating {day_py_file}')
            shutil.copyfile(py_template_path, day_py_path)
            logging.debug(f'Looking for {day_txt_file}')

            if not day_txt_path.exists():
                logging.info(f'Creating {day_txt_file}')
                shutil.copyfile(txt_template_path, day_txt_path)
            else:
                logging.info(f'Skipping {day_txt_file}.')
            break
        else:
            logging.debug('Found. Continuing')

def main():
    parser = argparse.ArgumentParser(description='Generate new Advent of Code files.')
    parser.add_argument('--py-template', default=DEFAULT_PY_TEMPLATE, help='Python template filename')
    parser.add_argument('--txt-template', default=DEFAULT_TXT_TEMPLATE, help='Text template filename')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()

    setup_logging(args.debug)
    make_new_day(args.py_template, args.txt_template)

if __name__ == "__main__":
    main()