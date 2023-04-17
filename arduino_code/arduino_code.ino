#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>


WiFiClient wificlient;
ESP8266WiFiMulti wifiMulti;

#define f 5

HTTPClient http;    //Declare object of class HTTPClient

String  Link1, Link2, c, payload1, payload2, getData, getData2;
int httpCode1, httpCode2,a=11;
int p1;


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(f,INPUT_PULLUP);
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  wifiMulti.addAP("Redmi 5", "12345678");
  wifiMulti.addAP("Galaxy M30s404B", "shrishti");
  
  
  Serial.print("Connecting");  // Wait for connection
  while (wifiMulti.run() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  
  delay(1000); 
 
}


void loop()
{
 delay(1000);
 int var=digitalRead(f);
 if(var==HIGH)
 {
  Serial.println("road is blocked"); 
 }
 else
 {
  Serial.println("Road is clear");
 }
  
  getData= String(var);
  Serial.println(getData);
  Link2 ="http://192.168.43.181:500/add/"+getData; //http://192.168.121.6:500/add/o
  http.begin(wificlient,Link2);
   httpCode1 = http.GET();
  payload1 = http.getString();
  Serial.println(httpCode1);
  Serial.println(payload1);
  
  delay(1000);

}
