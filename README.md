# Essential WebCam controls overlay

Do you have a webcam that goes crazy when the sun shine behind you?

Do you want to replace the crappy self-exposition control of your webcam?

This is the software for you ;)

# How it works

An always-on-top dialog window will be displayed, allowing you to set the main parameters of the webcam.

## Under the hood

This program does not use special libraries to deal with the Video4Linux2 subsystem.

Instead, it relies on the `v4l2-ctl` utility, without any particular requirements on your system.

# Requirements

* A modern Linux system
* PyGObject, see their [getting started](https://pygobject.readthedocs.io/en/latest/getting_started.html#arch-getting-started) guide.
* A working V4L2 setup (which should be granted on modern installations)
* A webcam :P

# Installation and usage

Just clone this repository and execute `webcamEssentials.py`.

You can pass the `-d DEVICE` if you have multiple devices on your system.

With `-l` you can have a list of all devices on your system.

# License

This software is distributed under the GNU GPL v3 license. See [LICENSE](LICENSE).

(C) 2020 Massimo Girondi
