from paintcompiler import compile_paints
from fontTools.ttLib import TTFont
from fontTools.fontBuilder import addFvar
from fontTools.ttLib.tables._f_v_a_r import Axis

font = TTFont("fonts/variable/BriemHand[wght].ttf")

print("Adding axes...")

axis = Axis()
nameTable = font["name"]
axis.axisNameID = nameTable.addMultilingualName({"en":"Guideline opacity"}, ttFont=font)
axis.axisTag = "GDLN"
axis.minValue = 0
axis.defaultValue = 0
axis.maxValue = 1
font["fvar"].axes.append(axis)
for instance in font["fvar"].instances:
	instance.coordinates["GDLN"] = 0 # ???

print("Adding paints...")
compile_paints(font, open("scripts/paints.py").read())

print("Saving...")
font.save("fonts/variable/BriemHand[wght,GDLN].ttf")
print("fonts/variable/BriemHand[wght,GDLN].ttf")
