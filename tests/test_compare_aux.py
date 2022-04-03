from compare_alt_branches import compare_aux

test_data_1 = {
    ('a1', 'b1'): '0.1.0',
    ('a1', 'b2'): '2.0.3',
    ('a2', 'b2'): '0.4',
    ('f5', 'f5'): '5.04',
    ('b1', 'a1'): '1.0',
    ('a7', 'a7'): '9.5'
}

test_data_2 = {
    ('a1', 'b1'): '0.1',
    ('a1', 'b3'): '2.14.158',
    ('c2', 'b2'): '22.22',
    ('f5', 'f5'): '5.40'
}

test_data_3 = {('a7', 'a7'): '10.0'}

def test_pkg_compare_diff():
    assert compare_aux.pkg_compare_diff(test_data_1, test_data_1) == {}
    assert compare_aux.pkg_compare_diff(test_data_1, test_data_2) == {('a1', 'b2'): '2.0.3',
                                                                      ('a2', 'b2'): '0.4',
                                                                      ('b1', 'a1'): '1.0',
                                                                      ('a7', 'a7'): '9.5'}
    assert compare_aux.pkg_compare_diff(test_data_2, test_data_1) == {('a1', 'b3'): '2.14.158',
                                                                      ('c2', 'b2'): '22.22'}

def test_pkg_compare_ver():
    assert compare_aux.pkg_compare_ver(test_data_1, test_data_1) == {}
    assert compare_aux.pkg_compare_ver(test_data_1, test_data_3) == {}
    assert compare_aux.pkg_compare_ver(test_data_3, test_data_1) == test_data_3
    assert compare_aux.pkg_compare_ver(test_data_1, test_data_2) == {}
    assert compare_aux.pkg_compare_ver(test_data_2, test_data_1) == {('f5', 'f5'): '5.40'}
