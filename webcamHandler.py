import glob
import subprocess
import re

def get_devs():
    return list(glob.glob("/dev/video*"))


def get_name(dev):
    dev = dev.replace("/dev/", "")
    with open(f"/sys/class/video4linux/{dev}/name") as name:
        return name.read()

def set_property(dev, prop, value):
    subprocess.call(["v4l2-ctl", "-d", dev, "-c", prop+"="+str(value)])

def get_property(dev, prop):
    return subprocess.check_output(f"v4l2-ctl -d {dev} -C {prop} | sed -e 's/.*://'", shell=True).strip()

def get_limits(dev, prop):
    # TODO: Handle errors!

    l=str(subprocess.check_output("v4l2-ctl -d " + dev + " -l | grep "+ prop, shell = True))
    minimum=int(re.findall("min=\d*", l)[0].replace("min=",""))
    maximum=int(re.findall("max=\d*", l)[0].replace("max=",""))
    return (minimum, maximum)
