from working import convert

def test_convert():
    # Test valid inputs
    assert convert('3 AM to 1 PM') == '03:00 to 13:00'
    assert convert('7 AM to 4 PM') == '07:00 to 16:00'
    assert convert('9 AM to 11 PM') == '09:00 to 23:00'

    # Test invalid inputs that should raise ValueError
    invalid_inputs = ['4:0s AM to 5', 'Cat', '8:60 AM to 4:60 PM', '9AM to 5PM', '9 AM - 5 PM', '10:7 AM - 5:1 PM']
    for input_str in invalid_inputs:
        try:
            convert(input_str)
            # If no exception is raised, the test should fail
            assert False, f"Expected ValueError for input: {input_str}"
        except ValueError:
            pass  # Test passes if ValueError is raised
