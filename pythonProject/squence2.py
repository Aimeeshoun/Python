import maya.cmds as cmds

sels = cmds.ls(sl=True)

def name_sequence(input):
    i = 0
    for i in range(len(sels)):
        string_a = input
        the_string = string_a.partition("##")
        num_pounds = the_string[1].count("#")
        finished_string = the_string[0] + str(i).zfill(num_pounds) + the_string[2]
        new_name = cmds.rename(finished_string)
name_sequence("Leg_##_Jnt")