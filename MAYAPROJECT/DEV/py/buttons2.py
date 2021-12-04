
import maya.cmds as cmds
window = cmds.window(title="Long Name", iconName='Short Name', widthHeight=(200,55 ))
layout1 = cmds.rowColumnLayout(numberOfColumns=3, parent=window)
cmds.button(parent=layout1, label=' ball', command='cmds.polySphere()')
cmds.button(parent=layout1, label='wire frame/red', command='ChangeColor(13)')
cmds.button(parent=layout1, label='wire frame/pink', command='ChangeColor(9)')
cmds.button(parent=layout1, label='wire frame/yellow', command='ChangeColor(17)')
cmds.button(parent=layout1, label='wire frame/brown', command='ChangeColor(10)')
cmds.button(parent=layout1, label='wire frame/black', command='ChangeColor(1)')
cmds.button(parent=layout1, label='wire frame/blue', command='ChangeColor(6)')
cmds.button(parent=layout1, label='wire frame/green', command='ChangeColor(14)')
cmds.button(parent=layout1, label='wire frame/purple', command='ChangeColor(30)')
cmds.button(parent=layout1, label='default control', command='CreateControl()')
cmds.button(parent=layout1, label='controls', command='ctrl_creator()')
cmds.button(parent=layout1, label='rename ctrl', command='renamer()')


cmds.showWindow(window)




import maya.cmds as cmds

def ChangeColor(color):
    sels=cmds.ls(sl=True)
    for sel in sels:
        shapes = cmds.listRelatives(sel, children=True, shapes=True)
        for shape in shapes:
            cmds.setAttr( "%s.overrideEnabled" % (shape),True)
            cmds.setAttr( "%s.overrideColor" % (shape),color)
        return

ChangeColor()


import maya.cmds as cmds
def ctrl_creator():
    sel = (cmds.ls(sl=True))
    grpstring = "grp"
    ctrlstring = "ctrl"
    geostring = "geo"
    jntstring = "jnt"
    nurvs = [];
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


ctrl_creator()


def CreateControl():
    newCircle = cmds.circle(r=1.5, n='Joint_ctrl')
    create_group = (cmds.group(n='group_ctrl'))
    nurvs.append("newCircle")  
CreateControl()    
    
    
    
    
def grouper():
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
        
        
        
        
        
        
        
import maya.cmds as cmds
def ctrl_creator():
    sel = (cmds.ls(sl=True))
    grpstring = "grp"
    ctrlstring = "ctrl"
    geostring = "geo"
    jntstring = "jnt"
    nurvs = [];
    for i in range(len(sel)):
        obj_translate = cmds.xform(sel[i], query=True, rp=True, worldSpace=True)
        obj_rotate = cmds.xform(sel[i], query=True, rotation=True, worldSpace=True)
        nurvs.append("newCircle")
        the_string = sel[i].partition("_")
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
ctrl_creator()




import maya.cmds as cmds
def renamer():
    sel = (cmds.ls(sl=True))
    grpstring = "grp"
    ctrlstring = "ctrl"
    geostring = "geo"
    jntstring = "jnt"
    nurvs = [];
    for i in range(len(sel)):
        obj_translate = cmds.xform(sel[i], query=True, rp=True, worldSpace=True)
        obj_rotate = cmds.xform(sel[i], query=True, rotation=True, worldSpace=True)
        nurvs.append("newCircle")
        the_string = sel[i].partition("_")
        stg_partition = the_string[2]
        finished_string = the_string[0] + "_ctrl"
        new_name = cmds.rename(finished_string)
renamer()

import maya.cmds as cmds
def changeControlBlue()
    sel = (cmds.ls(sl=True))

    cmds.setAttr(new_shape + ".overrideEnabled", 1)
    cmds.setAttr(new_shape + ".overrideColor", 2)
    
    
    
    
    
    
    
import maya.cmds as cmds

def re_color(input):
    sels = (cmds.ls(sl=True))
    for sel2 in sels:
        new_shape = (cmds.listRelatives(sel2, children=True, shapes=True)[0])
        print (new_shape)
        cmds.setAttr(new_shape + ".overrideEnabled", 1)
        cmds.setAttr(new_shape + ".overrideColor", 2)
        
        
        
        
        

from maya import cmds


window = cmds.window( title="Long Name", iconName='Short Name', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Do Nothing' )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )        
        
        
        
        

from maya import cmds


window = cmds.window( title="default control", iconName='ctrl', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='default control', command='CreateControl()' )
cmds.setParent( '..' )
cmds.showWindow( window )  






from maya import cmds


window = cmds.window( title="controls", iconName='ctrls', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='controls', command='ctrl_creator()' )
cmds.setParent( '..' )
cmds.showWindow( window )  






from maya import cmds


window = cmds.window( title="renamer", iconName='name', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='rename ctrl', command='renamer()' )
cmds.setParent( '..' )
cmds.showWindow( window )    

cmds.button(parent=layout1, label='rename ctrl', command='renamer()')     




from maya import cmds


window = cmds.window( title="wire frame/red", iconName='red', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='wire frame/red', command='ChangeColor(13)')
cmds.setParent( '..' )
cmds.showWindow( window )    

cmds.button(parent=layout1, label='rename ctrl', command='renamer()')  


from maya import cmds


window = cmds.window( title="wire frame/blue", iconName='blue', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='wire frame/blue', command='ChangeColor(6)')
cmds.setParent( '..' )
cmds.showWindow( window )    



from maya import cmds


window = cmds.window( title="wire frame/green", iconName='green', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='wire frame/green', command='ChangeColor(14)')
cmds.setParent( '..' )
cmds.showWindow( window )    

        