from compare_alt_branches import branches
import json

test_data = [{('a1', 'b1'): '0.1.0',
              ('a1', 'b2'): '2.0.3'},

             {('a2', 'b2'): '0.4'},

             {('b1', 'a1'): '1.0'}]


def test_branch_compare_full_to_json():
    assert branches.branch_compare_full_to_json([dict(), dict(), dict()]) == json.dumps([{"type": "only_in_p10",
                                                                                          "packages": []},
                                                                                         {"type": "only_in_sisyphus",
                                                                                          "packages": []},
                                                                                         {"type": "version_higher_in_sisyphus",
                                                                                          "packages": []}
                                                                                         ])
    assert branches.branch_compare_full_to_json(test_data) == json.dumps([{'type': 'only_in_p10',
                                                                           'packages': [{'arch': 'a1',
                                                                                         'name': 'b1',
                                                                                         'version': '0.1.0'},
                                                                                        {'arch': 'a1',
                                                                                         'name': 'b2',
                                                                                         'version': '2.0.3'}
                                                                                        ]},
                                                                          {'type': 'only_in_sisyphus',
                                                                           'packages': [{'arch': 'a2',
                                                                                         'name': 'b2',
                                                                                         'version': '0.4'}
                                                                                        ]},
                                                                          {'type': 'version_higher_in_sisyphus',
                                                                           'packages': [{'arch': 'b1',
                                                                                         'name': 'a1',
                                                                                         'version': '1.0'}
                                                                                        ]}
                                                                          ])
