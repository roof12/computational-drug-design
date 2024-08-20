#!/usr/bin/env python3

# Extract mol files from an Mcule SDF, naming the files with the Mcule ID

from openbabel import pybel

def extract_sdf_files(sdf_file, comment_field, default_prefix, output_dir):
    """
    Extracts molecules from an SDF file and saves each as a MOL file. Filenames are prefixed with the value of the comment field.

    Parameters:
    - sdf_file (str): Path to the input SDF file.
    - comment_field (str): Field to use for filename. If missing, use default_prefix.
    - default_prefix (str): Prefix for filenames if comment_field is not present.
    - output_dir (str): Directory to save the MOL files. Created if it doesn't exist.
    """

    # Ensure the output directory exists
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the SDF file
    mols = pybel.readfile('sdf', sdf_file)

    for i, mol in enumerate(mols):
        # Extract comment as filename
        comment = mol.data[comment_field] if comment_field in mol.data else f'{default_prefix}-{i+1}'
        comment = comment.replace(' ', '_').replace('/', '_')  # Clean up the filename
        filename = f'{output_dir}/{comment}.mol'
        
        # Write the molecule to a MOL file
        mol.write('mol', filename)

        print(f'Saved {filename}')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract mol files from an SDF.")
    parser.add_argument('-o', '--output-dir', default='sdf_files', help='output directory')
    parser.add_argument('-d', '--default-prefix', default='compound', help='prefix used when the comment is not found')
    parser.add_argument("sdf_file", help="path to the SDF file")
    parser.add_argument("comment_field", help="comment field")
    args = parser.parse_args()

    extract_sdf_files(args.sdf_file, args.comment_field, args.default_prefix, args.output_dir)

