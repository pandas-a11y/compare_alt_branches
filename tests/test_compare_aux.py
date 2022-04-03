from compare_alt_branches import compare_aux

def test_pkg_compare_diff():
    test_data_1 = {
        ('a1', 'b1'): '1',
        ('a1', 'b2'): '2',
        ('a2', 'b2'): '2',
        ('f5', 'f5'): '5',
        ('b1', 'a1'): '1'
    }

    test_data_2 = {
        ('a1', 'b1'): '1',
        ('a1', 'b3'): '2',
        ('c2', 'b2'): '2',
        ('f5', 'f5'): '5'
    }

    assert compare_aux.pkg_compare_diff(test_data_1, test_data_1) == {}
    assert compare_aux.pkg_compare_diff(test_data_1, test_data_2) == {('a1', 'b2'): '2',
                                                                      ('a2', 'b2'): '2',
                                                                      ('b1', 'a1'): '1'}
    assert compare_aux.pkg_compare_diff(test_data_2, test_data_1) == {('a1', 'b3'): '2',
                                                                      ('c2', 'b2'): '2'}