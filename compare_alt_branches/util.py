import requests

SERVER_ADRESS = "https://rdb.altlinux.org/api"


def get_branch_bin(branch):
    """
    Sends a GET request, returns branch package data as a list.

    :param branch: ALT branch to request binaries of
    :type branch: str
    :return: List of packages in the branch
    :rtype: list
    """
    try:
        response = requests.get(SERVER_ADRESS + "/export/branch_binary_packages/{}".format(branch))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    branch_bin = response.json()
    branch_pkg_list = branch_bin['packages']
    return branch_pkg_list


def pkg_to_dict(branch_pkg_list):
    """
    Utility function for the 'compare_aux' module, takes a list of
    packages of one branch, converts it into a dictionary such that:

    key: tuple('architecture', 'package-name'),

    val: 'package version'.

    :param branch_pkg_list: List of packages in the branch
    :type branch_pkg_list: list
    :return: Dictionary of packages in the branch
    :rtype: dict
    """
    branch_pkg_dict = dict()
    for p in branch_pkg_list:
        branch_pkg_dict[(p['arch'], p['name'])] = p['version']
    return branch_pkg_dict
