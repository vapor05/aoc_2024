import pathlib

input_dir = pathlib.Path(__file__).parent.joinpath("problem_data")


def _problem_data_file(fn: str) -> pathlib.Path:
    return input_dir.joinpath(fn)
