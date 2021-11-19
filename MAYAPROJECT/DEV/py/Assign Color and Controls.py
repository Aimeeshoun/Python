import maya.cmds as cmds

sel = (cmds.ls(sl=True))
grpstring = "grp"
ctrlstring = "ctrl"
geostring = "geo"
jntstring = "jnt"
curves=(cmds.ls(type='nurbCurves'))
i=0


def color_changer(input2):
    color_option = input2
    cur_shapes = (cmds.listRelatives(curves[0], children=True, shapes=True))
    control_tochange = cur_shapes
    enable_color = (cmds.setAttr("control_tochange.overrideEnabled", 1))
    over_ridecolor = (cmds.setAttr("control_tochange.overrideColor", input2))


def ctrl_creator(color_option):
    for i in range(len(sel)):
        the_string = sel[i].partition("_")
        stg_partition = the_string[1]
        finished_string = the_string[0] + "_ctrl"
        new_name = cmds.cur_children[0]( n='sphere2' )
        new_name = cmds.rename(finished_string)
        if grpstring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        elif ctrlstring in stg_partitiong:
            replaced_text = cmds.rename(finished_string)
        elif geostring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        elif jntstring in stg_partition:
            replaced_text = cmds.rename(finished_string)
        else:
            replaced_text = cmds.rename(finished_string)
        obj_translate = cmds.xform(sel[i], query=True, rp=True, worldSpace=True)
        obj_rotate = cmds.xform(sel[i], query=True, rotation=True, worldSpace=True)
        newCircle = cmds.circle( r=1.5, n='Joint_ctrl')
        create_group = (cmds.group(n='group_ctrl'))
        cmds.xform(create_group, translation=obj_translate, worldSpace=True)
        cmds.xform(create_group, rotation=obj_rotate, worldSpace=True)
        color_changer(color_option)
ctrl_creator(2)
