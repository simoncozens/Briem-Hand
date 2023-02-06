RED = "#FF141DFF"
ORANGE = "#FB7236FF"
LOW_GREEN = "#14FF1D22"
HIGH_GREEN = "#72FB3655"
LOW_BLUE = "#141DFFFF"
HIGH_BLUE = "#7236FB55"
TRANSPARENT = "#00000000"

# Getting widths out of a variable font is hard, let's
# get them out of the sources instead
import glyphsLib

source = glyphsLib.load(open("sources/BriemHand.glyphs"))
widths = {}
for glyph in source.glyphs:
	widths[glyph.production or glyph.name] = [l.width for l in glyph.layers]

for gname in font.getGlyphOrder():
	if gname not in widths:
		continue
	w1 = widths[gname][0] / widths["bline"][0]
	w2 = widths[gname][1] / widths["bline"][1]
	if w1 >= 2:
		print(f"Could not stretch line for glyph {gname}")
		continue
	glyphs[gname] = PaintColrLayers([
	 	# Baseline
	 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 1.0,
		 	PaintGlyph("bline", PaintVarSolid("foreground", "GDLN=0:0 GDLN=1:1"))
	 	),
	 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 1.0,
		 	PaintGlyph("bline", PaintVarSolid([TRANSPARENT, LOW_BLUE], "GDLN=0:0 GDLN=1:1"))
	 	),
	 	# X height
	 	PaintTranslate(0, 500,
		 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 1.0,
			 	PaintGlyph("bline", PaintVarSolid("foreground", "GDLN=0:0 GDLN=1:1"))
		 	),
		),
	 	PaintTranslate(0, 500,
		 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 1.0,
			 	PaintGlyph("bline", PaintVarSolid([TRANSPARENT, LOW_BLUE], "GDLN=0:0 GDLN=1:1"))
		 	),
		),
	 	# Descender
	 	PaintTranslate(0, -315,
		 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 0.5,
			 	PaintGlyph("bline", PaintVarSolid("foreground", "GDLN=0:0 GDLN=1:1"))
		 	)
	  ),
	 	PaintTranslate(0, -315,
		 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 0.5,
			 	PaintGlyph("bline", PaintVarSolid([TRANSPARENT, RED], "GDLN=0:0 GDLN=1:1"))
		 	)
	  ),
		# Ascender
	 	PaintTranslate(0, 784,
		 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 0.5,
			 	PaintGlyph("bline", PaintVarSolid("foreground", "GDLN=0:0 GDLN=1:1"))
		 	)
	  ),
	 	PaintTranslate(0, 784,
		 	PaintVarScale(f"wght=100:{w1} wght=900:{w2}", 0.5,
			 	PaintGlyph("bline", PaintVarSolid([TRANSPARENT, RED], "GDLN=0:0 GDLN=1:1"))
		 	)
	  ),
		# Glyph
	 	PaintGlyph(gname, PaintSolid("foreground")),
])
