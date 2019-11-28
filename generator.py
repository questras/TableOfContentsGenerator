"""
Script to generate table of contents based on
headers in markdown languages.
Created for use with readme on github.
For now it handles '#' and '##' headers.

Created by Michał Wiśniewski on 27.11.2019

toc - table of contents

Last edit: 28.11.2019
"""

import re
import argparse


def generate_head1(head1, index, link_index):
    """Generate 'h1' item in toc"""
    if head1[0] == '#':
        head1 = head1[1:]

    return '{}. [{}](#p{})'.format(index, head1, link_index)

def generate_head2(head2, index, link_index):
    """Generate 'h2' item in toc"""
    if head2[:2] == '##':
        head2 = head2[2:]
    
    return '    {}. [{}](#p{})'.format(index, head2, link_index)

def generate_alink(index):
    """Create 'a' link for header item in toc"""
    return '<a name="p{}"></a>'.format(index)


def generate_toc_in_file(input_file_path, output_file_path):
    """
    Modify given file: add table of contents
    and links to headers.
    Assuming that input_file does not contain any toc, 
    it might cause problems otherwise.
    """
    output = ''
    toc = '\n# Table of contents'

    input_file = open(input_file_path, 'r')

    main_index = 0   # index for main headers in toc
    sub_index = 1   # index for sub headers in toc
    link_index = 0  # index for links in toc

    for line in input_file:
        if line[0] == '#':  
            line = line.replace('\n', '')

            # generate link and header
            alink = generate_alink(link_index)
            
            if line[1] == '#':
                header = generate_head2(line, sub_index, link_index)
                sub_index += 1
            else:
                header = generate_head1(line, main_index, link_index)
                main_index += 1
                sub_index = 1
            
            link_index += 1
            # append to toc and output text
            toc = '{}\n{}'.format(toc, header)
            output = '{}{} {}\n'.format(output, line, alink)
            
        else:
            output = '{}{}'.format(output, line)
    
    output = '{}\n\n{}'.format(toc, output)
    
    input_file.close()

    output_file = open(output_file_path, 'w')
    output_file.write(output)
    output_file.close()
    
def delete_toc_in_file(input_file_path, output_file_path):
    """Delete toc and all links connected to it in file"""
    input_file = open(input_file_path, 'r')
    output = input_file.read()
    input_file.close()

    output = re.sub(r'# Table of contents\n', '', output)
    output = re.sub(r'\(#p\d+\)', '', output)
    output = re.sub(r' <a name=".+"></a>', '', output)
    output = re.sub(r'\d+\. \[.+\]\n', '', output)

    # delete blank spaces at the top and bottom of file
    output = output.strip()

    output_file = open(output_file_path, 'w')
    output_file.write(output)
    output_file.close()


def generate_toc(input_file_path, output_file_path=None):
    """Delete existing toc and generate new one"""

    # check if output file specified
    if output_file_path is None:
        output_file_path = input_file_path

    delete_toc_in_file(input_file_path, output_file_path)
    generate_toc_in_file(input_file_path, output_file_path)


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=True)
parser.add_argument('-o', '--output', type=str, required=False)
args = parser.parse_args()

generate_toc(args.input, args.output)