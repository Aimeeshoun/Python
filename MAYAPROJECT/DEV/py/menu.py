import maya.cmds as cmds


class ToolUI():
    def __init__(self):
        self.m_window = 'changeColorUIWin'
        pass


    def create(self):
        self.delete()

        self.m_window = cmds.window(self.m_window,
                                title="Boring Tile",
                                widthHeight=(200, 55))
        m_columnLayout(parent=self.m_window,
                   adjustableColumn=True)
 #      cmds.button(parent.m_column, label='Ball', commands='cmds.polySphere()')
  #     cmds.button(parent.m_column, label='redcolor', commands='cmds.polySphere()')
#       cmds.button(parent.m_column, label='bluecolor', commands='cmds.polySphere()')
 #      cmds.button(parent.m_column, label='greencolor', commands='cmds.polySphere()')
 #      cmds.button(parent.m_column, label='remaner', commands='cmds.polySphere()')
 #      cmds.button(parent.m_column, label='controls', commands='cmds.polySphere()')
  #     cmds.button(parent.m_column, label='default control', commands='cmds.polySphere()')

        cmds.showWindow(self.m_window)


    def delete(self):
        if cmds.window(self.m_window, exists=True):
            cmds.deleteUI(self.m_window)