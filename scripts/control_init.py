# me is this DAT.
# 
# frame is the current frame.
# state is true if the timeline is paused.
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def start():
	print ("--- Initializing control "+me.parent().name)
	slider = op('Slider')
	mod = op('Modulate/slider1')
	print("Slider: " + slider.name)
	slider.panel.u.val = op('sliderPreset')[0].eval()
	print("Mod: "+mod.path)
	mod.panel.radio.val = op('modPreset')[0].eval()
	print("Mod value: "+str(mod.panel.radio.val))
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
	
