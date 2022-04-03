import pkg_resources as p_res


def pkg_compare_diff(dict_has_pkg, dict_lacks_pkg):
    """
    Outputs unmatched packages that are present in the 1st package dictionary,
    but not present in the 2nd package dictionary.

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


def pkg_compare_ver(pkg_dict_sis, pkg_dict_p10):
    """
    Outputs a dictionary of packages for which versions are higher in the 'sisyphus' branch.

    :param pkg_dict_sis: Sisyphus package dictionary
    :type pkg_dict_sis: dict
    :param pkg_dict_p10: Compared package dictionary (p10 by default)
    :type pkg_dict_p10: dict
    :return: Dictionary of packages with higher version in 'sisyphus'
    :rtype: dict
    """
    set_sis = {*pkg_dict_sis.keys()}
    set_p10 = {*pkg_dict_p10.keys()}
    pkg_in_both = frozenset(set_sis & set_p10)
    higher_v_sis = dict()
    for p in pkg_in_both:
        if p_res.parse_version(pkg_dict_sis[p]) > p_res.parse_version(pkg_dict_p10[p]):
            higher_v_sis[p] = pkg_dict_sis[p]
    return higher_v_sis
