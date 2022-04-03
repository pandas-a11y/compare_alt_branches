def pkg_compare_diff(dict_has_pkg, dict_lacks_pkg):
    """
    Outputs unmatched packages that are present in the 1st package dictionary,
    but not present in the 2nd package dictionary

    :param dict_has_pkg: Point of comparison package dictionary
    :type dict_has_pkg: dict
    :param dict_lacks_pkg: Compared package dictionary
    :type dict_lacks_pkg: dict
    :return: Dictionary containing packages present only in the 1st argument
    :rtype: dict
    """
    set_has_pkg = {*dict_has_pkg.keys()}
    set_lacks_pkg = {*dict_lacks_pkg.keys()}
    unmatched_pkg = frozenset(set_has_pkg - set_lacks_pkg)
    pkg_difference = {k: dict_has_pkg[k] for k in unmatched_pkg}
    return pkg_difference
