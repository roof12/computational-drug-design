#!/usr/bin/env python3
import argparse

from cctdi import filenames_from_file, random_sample

def main(filename, count):
    ligands = random_sample(
        filenames_from_file(filename),
        count)

    for ligand in ligands:
        print(ligand)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sample lines from an input file")
    parser.add_argument("ligands_file", help="file containing the filenames of input molecules")
    parser.add_argument("count", type=int, help="number of lines to sample")
    args = parser.parse_args()

    main(args.ligands_file, args.count)

