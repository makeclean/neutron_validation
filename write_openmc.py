#/usr/bin/python

# Class to handle writing a complete OpenMCWriter
# input deck to disk
class OpenMCWriter():
    def __init__(self,input_snippet,nuc):
        """ Constructor for class instantiates the
        OpenMCWriter class
        
        Keyword arguments
        input_snippet - the snippet of mcnp file to write
        nuc - the nuclide name to write to file
        """

        self.input = input_snippet
        self.nuclide = nuc
        
    def write_openmc(self):
        """ method that writes the whole ready to run
        OpenMC Problem
        
        Keyword arguments
    
        """

        write_crosssections_file()
        write_geometry_file()
        write_tally_file()
        write_settings_file()
        
        return

    def write_crosssections_file():
        """ Method that writes the 
        cross sections.xml file for openmc

        Keyword arguments
        None
        """
        
        file = "cross_sections.xml"

        
        
        return
