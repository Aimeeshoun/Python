
import maya.cmds as cmds

sels = cmds.ls(sl=True)

def name_sequence(input):

    for i in range(len(sels)):
        string_a = input
        spi_sent2= string_a.split()
        for e in spi_sent2:
            alphabet = e
            num_pounds = alphabet.count("#")  
            print =num_pounds 
            if num_pounds is 2:
                the_string = string_a.partition("##")
            elif num_pounds is 3:
                the_string = string_a.partition("###")
            elif num_pounds is 4:
                the_string = string_a.partition("####")
            elif num_pounds is 1:
                the_string = string_a.partition("#")
        num_pounds = the_string[1].count("#")
        finished_string = the_string[0] + str(i).zfill(num_pounds) + the_string[2]
        new_name = cmds.rename(finished_string)    
    return