from .ui import *
from .capture import Capture

def main() -> None:
	window = app_window()
	capture = Capture()

	window["Stop"].update(disabled=True) # type: ignore

	while True:
		event, values = window.read(1) # type: ignore

		if event == sg.WIN_CLOSED:
			break

		elif event == "Start":
			try:
				window["-STATUS-"].update("Recording...") # type: ignore
				window["Stop"].update(disabled=False) # type: ignore
				window["Start"].update(disabled=True) # type: ignore
				window["Render"].update(disabled=True) # type: ignore

				capture_area = (int(values["-BOX_X-"]), int(values["-BOX_Y-"]), int(values["-BOX_W-"]), int(values["-BOX_H-"]),)
				capture_interval = int(values["-INTERVAL-"])
				capture_destination = values["-CAPTURE_DESTINATION-"]

				capture.setup(capture_area, capture_interval, capture_destination)
				capture.start_recording()
			
			except(PermissionError):
				sg.Popup("Permission denied!", title="Error!")
			
			except(FileNotFoundError):
				sg.Popup("No such file or directory!", title="Error!")
			
			except(FileExistsError):
				sg.Popup("File already exists!", title="Error!")
		
		elif event == "Stop":
			window["-STATUS-"].update("Stop!") # type: ignore
			window["Stop"].update(disabled=True) # type: ignore
			window["Start"].update(disabled=False) # type: ignore
			window["Render"].update(disabled=False) # type: ignore
			capture.stop_recording()
		
		elif event == "Render":
			try:
				window["-STATUS-"].update("Done!") # type: ignore

				render_input = values["-CAPTURE_DESTINATION-"]
				render_resolution = (int(values["-VIDEO_WIDTH-"]), int(values["-VIDEO_HEIGHT-"]))
				render_framerate = int(values["-FPS-"])
				render_destination = values["-RENDER_DESTINATION-"]

				capture.render(render_input, render_resolution, render_framerate, render_destination)
			
			except(PermissionError):
				sg.Popup("Permission denied!", title="Error!")
			
			except(FileNotFoundError):
				sg.Popup("No such file or directory!", title="Error!")
			
			except(FileExistsError):
				sg.Popup("File already exists!", title="Error!")
		
		capture.update()
