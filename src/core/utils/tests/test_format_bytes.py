import pytest

from core.utils.format_bytes import format_bytes


class TestFormatBytes:
    @pytest.mark.parametrize(
        "test_input, expected_output",
        [
            (1023, {"value": 1023, "suffix": "b"}),
            (2048, {"value": 2.0, "suffix": "kb"}),
            (5242880, {"value": 5.0, "suffix": "mb"}),
            (10737418240, {"value": 10.0, "suffix": "gb"}),
            (5497558138880, {"value": 5.0, "suffix": "tb"}),
        ],
    )
    def test_format_bytes(self, test_input, expected_output):
        assert format_bytes(test_input) == expected_output
