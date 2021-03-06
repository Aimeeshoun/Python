from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
import maya.cmds as cmds
import maya.OpenMayaRender as OpenMayaRender
import maya.app.renderSetup.common.profiler as profiler


if False:
    from typing import Dict, List, Tuple, Union, Optional

def rename(oldLegacyRenderLayerName, newParentName): ...
def renderSetupLayer(legacyRenderLayerName): ...
def removeNodes(legacyRenderLayerName): ...
def create(parentName): ...
def appendNodes(legacyRenderLayerName, nodeNames): ...
def setRenderable(legacyRenderLayerName, value): ...
def makeVisible(legacyRenderLayerName): ...
def isVisible(legacyRenderLayerName): ...
def delete(legacyRenderLayerName): ...
def isRenderable(legacyRenderLayerName): ...

