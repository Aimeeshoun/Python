#COLOR CHANGER
import maya.cmds as cmds
def ChangeColor(color):
    sels = cmds.ls(sl=True)
    for sel in sels:
        shapes = cmds.listRelatives(sel, children=True, shapes=True)
        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % (shape), True)
            cmds.setAttr('%s.overrideColor' % (shape), color)
    return

# THIS IS A DEFAULT CONTROL CREATOR


import maya.cmds as cmds
def CreateControl():
    nurvs = []
    newCircle = cmds.circle(r=1.5, n='Joint_ctrl')
    create_group = (cmds.group(n='group_ctrl'))
    nurvs.append("newCircle")
    return





#CONTROL CREATOR

import maya.cmds as cmds

def ctrl_creator():
    sel = (cmds.ls(sl=True))
    grpstring = "grp"
    ctrlstring = "ctrl"
    geostring = "geo"
    jntstring = "jnt"
    nurvs = [];
    for i in sel:
        obj_translate = cmds.xform(i, query=True, rp=True, worldSpace=True)
        obj_rotate = cmds.xform(i, query=True, rotation=True, worldSpace=True)
        nurvs.append("newCircle")
        the_string = i.partition("_")
        stg_partition = the_string[2]
        finished_string = the_string[0] + "_ctrl"
        new_name = cmds.rename(finished_string)
        newCircle2 = cmds.circle(r=1.5, n=the_string[0] + '_joint_ctrl')
        create_group = (cmds.group(n=the_string[0] + '_group_ctrl'))
        cmds.xform(create_group, translation=obj_translate, worldSpace=True)
        cmds.xform(create_group, rotation=obj_rotate, worldSpace=True)
        if grpstring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        elif ctrlstring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        elif geostring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        elif jntstring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        elif object_selection is '':
            replaced_text = cmds.rename(finished_string)
    sel.append(object_sec)

    return



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
