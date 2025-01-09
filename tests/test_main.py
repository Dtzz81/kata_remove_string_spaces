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
    original = "awe some"
    expected_output = "awesome"
    result = no_space(original)
    assert expected_output == result

def test_space_in_string_and_on_sides():
    original = "aqua 12 Yes "
    expected_output = "aqua12Yes"
    result = no_space(original)
    assert expected_output == result


def test_from_codewars():
    original = "8 j 8   mBliB8g  imjB8B8  jl  B"
    expected_output = "8j8mBliB8gimjB8B8jlB"
    result = no_space(original)
    assert expected_output == result
