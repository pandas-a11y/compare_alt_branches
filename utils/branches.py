from utils import util
from utils import comparators
import json


def branch_compare_full_to_json(pkg_comp_full, branches_list):
    """
    Outputs results of branch comparisons to JSON format.

    :param pkg_comp_full: A tuple of dictionaries with comparison results
    :type pkg_comp_full: list
    :param branches_list: A list of branches being compared
    :type branches_list: list
    :return: Comparison results as a JSON object
    :rtype: `JSON` object
    """

    comp_out = ["only_in_" + branches_list[1],
                "only_in_" + branches_list[0],
                "version_higher_in_" + branches_list[0]
                ]

    data_array = []
    for i in range(len(comp_out)):
        package_list = dict()
        data_list = [{'arch': k[0], 'name': k[1], 'version': v} for (k, v) in pkg_comp_full[i].items()]
        package_list['type'] = comp_out[i]
        package_list['packages'] = data_list
        data_array.append(package_list)

    json_obj = json.dumps(data_array)
    return json_obj


def branch_request_bin(branches_list):
    """
    Retrieves package binaries for two ALTRepo branches. Outputs a list with binaries.

    :param branches_list: A list with branch names
    :type branches_list: list
    :return: A list with branch binaries
    :rtype: list
    """
    branch_1, branch_2 = branches_list[0], branches_list[1]

    branch_pkg_list_first = util.get_branch_bin(branch_1)
    branch_pkg_list_second = util.get_branch_bin(branch_2)
    return [branch_pkg_list_first, branch_pkg_list_second]


def branch_compare_full(pkg_bin_list):
    """
    Compares packages in two ALTRepo branches. Outputs a list of dictionaries containing comparison results.

    :param pkg_bin_list: A list with branch binaries to compare
    :type pkg_bin_list: list
    :return: A list of dictionaries of comparison results
    :rtype: list
    """
    branch_pkg_list_first, branch_pkg_list_second = pkg_bin_list[0], pkg_bin_list[1]
    dict_first = util.pkg_to_dict(branch_pkg_list_first)
    dict_second = util.pkg_to_dict(branch_pkg_list_second)

    only_in_second = comparators.pkg_compare_diff(dict_second, dict_first)
    only_in_first = comparators.pkg_compare_diff(dict_first, dict_second)
    version_diff = comparators.pkg_compare_ver(dict_first, dict_second)

    return [only_in_second, only_in_first, version_diff]
