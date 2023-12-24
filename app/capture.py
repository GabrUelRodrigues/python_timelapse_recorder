import time
import os
import numpy as np
from datetime import datetime
from PIL import ImageGrab, Image
from moviepy.editor import ImageSequenceClip

class Capture:
	def __init__(self) -> None:
		self.area: tuple[int, int, int, int]
		self.interval: int
		self.destination: str

		self.frame: int = 0
		self.last_capture_time: float = 0
		self.recording: bool = False
	
	def setup(self, area: tuple[int, int, int, int], interval: int, path: str) -> None:
		self.area = area
		self.interval = interval
		self.destination = os.path.realpath(os.path.join(path, f"Capture-{datetime.now().time()}"))

	def update(self) -> None:
		if self.recording and self.elapsed_time() >= self.interval:
			self.last_capture_time = time.time()
			self.frame += 1
			self.record()

	def elapsed_time(self) -> float:
		return time.time() - self.last_capture_time

	def record(self) -> None:
		frame = ImageGrab.grab(bbox=self.area)
		frame.save(os.path.realpath(f"{self.destination}-{self.frame}.png"))

	def start_recording(self) -> None:
		self.recording = True

	def stop_recording(self) -> None:
		self.recording = False
	
	def render(self, input_path: str, resolution: tuple[int, int], fps: int, path: str) -> None:
		images = [file for file in os.listdir(input_path) if file.endswith((".png"))]
		frames = []
		destination = os.path.realpath(f"{path}/Capture-{datetime.now().time()}.mp4")

		for image in images:
			with Image.open(os.path.realpath(os.path.join(input_path, image))) as frame:
				frame = np.array(frame.resize(size=resolution))
				frames.append(frame)
		
		if len(frames) > 0:
			clip = ImageSequenceClip(sequence=frames, fps=fps)
			clip.write_videofile(filename=destination, fps=fps, codec="libx264")
