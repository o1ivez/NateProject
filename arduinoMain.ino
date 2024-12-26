int i;
int j;

void setup() {
  Serial.begin(115200);               //Configure Arduino Serial and LED out
	Serial.setTimeout(1); 
	pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  while (!Serial.available()); 
    i = Serial.readString().toInt();  //Read in time data
  while (!Serial.available());
    j = Serial.readString().toInt();  //Read in temperature data
    
    digitalWrite(LED_BUILTIN, HIGH);  //Turn on LED
    delay(i*1000);                    //Keep LED on for given time
    digitalWrite(LED_BUILTIN, LOW);   //Turn off LED
}
