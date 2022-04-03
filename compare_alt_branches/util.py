import requests


def get_branch_bin(branch):
    """
    Sends a GET request, returns package data as a list

    :param branch: ALT branch to request binaries of
    :type branch: str
    :return: List of packages in the branch
    :rtype: list
    """
    try:
        response = requests.get("https://rdb.altlinux.org/api/export/branch_binary_packages/{}".format(branch))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    branch_bin = response.json()
    branch_pkg_list = branch_bin['packages']
    return branch_pkg_list