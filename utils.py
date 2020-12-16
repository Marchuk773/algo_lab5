def read_from_file(filename: str) -> tuple[str, str]:
    with open(filename, 'r') as file:
        string, substring = tuple(map(str.strip, (file.readline(), file.readline())))
    return string, substring


def write_to_file(content: list[int]) -> None:
    with open('result.out', 'w') as file:
        file.write(str(content))
