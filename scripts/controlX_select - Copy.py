# me is this DAT.
# 
# dat is the changed DAT.
# rows is a list of row indices.
# cols is a list of column indices.
# cells is the list of cells that have changed content.
# prev is the list of previous string contents of the changed cells.
# 
# Make sure the corresponding toggle is enabled in the DAT Execute DAT.
# 
# If rows or columns are deleted, sizeChange will be called instead of row/col/cellChange.


def tableChange(dat):
	print(dat.rows[0].cells[0])
	return

def rowChange(dat, rows):
	return

def colChange(dat, cols):
	return

def cellChange(dat, cells, prev):
	return

def sizeChange(dat):
	return
	

