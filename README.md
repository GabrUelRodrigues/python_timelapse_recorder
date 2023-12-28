# Python Timelapse Recorder
## Timelapse screen recorder made using Python

This project is a simple timelapse screen recorder made using PySimpleGUI, Pillow and MoviePy. I captures your screen after a fixed interval (in seconds) and can also render the captured images as a video file.

## Setup and run

In order to run this project, make sure you already have Python installed, then follow the instructions:

1. Clone this repository
2. Install `PySimpleGUI`, `Pillow`, `Natsort` and `MoviePy`
   
   ```bash
   pip install pysimplegui pillow natsort moviepy
   ```
   
3. Run the `main.py` file in the project directory

   ```bash
   python main.py
   ```

## Usage
### Capturing

On the capture tab, you can define the screen area to be captured, the interval in seconds between each capture, and the destination of the image files. After setting everything up, press the `Start` button to start capturing your screen. To stop capturing, press the `Stop` button.

### Rendering

If you want to render the images as a video file, go to the render tab, type the video resolution you want, the number of frames per second and a path where the video file will be saved, after this, press the `Render` button. The ui will freeze for a couple of seconds while the video renders, after that, you can close the application.
It's worth knowing that the images will be taken from the same directory they were previously saved, so if you want to render images from another directory, simply inform the path that directory on the capture tab.
