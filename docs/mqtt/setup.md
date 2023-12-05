# iot-ht2023-data-protocols-mqtt-setup-guide
## MQTT setup guide for local environment (MacOS, Windows, Linux) - those who watns more info [Official Documentation] (https://mosquitto.org/download/).
### **MacOS setup guide**
#### Install Homebrew:
##### If you don't have Homebrew installed, you can install it by running the following command in your terminal: 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
#### **Install Mosquitto:**
##### Once Homebrew is installed, you can use it to install Mosquitto:
```
brew install mosquitto
```
#### **Start Mosquitto:**
##### After the installation is complete, you can start the Mosquitto broker using: 
```
mosquitto
```
##### **If you want Mosquitto to start automatically on system startup, you can use Homebrew services:**
```
brew services start mosquitto
```
##### **If you want Mosquitto to stop, you can use Homebrew services:**
```
brew services stop mosquitto
```

##### **If you want Mosquitto to restart, you can use Homebrew services:**
```
brew services restart mosquitto
```

## For better working environment/understanding you can install the desktop UI for your local machine (MacOS, Windows, Linux) - Those who wants more info [Official Documentation](https://mqttx.app/)
### For MacOS - installation guide for MQTTX in your local machine
#### **Download MQTTX:**
##### Visit the official GitHub repository for MQTTX: MQTTX GitHub Releases.

#### **Download the Latest Release:**
##### Find the latest release on the GitHub page and download the appropriate macOS version. The file should have a .dmg extension.

##### **Install MQTTX:**
##### Open the downloaded .dmg file. You should see the MQTTX application. Drag the MQTTX icon to the "Applications" folder to install it.

#### **Open MQTTX:**
##### Navigate to your "Applications" folder and find MQTTX. Double-click to open the application.

#### **Allow Unidentified Developer:**
##### If you encounter a security prompt stating that the app is from an unidentified developer, you may need to allow it. Go to "System Preferences" > "Security & Privacy" > "General" and click the "Open Anyway" button.

#### **Start Using MQTTX:**
##### Once installed, open MQTTX, and you can start using it to interact with MQTT brokers and topics.

## **Logging the configuration in a file for better debugging or understanding in MacOS:**
### **Open the Mosquitto Configuration File:**
#### Use a text editor to open the Mosquitto configuration file. The default path is /opt/homebrew/etc/mosquitto/mosquitto.conf. You can use the nano text editor in the terminal or modification:
```
nano /opt/homebrew/etc/mosquitto/mosquitto.conf

```
### **Configure Logging:**
#### Add or modify the following lines in the configuration file to configure logging. You can customize the paths and settings according to your requirements. Navigate to the line in the configuration file where **log_type** is defined and add or modify with your requirements.
```
# add those lines to the log_type
log_type all
log_type debug
log_dest file /path/to/your/mosquitto.log

```
### **Correct the log_type Value:**
#### Ensure that the log_type value is valid. The **log_type** can be one of the following: `all`, `debug`, `error`, `information`, `notice`, `warning`, or `none`.

#### Ensure that the directory specified for the log file has appropriate write permissions.
### **Save and Restart Mosquitto:**
#### Save the changes to the configuration file and restart the Mosquitto broker to apply the new logging settings:
```
brew services restart mosquitto
```
#### If you're not using Homebrew services, you can stop and start Mosquitto manually:
```
brew services stop mosquitto
brew services start mosquitto

```
#### Now, Mosquitto should log messages to the specified file as per your configuration. Adjust the paths and settings based on your preferences and system configuration.

### **Create a configuration file that defines a listener to allow remote access for mosquitto in macos:**
#### **Open the configuration file by useing the below command:**
```
nano /opt/homebrew/etc/mosquitto/mosquitto.conf

```
#### **Add Listener Configuration:**
##### Add the following lines to the configuration file to define a listener. Adjust the settings according to your preferences:
```
`**Allow anonymous connections**`
allow_anonymous true

`**Listener for remote access**`
listener 1883 <your ip address>

```
### **Restart Mosquitto:**
#### After making changes to the mosquitto.conf file, restart the Mosquitto service to apply the changes:
```
brew services restart mosquitto

```
