from source.main import no_space

def test_no_space_in_output():
    #act
    original = "awesome"
    #arrange
    expected_output = "awesome"
    result = no_space(original)
    #assert
    assert expected_output == result

def test_space_in_string():
    #act
    original = "awe some"
    #arrange
    expected_output = "awesome"
    result = no_space(original)
    #assert
    assert expected_output == result

def test_space_in_string_and_on_sides():
    #act
    original = "aqua 12 Yes "
    #arrange
    expected_output = "aqua12Yes"
    result = no_space(original)
    #assert
    assert expected_output == result
