# me is this DAT.
# 
# frame is the current frame.
# state is true if the timeline is paused.
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def start():
	name = op('selected')[0, 0]
	print ("--- Initializing control "+me.parent().name + " - " + name)
	slider = op('Slider')
	mod = op('Modulate/slider1')

	sliderVal = op('sliderPreset')[0].eval() if op('sliderPreset')[0].valid else 0
	sliderRange = op('../settings')[name, 'max'] - op('../settings')[name, 'min']
	print("Slider: " + slider.name + " range " + str(sliderRange) + " mapped " + str(sliderVal * sliderRange))
	op('Slider/set').run(sliderVal * sliderRange)
	print("Mod: "+mod.path)

	modVal = op('modPreset')[0].eval() if op('modPreset')[0].valid else 0
	print("Mod value: "+str(modVal))
	#mod.panel.radio.val = modVal
	op('Modulate/slider1/on_change').run(1, 1, modVal)

	op('modPreset').par.chop = "/flaked/modulatorPresets"

	return

def create():
	return

def exit():
	return

def frameStart(frame):
	return

def frameEnd(frame):
	return

def playState(state):
	return
	
