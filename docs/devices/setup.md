# Raspberry Pi Setup Guide

This guide documents the steps to set up  Raspberry Pi.


## Introduction

This guide provides a step-by-step walkthrough of setting up a Raspberry Pi for various projects and use cases.







### Install an operating system

Install it from a terminal using your package manager.

```bash 
sudo apt install rpi-imager
```

![Local Image](/home/adit/Documents/Stockholm University/IOT/iot-ht2023-data-protocols/docs/devices/img/1.png)


After installing the Imager, launch the application by  running:
```bash 
rpi-imager.
```

![Local Image](/home/adit/Documents/Stockholm University/IOT/iot-ht2023-data-protocols/docs/devices/img/2.png)


Click Choose device and select your Raspberry Pi model from the list.

Next, click Choose OS and select an operating system to install.Then plug a microSD card in using an external or built-in SD card reader. Then, click Choose storage and select your storage device.

![Local Image](/home/adit/Documents/Stockholm University/IOT/iot-ht2023-data-protocols/docs/devices/img/3.png)


Then click the settings at the right bottom and apply OS customisation. We strongly recommend configuring your Raspberry Pi via the OS customisation settings. Click the Edit Settings button to open OS customisation.

![Local Image](/home/adit/Documents/Stockholm University/IOT/iot-ht2023-data-protocols/docs/devices/img/4.png)


Next, click Write.





### Alternate way (Installing Manually)

If you face any issue installing you can try this was manunally using custom imange from your computer.
First download the  Raspberry Pi OS .img file from the [official website](https://www.raspberrypi.com/software/operating-systems/).

Then select the "Use custom" from operting system option then after selecting the custom .img file from the local computer write the image to install raspberry 



![Local Image](/home/adit/Documents/Stockholm University/IOT/iot-ht2023-data-protocols/docs/devices/img/5.png)
