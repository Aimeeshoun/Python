

import maya.cmds as cmds


class ToolUI():
    def __init__(self):
        self.m_window = 'changeColorUIWin'
        self.name_txtfield = ''

    def create(self):
        self.delete()
        import tools

        self.m_window = cmds.window(self.m_window, title="Button Window", widthHeight=(200, 55))
        m_column = cmds.columnLayout(parent=self.m_window, adjustableColumn=True)
        cmds.button(parent=m_column, label='Create Ball', command='cmds.polySphere()')
        cmds.button(parent=m_column, label='Grey', backgroundColor=(.400, .4000, .4000),
                    command=lambda x: tools.ChangeColor(0))
        cmds.button(parent=m_column, label='Black', backgroundColor=(.00, .000, .000),
                    command=lambda x: tools.ChangeColor(1))
        cmds.button(parent=m_column, label='Dark Grey', backgroundColor=(.20, .200, .200),
                    command=lambda x: tools.ChangeColor(2))
        cmds.button(parent=m_column, label='Med Grey', backgroundColor=(.30, .300, .300),
                    command=lambda x: tools.ChangeColor(3))
        cmds.button(parent=m_column, label='Red', backgroundColor=(.83233, .242750, .288730),
                    command=lambda x: tools.ChangeColor(4))
        cmds.button(parent=m_column, label='Dark Blue', backgroundColor=(.14454300, .12345000, .76576000),
                    command=lambda x: tools.ChangeColor(5))
        cmds.button(parent=m_column, label='Light Blue', backgroundColor=(.343500, .542000, .7657000),
                    command=lambda x: tools.ChangeColor(6))
        cmds.button(parent=m_column, label='Green', backgroundColor=(.16534500, .3766000, .2345000),
                    command=lambda x: tools.ChangeColor(7))
        cmds.button(parent=m_column, label='Dark Purple', backgroundColor=(.64454300, .32345000, .96576000),
                    command=lambda x: tools.ChangeColor(8))
        cmds.button(parent=m_column, label='Light Purple', backgroundColor=(.74454300, .32345000, .76576000),
                    command=lambda x: tools.ChangeColor(9))
        cmds.button(parent=m_column, label='Brown', backgroundColor=(.64454300, .42345000, .36576000),
                    command=lambda x: tools.ChangeColor(10))
        cmds.button(parent=m_column, label='Dark Brown', backgroundColor=(.74454300, .42345000, .26576000),
                    command=lambda x: tools.ChangeColor(11))
        cmds.button(parent=m_column, label='Red Brown', backgroundColor=(.76534500, .3766000, .2345000),
                    command=lambda x: tools.ChangeColor(12))
        cmds.button(parent=m_column, label='Orange Red', backgroundColor=(.73233, .342750, .288730),
                    command=lambda x: tools.ChangeColor(13))
        cmds.button(parent=m_column, label='Light Green', backgroundColor=(.76534500, .8766000, .6345000),
                    command=lambda x: tools.ChangeColor(14))
        cmds.button(parent=m_column, label='Light Blue Too', backgroundColor=(.343500, .542000, .7657000),
                    command=lambda x: tools.ChangeColor(15))
        cmds.button(parent=m_column, label='White', backgroundColor=(1.00, 1.000, 1.000),
                    command=lambda x: tools.ChangeColor(16))
        cmds.button(parent=m_column, label='Yellow', backgroundColor=(.76534500, .8766000, .2345000),
                    command=lambda x: tools.ChangeColor(17))
        cmds.button(parent=m_column, label='Pastel Blue', backgroundColor=(.243500, .842000, .9657000),
                    command=lambda x: tools.ChangeColor(18))
        cmds.button(parent=m_column, label='Pastel Green', backgroundColor=(.76534500, .8766000, .6345000),
                    command=lambda x: tools.ChangeColor(19))
        cmds.button(parent=m_column, label='Pastel Pink', backgroundColor=(.8783, .698750, .788730),
                    command=lambda x: tools.ChangeColor(20))
        cmds.button(parent=m_column, label='Pastel Orange', backgroundColor=(.734500, .5754000, .5654000),
                    command=lambda x: tools.ChangeColor(21))
        cmds.button(parent=m_column, label='Pastel Yellow', backgroundColor=(.76534500, .8766000, .2345000),
                    command=lambda x: tools.ChangeColor(22))
        cmds.button(parent=m_column, label='Green Kelly', backgroundColor=(.76534500, .8766000, .6345000),
                    command=lambda x: tools.ChangeColor(23))
        cmds.button(parent=m_column, label='Green Brown', backgroundColor=(.26534500, .3766000, .2345000),
                    command=lambda x: tools.ChangeColor(24))
        cmds.button(parent=m_column, label='Green Puke', backgroundColor=(.16534500, .4766000, .2345000),
                    command=lambda x: tools.ChangeColor(25))
        cmds.button(parent=m_column, label='Green Lime', backgroundColor=(.16534500, .4766000, .1345000),
                    command=lambda x: tools.ChangeColor(26))
        cmds.button(parent=m_column, label='Green Swamp', backgroundColor=(.76534500, .8766000, .6345000),
                    command=lambda x: tools.ChangeColor(27))
        cmds.button(parent=m_column, label='Grey Blue', backgroundColor=(.334500, .4754000, .5654000),
                    command=lambda x: tools.ChangeColor(28))
        cmds.button(parent=m_column, label='Elephant Blue', backgroundColor=(.343500, .542000, .7657000),
                    command=lambda x: tools.ChangeColor(29))
        cmds.button(parent=m_column, label='Purple', backgroundColor=(.343500, .242000, .7657000),
                    command=lambda x: tools.ChangeColor(30))
        cmds.button(parent=m_column, label='Magenta', backgroundColor=(.74454300, .32345000, .76576000),
                    command=lambda x: tools.ChangeColor(31))
        cmds.button(parent=m_column, label='Control Builder', command=lambda x: tools.ctrl_creator())
        cmds.button(parent=m_column, label='Default Control', command=lambda x: tools.CreateControl())
        self.name_txtfield = (cmds.textField(parent=m_column))
        cmds.button(parent=m_column, label='Enter',
                    command=lambda x: self.renamer_cmd())

        cmds.showWindow(self.m_window)

    def delete(self):
        if cmds.window(self.m_window, exists=True):
            cmds.deleteUI(self.m_window)

    def renamer_cmd(self):
        import tools
        tools.name_sequence(cmds.textField(self.name_txtfield, q=True, text=True))
        return


myUI = ToolUI()
myUI.create()


