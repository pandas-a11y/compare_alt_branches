import pytest
import requests
from compare_alt_branches import util

@pytest.mark.xfail(raises=requests.exceptions.HTTPError)
def test_get_branch_bin():
    assert type(util.get_branch_bin('p10')) == list
    assert len(util.get_branch_bin('p10')) > len([])
    with pytest.raises(SystemExit):
        util.get_branch_bin('')