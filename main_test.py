from tqdm import tqdm
import pytest
import sys
import pprint
from utils import get_input, TEST_INPUTS


class TestInputParser(object):
    def test_read_file(self):
        get_input(TEST_INPUTS[0])

    def test_output_data_structure(self):
        for file_path in tqdm(TEST_INPUTS):
            output = get_input(file_path)
            # pprint.pprint(output)
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
            assert len(output["libraries"]) == output["total_libraries"]
            assert len(output["books"]) == output["total_books"]
            for library in output["libraries"]:
                assert len(library["books"]) == library["total_books"]
                assert isinstance(library["books"][0], int)


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
