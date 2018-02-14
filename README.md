# Deep Learning Bird Camera

NVIDIA Jetson Powered Deep Learning Bird Camera

## What is this?

This is a repo specifically for my Deep Learning Bird Camera platform. It's a plywood / 3D printed platform running a YOLO v2 model to detect birds.

It's eventual goal is to build a computation platform to detect, identify, and interact with specifci bird species, and evetually, specific birds in the wild.

It's inspired by the [insane intelligence](https://www.youtube.com/watch?v=URZ_EciujrE) of crows, and aims to eventually be a platform for exploring crow intelligence via robotics and games.

For now, it's a system to automatically identify birds, and record videos of them. 

## How does it work?

The NVIDIA Jetson TX1 is connected to a webcam, and runs a YOLO v2 model on every 5th frame or so.

When the model detects a bird, it records a video and makes a web request to an Rasberry Pi connected on the same WIFI network, and mounted in to the same box.

This Raspberry Pi will eventually be the platform for robotic response upon the detection of birds. It's much cheaper to accidentally fry a Raspberry Pi than a TX1.

These detected images and video frames are then saved to disk on a 512 GB SSD attached to the TX1. 

Eventually, these detected images will be available through a web based interface. For now, you must ssh into the TX1, and `scp` the images back to your computer.


