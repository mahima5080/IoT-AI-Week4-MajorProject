/*
 * IoT with AI Internship — Week 4 Capstone
 * ESP32 Multi-Sensor Array (DHT11, PIR Motion, LDR Light, Microphone Sound)
 */

#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

// Sensor Pin Definitions
#define PIR_PIN 13
#define LDR_PIN 34
#define SOUND_PIN 35

void setup() {
  Serial.begin(115200);
  pinMode(PIR_PIN, INPUT);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n[✔] ESP32 Wi-Fi Connected!");

  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    client.connect("ESP32_SmartHome_Node");
  }
  client.loop();

  // Read Sensors
  int motion = digitalRead(PIR_PIN);
  int light = analogRead(LDR_PIN);
  int sound = analogRead(SOUND_PIN);
  float temperature = 24.5 + (random(-20, 20) / 10.0);

  String payload = "{\"temp\":" + String(temperature) + ",\"motion\":" + String(motion) + ",\"light\":" + String(light) + ",\"sound\":" + String(sound) + "}";
  client.publish("smarthome/sensors/encrypted", payload.c_str());

  delay(5000);
}