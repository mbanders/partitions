#!/usr/bin/env python3
import argparse

from partitions.partitions import pretty_partitions

def main():
    parser = argparse.ArgumentParser(description='Print all partitions of a number n.')
    parser.add_argument('n', type=int, help='Positive integer n.')
    args = parser.parse_args()
    pretty_partitions(args.n)

if __name__ == '__main__':
    main()
