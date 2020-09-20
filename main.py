from lib import *


def main():
    text = open('text.txt','r', encoding='utf8').read()
    distribution = get_dist(text)
    print(distribution.most_common())


if __name__ == '__main__':
    main()