from source.main import no_space

def test_no_space_in_output():
    #act
    original = "awesome"
    #arrange
    expected_output = "awesome"
    result = no_space()
    #assert
    assert expected_output == result
