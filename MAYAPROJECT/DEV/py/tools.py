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


#RENAMER

import maya.cmds as cmds

def renamer(txt_data):
    sel = (cmds.ls(sl=True))
    object_sec = txt_data
    sel.append(object_sec)
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



