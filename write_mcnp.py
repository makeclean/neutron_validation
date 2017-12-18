#/usr/bin/python

# Class to handle writing a complete MCNP
# input deck to disk
class McnpWriter():
    def __init__(self,input_snippet,nuc):
        """ Constructor for class instantiates the
        McnpWriter class
        
        Keyword arguments
        input_snippet - the snippet of mcnp file to write
        nuc - the nuclide name to write to file
        """

        self.input = input_snippet
        self.nuclide = nuc
        
    def write_mcnp(self,file):
        """ method that writes the whole ready to run
        MCNP input deck
        
        Keyword arguments
        file - filename snippet like xo
        """

        # todo maybe it would be nice to be able to pass
        # spectra bins through also?

        file = file + '.mcnp'
        
        f = open(file,'w')
        for line in self.input:
            if 'material_description' in line:
                line = line.replace("material_description",self.nuclide)
            f.write(line)
        f.close()
        
        return
