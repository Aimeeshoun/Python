import maya.cmds as cmds

sel=(cmds.ls(sl=True))
list_rel=(cmds.listRelatives(sel[0], children=True, shapes=True))
shape=(cmds.listRelatives (sel, shapes=True))
color_index=(cmds.palettePort(color_palette, q=True, setCurCell=True))
def change_color(color_index):
    for node in shape:
        node.overrideEnabled.set(1)
        node.overrideRGBColors.set(1)
        node.overrideColorRGB.set(0.4, 0.2, 0.8)
def ctrl_center(input, color_index2):
    for i in range(len(sels)):
        sels[i]=obj
        center_object = (cmds.xform(obj[0], q=True, rotatePivot=True, worldSpace=True))
        rotation_object = (cmds.xform(obj[0], q=True, rotation=True, worldSpace=True))
        circle_obj=(cmds.circle(r=5))
        edit_ctrl=(cmds.xform(cirle_obj[0], e=True, rotation=(rotation_object), rotatePivot=(center_object))
        change_color(color_index2)
