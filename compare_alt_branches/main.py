from compare_alt_branches import branches


def main():
    """
    Upon execution exports branch binaries, outputs their comparison results as a JSON object.
    :return: JSON object
    """
    binaries = branches.branch_request_bin()
    result_py = branches.branch_compare_full(binaries)
    result_json = branches.branch_compare_full_to_json(result_py)
    print(result_json)


if __name__ == "__main__":
    main()
