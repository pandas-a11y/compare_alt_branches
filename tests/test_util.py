from compare_alt_branches import util
import pytest
import requests

@pytest.mark.xfail(raises=requests.exceptions.HTTPError)
def test_get_branch_bin():
    with pytest.raises(SystemExit):
        util.get_branch_bin('')
    assert type(util.get_branch_bin('p10')) == list
    assert len(util.get_branch_bin('p10')) > len([])
    assert sorted(util.get_branch_bin('sisyphus')[0].keys()) == [
        "arch",
        "buildtime",
        "disttag",
        "epoch",
        "name",
        "release",
        "source",
        "version"
    ]
    assert util.get_branch_bin('sisyphus')[0]['arch'] != util.get_branch_bin('sisyphus')[-1]['arch']


def test_pkg_to_dict():
    test_data = [{
            "arch": "aarch64",
            "buildtime": 1640428491,
            "disttag": "p10+291491.1000.21.1",
            "epoch": 0,
            "name": "ruby-mspec",
            "release": "alt2.2.1",
            "source": "ruby",
            "version": "2.7.4"
        },
        {
            "arch": "aarch64",
            "buildtime": 1645710288,
            "disttag": "p10+295902.100.1.1",
            "epoch": 0,
            "name": "qemu-user-static-aarch64",
            "release": "alt1",
            "source": "qemu",
            "version": "6.1.1"
        },
        {
            "arch": "i586",
            "buildtime": 1640428340,
            "disttag": "p10+291491.1000.21.1",
            "epoch": 0,
            "name": "libruby-debuginfo",
            "release": "alt2.2.1",
            "source": "ruby",
            "version": "2.7.4"
        }
    ]

    assert len(util.pkg_to_dict(test_data).items()) == 3
    assert util.pkg_to_dict(test_data)[('i586', 'libruby-debuginfo')] == "2.7.4"
    assert util.pkg_to_dict(test_data)[('aarch64', 'qemu-user-static-aarch64')] != "2.7.4"