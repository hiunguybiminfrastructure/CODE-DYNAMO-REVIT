"""Copyright(c) 2024 by: nguyenminhhieu18062003@gmail.com"""
import clr 
import sys
sys.path.append(r'C:\Program Files\Autodesk\Revit 2023\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8')
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#Preparing input from dynamo to revit
elements = UnwrapElement(IN[0])

def getDBLineByLines(elements):
    re = []
    for i in elements:
        crv = i.GeometryCurve
        re.append(crv)
    return re

factor = IN[1]
dbLines = getDBLineByLines(element)

points = [dbLine.Evaluate(factor, True).ToPoint() for dbLine in dbLines]

OUT = points