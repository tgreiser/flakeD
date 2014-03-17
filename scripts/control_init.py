# me is this DAT.
# 
# frame is the current frame.
# state is true if the timeline is paused.
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def start():
	print ("--- Initializing control "+me.name)
	slider = op('Slider')
	mod = op('Modulate')
	print(slider)
	slider.panel.u.val = op('sliderPreset')[0].eval()
	mod.panel.radio.val = op('modPreset')[0].eval()
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
	
