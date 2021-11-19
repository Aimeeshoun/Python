import maya.cmds as cmds


#def color_changer(input2):
#    sel2 = cmds.ls(sl=True)
#    for t in range(len(sel2)):
#        curves = cmds.listRelatives(str[t], children=True, shapes=True)[0]
#        for o in range(len(curves)):
#            cmds.setAttr ("str[o].overrideEnabled",1)
#            cmds.setAttr ("str[o].overrideColor",input2)
#            print (curves)
#color_changer('color_option')

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
        replaced_text = cmds.rename(finished_string)
    for i in range(len(sel)):
        obj_translate = cmds.xform(sel[i], query=True, rp=True, worldSpace=True)
        obj_rotate = cmds.xform(sel[i], query=True, rotation=True, worldSpace=True)
        the_string = sel[i].partition("_")
        stg_partition = the_string[2]
        finished_string = the_string[0] + "_ctrl"
        new_name = cmds.rename(finished_string)
        newCircle2 = cmds.circle(r=1.5, n=the_string[0] + '_joint_ctrl')
        create_group = (cmds.group(n=the_string[0] + '_group_ctrl'))
        cmds.xform(create_group, translation=obj_translate, worldSpace=True)
        cmds.xform(create_group, rotation=obj_rotate, worldSpace=True)
        nurvs.append("newCircle")
        color_option = ('input2')
        color_changer('color_option')
        newCircle2 = cmds.circle(r=1.5, n=the_string[0] + '_joint_ctrl')
        create_group = (cmds.group(n=the_string[0] + '_group_ctrl'))
        cmds.xform(create_group, translation=obj_translate, worldSpace=True)
        cmds.xform(create_group, rotation=obj_rotate, worldSpace=True)
        nurvs.append("newCircle")
        color_option = ('input2')
        if len(sel) is 0:
            newCircle2 = cmds.circle(r=1.5, n=the_string[0] + '_joint_ctrl')
            create_group = (cmds.group(n=the_string[0] + '_group_ctrl'))
            newCircle = cmds.circle(r=1.5, n='Joint_ctrl')
            create_group = (cmds.group(n='group_ctrl'))
            nurvs.append("newCircle")
            replaced_text = cmds.rename(finished_string)
        else:
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
        color_changer('color_option')
ctrl_creator('pCylinder3_group_ctrl10', '16')