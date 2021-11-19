import maya.cmds as cmdss

sel = (cmdss.ls(sl=True))
list_rel = (cmdss.listRelatives(sel[0], children=True, shapes=True))


def change_color(index):
    if ctl == 'C':
        color_shape = (cmdss.listRelatives(sel[0], children=True, shapes=True))
        color_shape = color_shape[0]
        n.setAttr(color_shape + '.overrideEnabled', 1)
        n.setAttr(color_shape + '.overrideRGBColors', 14)


def ctrl_center(input, color_index2):
    for i in range(len(sel)):
        sel[i] = obj
        center_object = (cmdss.xform(obj[0], q=True, rotatePivot=True, worldSpace=True))
        rotation_object = (cmdss.xform(obj[0], q=True, rotation=True, worldSpace=True))
        circle_obj = (cmdss.circle(r=5))
        edit_ctrl = (cmdss.xform(cirle_obj[0], e=True, rotation=rotation_object, rotatePivot=center_object)
                     change_color(color_index)
