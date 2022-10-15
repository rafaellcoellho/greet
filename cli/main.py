import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(prog='hello')
    parser.add_argument('name')
    args = parser.parse_args(argv)

    print(f"hello {args.name}")

    return 0


if __name__ == '__main__':
    exit(main())
