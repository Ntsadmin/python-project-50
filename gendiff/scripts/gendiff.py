import argparse


def main() -> None:
    """
    function to get input args to start the game
    """
    parser = argparse.ArgumentParser(description='Compares two configuration '
                                                 'files and shows a'
                                                 ' difference')
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
            '-f',
            '--format',
            help='set format of output')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
