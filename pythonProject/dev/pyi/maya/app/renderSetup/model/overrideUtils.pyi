from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
from . import namespace
from . import enabled
import weakref
import itertools
from . import localOverride
from . import childNode


from maya.app.renderSetup.model.connectionOverride import *


from maya.app.renderSetup.model.override import Property
from maya.app.renderSetup.model.override import fillVector
from maya.app.renderSetup.model.override import RelUniqueOverride
from maya.app.renderSetup.model.override import RelOverride
from maya.app.renderSetup.model.override import LeafClass
from maya.app.renderSetup.model.override import attributeToPlug
from maya.app.renderSetup.model.override import Override
from maya.app.renderSetup.model.override import valid
from maya.app.renderSetup.model.override import finalizationChanged
from maya.app.renderSetup.model.override import AbsUniqueOverride
from maya.app.renderSetup.model.override import UnapplyCmd
from maya.app.renderSetup.model.override import UniqueOverride
from maya.app.renderSetup.model.override import ValueOverride
from maya.app.renderSetup.model.override import AbsOverride
from maya.app.renderSetup.model.override import OverridePlugHandle
from collections import namedtuple


if False:
    from typing import Dict, List, Tuple, Union, Optional

def create(*args, **kwargs): ...
def getAllOverrideClasses():
    """
    Returns the list of Override subclasses
    """
    ...
def delete(*args, **kwargs): ...


kUnconnectableAttr : unicode
kUnapplyCmdPrivate : unicode
kMissingDependencies : unicode
kUnfinalized : unicode

