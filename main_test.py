import pytest
import sys
from main import get_input, TEST_INPUTS


class TestInputParser(object):
    def test_read_file(self):
        get_input(TEST_INPUTS[0])

    def test_output_data_structure(self):
        output = get_input(TEST_INPUTS[0])
        assert output["total_books"] is not None
        assert output["total_libraries"] is not None
        assert output["total_days"] is not None
        assert output["books"] is not None
        assert output["libraries"] is not None

        assert isinstance(output["total_books"], int)
        assert isinstance(output["total_libraries"], int)
        assert isinstance(output["total_days"], int)
        assert isinstance(output["total_libraries"], int)
        assert isinstance(output["books"], list)
        assert isinstance(output["books"][0], int)

        assert isinstance(output["libraries"], list)
        assert isinstance(output["libraries"][0], dict)


class TestAndScoreAlgorithms(object):
    def setup_class(self):

        # {function: Function,  score: Number, output: return from Function}
        self.algorithms = []
        self.file_path = TEST_INPUTS[0]
        self.input = get_input(self.file_path)
        print("Algorithm\tScore")
        for algorithm in self.algorithms:
            algorithm["output"] = algorithm["function"](self.input)
            algorithm["score"] = get_score(algorithm["output"])
            print("{}\t{}".format(algorithm["function"].__name__, algorithm["score"]))

    def test_valid_output(self):
        for algorithm in self.algorithms:
            output = algorithm["output"]
            assert output.length % 2 != 0

    def test_score_(self):
        pass


def get_score(output):
    return -1


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "--color=yes", "--verbose", "-s"]))
