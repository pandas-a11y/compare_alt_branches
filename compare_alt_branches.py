#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from utils import branches

BRANCHES_DEFAULT = ['sisyphus', 'p10']

parser = argparse.ArgumentParser(description='Compare two ALT branches')

parser.version = '0.2.0'
parser.add_argument('-b',
                    '--branch',
                    action='store',
                    type=str,
                    help='set branches to compare, expects 2 branch names in a comma-separated string; '
                         'example: "sisyphus,p10"; '
                         'default branches: sisyphus, p10')

args = parser.parse_args()

br = args.branch
if br != None:
    br = [b.strip() for b in br.split(',')]
    if len(br) != 2:
        raise SystemExit("Error: 2 branch names expected")
    else:
        branch_arg = br
else:
    branch_arg = BRANCHES_DEFAULT

def main():
    """
    Upon execution exports branch binaries, outputs their comparison results as a JSON object.
    :return: JSON object
    """
    binaries = branches.branch_request_bin(branch_arg)
    result_py = branches.branch_compare_full(binaries)
    result_json = branches.branch_compare_full_to_json(result_py, branch_arg)
    print(result_json)


if __name__ == "__main__":
    main()
