# RoadAware-road-block-alert-system
The goal of the RoadAware  project is to develop a system that could display the real-time status of road blockages caused by water levels.
   
   A project that uses a float sensor to know the water level, ESP8266, and Arduino IDE to display the status of water in a webpage is an excellent application of the Internet of Things (IoT) technology. This project involves installing a float sensor to either side of road, which detects the water level of  the road. The float sensor is connected to an ESP8266 module, which acts as a microcontroller to receive the signal from the float sensor and transmit it to the Server using Http Protocol. The ESP8266 module uses Wi-Fi to send data to the Server.

In this project, the Arduino IDE is used to program the ESP8266 module to establish the Wi-Fi connection and send the water level data to the Server. The data is either 0 or 1 , 0 means the water not yet reached the to the level of float sensor and 1 means the water has reached the level of float sensor. This data can be retrieved from the URL of the webpage .
	  Here we have many roads, so the pincode of the road can be used to search the road on the webpage itself and the user can  observe the status of the road  Overall, this project is an excellent example of how IoT technology can be used to monitor and control various systems remotely. 
