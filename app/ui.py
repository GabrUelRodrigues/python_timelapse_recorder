import PySimpleGUI as sg

def app_window() -> sg.Window:
	sg.theme("DarkGrey14")

	settings_frame = [
		[
			sg.Text("Area:"), sg.Input(key="-BOX_X-", default_text="0", size=(4, 1)), sg.Input(key="-BOX_Y-", default_text="0", size=(4, 1)),
			sg.Input(key="-BOX_W-", default_text="1366", size=(4, 1)), sg.Input(key="-BOX_H-", default_text="768", size=(4, 1)),
		],
		[sg.Text("Interval (sec):"), sg.Spin(key="-INTERVAL-", values=[i for i in range(1, 3600)], initial_value=1, size=(4, 1))],
		[sg.Text("Save path:"), sg.Input(key="-CAPTURE_DESTINATION-", size=(25, 1)), sg.FolderBrowse(initial_folder="./")]
	]

	settings_tab = [
		[sg.Frame("", layout=settings_frame, key="-SETTINGS-", relief=sg.RELIEF_FLAT)],
		[sg.Button("Start"), sg.Button("Stop")]
	]

	render_frame = [
		[sg.Text("Resolution:"), sg.Input(key="-VIDEO_WIDTH-", default_text="1920", size=(4, 1)), sg.Input(key="-VIDEO_HEIGHT-", default_text="1080", size=(4, 1))],
		[sg.Text("FPS:"), sg.Input(key="-FPS-", default_text="60", size=(3, 1))],
		[sg.Text("Save path:"), sg.Input(key="-RENDER_DESTINATION-", size=(25, 1)), sg.FolderBrowse(initial_folder="./")]
	]

	render_tab = [
		[sg.Frame("", layout=render_frame, key="-RENDER-", relief=sg.RELIEF_FLAT)],
		[sg.Button("Render")]
	]

	window_layout=[
		[sg.TabGroup([
			[
				sg.Tab("Capture", settings_tab),
				sg.Tab("Render", render_tab)
			]
		], key="-TABS-")],
		[sg.Text("", key="-STATUS-")]
	]

	return sg.Window("Timelapse Recorder", layout=window_layout, finalize=True)