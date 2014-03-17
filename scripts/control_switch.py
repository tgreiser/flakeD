# newval and oldval
#
# Add oldval to the constants and remove newval from the constants
newval = args[0]
oldval = args[1]

print("Newval="+newval+" Oldval="+oldval)
active = op('/flaked/controls/activeChans')
inactive = op('/flaked/controls/inactiveChans')
oldindex = inactive[oldval, 0].rows if inactive[oldval, 0] else None
if (oldindex):
	# set value
	print("Found oldindex"+oldindex)
else:
	print("no oldindex, checking active for "+oldval)
	# add oldindex to constants
	activeIndex = active[oldval, 0].rows
	inactive.appendRow(active.row(activeIndex))
	active.deleteRow(activeIndex)
