from incolumepy.incolume_cli import release, system, version
from incolumepy.incolume_cli.click import hello


if __name__ == '__main__':
    print(system(), version(), release())
    hello()