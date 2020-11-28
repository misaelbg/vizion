# Vizion - Real world, object detection and recognition

[![Build Status](https://travis-ci.org/misaelbg/vizion.svg?branch=master)](https://travis-ci.org/misaelbg/vizion)

Detection and Classification of objects in real time. Train your own neural network to classify any type of objects in the real world easily.

## Usage

	usage: vizion [-h]

**Object detection:** Images

	vizion image --detect cars --model default

This will download 10 cat images and metadata from Google Images.

**Object detection:** Video

	vizion video --detect cars --model default