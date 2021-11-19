import maya.cmds as cmds


def re_color():
    sels = (cmds.ls(sl=True))
    for sel2 in sels:
        new_shape = cmds.listRelatives(sel2, children=True, shapes=True)[0]
        new_shapes = (sel + ": " + ','.join(new_shape))
        for q in new_shapes:
            shape_node = q
            cmds.setAttr(shape_node + ".overrideEnabled", 1)
            cmds.setAttr(shape_node + ".overrideColor", "color_option")

def ctrl_creator(object_selection, color_option):
    sel = (cmds.ls(sl=True))
    grpstring = "grp"
    ctrlstring = "ctrl"
    geostring = "geo"
    jntstring = "jnt"
    object_sec = object_selection
    if len(sel) is 0:
        newCircle = cmds.circle(r=1.5, n='Joint_ctrl')
        create_group = (cmds.group(n='group_ctrl'))
        nurvs.append("newCircle")
    for i in range(len(sel)):
        obj_translate = cmds.xform(sel[i], query=True, rp=True, worldSpace=True)
        obj_rotate = cmds.xform(sel[i], query=True, rotation=True, worldSpace=True)
        nurvs.append("newCircle")
        the_string = sel[i].partition("_")
        stg_partition = the_string[2]
        finished_string = the_string[0] + "_ctrl"
        new_name = cmds.rename(finished_string)
        color_option = ('input2')
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
    re_color("color_option")
ctrl_creator('pCylinder3_ctrl53', '16')