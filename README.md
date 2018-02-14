# Deep Learning Bird Camera

![Jetson Deep Learning Bird Camera](https://github.com/burningion/deep-learning-bird-camera/raw/master/images/closed.jpg)

## What is this?

This is a repo specifically for my Deep Learning Bird Camera platform. It's a plywood / 3D printed platform running a YOLO v2 model to detect birds.

The goal is to build a computation platform to detect, identify, and interact with individual birds in the wild.

It's inspired by the [insane intelligence](https://www.youtube.com/watch?v=URZ_EciujrE) of crows, and aims to eventually be a platform for exploring crow intelligence via robotics and games.

For now, it's a system to automatically identify birds, take actions, and record videos of them. 

The plan is to use these videos as data to train better bird inference model.

## How does it work?

![NVIDIA Jetson Powered Deep Learning Bird Camera](https://github.com/burningion/deep-learning-bird-camera/raw/master/images/architecture.png)

The NVIDIA Jetson TX1 is connected to a webcam, and runs a YOLO v2 model on every 5th frame or so.

When the model detects a bird, it records a video and makes a web request to an Rasberry Pi connected on the same WIFI network, and mounted in to the same box.

This Raspberry Pi will eventually be the platform for robotic response upon the detection of birds. It's much cheaper to accidentally fry a Raspberry Pi than a TX1.

These detected images and video frames are then saved to disk on a 512 GB SSD attached to the TX1. 

Eventually, these detected images will be available through a web based interface. For now, you must ssh into the TX1, and `scp` the images back to your computer.

## How was it built?

![Jetson Deep Learning Bird Camera](https://github.com/burningion/deep-learning-bird-camera/raw/master/images/open.jpg)

The shell of the deep learning camera is a plywood box, that's been painted.

The plan is to add individual modules (like food dispensors, buttons, etc) to the Deep Learning Bird Camera, by drilling 1" holes in the box.

Modules for the device will then fit inside these 1" holes, allowing for expandability.

The current modules are in the `stl` folder of this repository, and were 3D printed using PLA and a Prusa i3 MK2 printer. They were sliced using PrusaControl, and the models themselves were scaled to 41% for printing.

(Since the models were designed in Blender, using Blender's built in units, they don't really translate when exporting as STL.)

![Birds in Action](https://github.com/burningion/deep-learning-bird-camera/raw/master/images/birds.gif)
