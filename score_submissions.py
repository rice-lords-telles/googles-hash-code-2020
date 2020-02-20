import pytest
import sys
from main import get_input


class TestAndScoreAlgorithms(object):
    def setup_class(self):

        # {function: Function,  score: Number, output: return from Function}
        self.algorithms = []
        self.file_path = ""
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
