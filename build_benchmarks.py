#/usr/bin/python

import argparse
import os


def write_input_for_code(nuc,code):
    """ Writes the input for the benchmark 
    for a given nuclide and code

    Keyword arguments
    nuc - the string identifying the nuclide
    code - the name of the code to write the benchmark 
    for
    """
    
    

    return

def make_directory_for_code(nuc,code):
    """ makes the directory for a given
    code and nuclide, then calls to write the
    specific input
    
    nuc - the string name for the nuclide
    code - the string for the given code
    """

    os.mkdir(nuc+'/'+code)
    write_input_for_code(nuc,code)

    return

def make_directory_for_nuc(nuc,codes):
    """ makes the directory tree for a given
    nuclide, but all the codes, including 
    writing the input deck

    Keyword arguments
    nuc - the string identifying the specific 
          nuclide
          
    codes - the list of codes to write the 
    benchmark for
    """

    for code in codes:
        make_directory_for_code(nuc,code)
    return


def make_directories(nuclides,codes):
    """ makes the whole directory structure 
    for the entire benchmark problem, including
    writing input decks
    
    Keyword arguments
    nuclides - list of nuclide names to write input for
    codes - list of codes to write inputs for
    """

    for nuc in nuclides:
        make_directory_for_nuc(nuc,codes)
    return



parser = argparse.ArgumentParser(description='Tool to setup neutron transport benchmarks')

# set the options
parser.add_argument('-x','--xsdir', default="xsdir", help='Set the xsdir to scan to figure out the case to run')
parser.add_argument('-c','--codes',  nargs='+', help = "output files to write for which codes")
parser.add_argument('-n','--nuclides', nargs='+', help = "run the nuclides in this list rather than from an xsdir")
parser.add_argument('-b','--benchmarks', nargs='+', help = "The benchmarks to run; sphere and cylinder are currently allowed")

# parse all the options
args = parser.parse_args()




 
