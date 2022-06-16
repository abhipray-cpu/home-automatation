//in this sketch I will be connectin node mcu to a firebase real time database for storing and readning data
//change the frequency of your network to 2.4 ghz in order to connect node mcu
#include<FirebaseESP8266.h>
#include<ESP8266WiFi.h>
//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"
#define WIFI_SSID "Heavy Driver"
#define WIFI_PASSWORD "maakabhosda"
#define FIREBASE_AUTH "J7zZWSjFYt1VW2h3Y6SgGz8JW7okCe1qrYYEnEe0"
#define FIREBASE_HOST "channel-relay-control-3a865-default-rtdb.asia-southeast1.firebasedatabase.app/"
FirebaseData firebaseData;
FirebaseJson json;
const int relay1=14;
const int relay2=13;
const int relay3=12;
const int relay4=15;

void setup() {
  Serial.begin(115200);
   
 
  
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
   pinMode(relay1,OUTPUT);
   pinMode(relay2,OUTPUT);
   pinMode(relay3,OUTPUT);
   pinMode(relay4,OUTPUT);
   Serial.println();
   Serial.print("Connected with IP: ");
   Serial.println(WiFi.localIP());
   Serial.println();

   Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  }

void loop() {

//Serial.println("Roopa ki maa ka bhosda");
    relay1Controller();
    relay2Controller();
    relay3Controller();
    relay4Controller();
}

//since we have only 4 chaneel relay modules therfore writing four controlling functions
void relay1Controller(){
  
    if (Firebase.getString(firebaseData, "/channels/-MwXFv-SgN8ETFYTML4A/relay1")){
    Serial.print("State of relay1:");
    Serial.println(firebaseData.stringData());
    if(firebaseData.stringData() == "off")
    { 
      Serial.println("Relay1 is switched off");
      digitalWrite(relay1,HIGH);
      }
      else if(firebaseData.stringData() == "on")
      {
        Serial.println("Relay1 is switched on");
        digitalWrite(relay1,LOW);
        }
    
     }
  
  }

void relay2Controller(){
  
    if (Firebase.getString(firebaseData, "/channels/-MwXFv1emQuelnjifQtb/relay2")){
    Serial.print("State of relay2:");
    Serial.println(firebaseData.stringData());
    if(firebaseData.stringData() == "off")
    { 
      Serial.println("Relay2 is switched off");
      digitalWrite(relay2,HIGH);
      }
      else if(firebaseData.stringData() == "on")
      {
        Serial.println("Relay2 is switched on");
        digitalWrite(relay2,LOW);
        }
    
     }
  
  }
  void relay3Controller(){
  
    if (Firebase.getString(firebaseData, "/channels/-MwXFv3eKge9wUK9CDVq/relay3")){
    Serial.print("State of relay3:");
    Serial.println(firebaseData.stringData());
    if(firebaseData.stringData() == "off")
    { 
      Serial.println("Relay3 is switched off");
      digitalWrite(relay3,HIGH);
      }
      else if(firebaseData.stringData() == "on")
      {
        Serial.println("Relay3 is switched on");
        digitalWrite(relay3,LOW);
        }
    
     }
  
  }
  void relay4Controller(){
  
    if (Firebase.getString(firebaseData, "/channels/-MwXFv66FXrzlm8oncNM/relay4")){
    Serial.print("State of relay4:");
    Serial.println(firebaseData.stringData());
    if(firebaseData.stringData() == "off")
    { 
      Serial.println("Relay4 is switched off");
      digitalWrite(relay4,HIGH);
      }
      else if(firebaseData.stringData() == "on")
      {
        Serial.println("Relay4 is switched on");
        digitalWrite(relay4,LOW);
        }
    
     }
  
  }
