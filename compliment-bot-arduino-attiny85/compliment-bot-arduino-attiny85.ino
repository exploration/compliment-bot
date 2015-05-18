/*
Author: Donald L. Merand for Explo ( http://explo.org )
Description: This is the lights (and whatever else) for 
 the compliment bot project
 */

byte outputEnablePin = 0;   // PWM - brightness control
byte dataPin = 1;           // digital - shift register data
byte latchPin = 2;          // shift register latch
byte clockPin = 3;          // shift register clock
byte raspberryPiPin = 4;    // read info from Pi

byte leds = 0;              // 8 bits - one for each LED ;)

void setup() 
{
  pinMode(outputEnablePin, OUTPUT); 
  pinMode(dataPin, OUTPUT);  
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(raspberryPiPin, INPUT);
}

// really simple. the raspberry pi sets its output pin to 
// HIGH if it wants the animation to run. then the animation
// runs. then the leds are turned off.
void loop() 
{
  if (digitalRead(raspberryPiPin) == HIGH) {
    fadeLoop(1);
    nightRider(4);
    fadeLoop(1);
  } 
  else {
    clearLeds();
  }
}

void updateShiftRegister() {
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, leds);
  digitalWrite(latchPin, HIGH);
}

void clearLeds() {
  leds = 0;
  updateShiftRegister();
}

// brightness is 0-255
void setBrightness(byte brightness) {
  analogWrite(outputEnablePin, 255-brightness);
}

// do the nightrider thing
void nightRider(int numReps) {
  int loopSpeed = 75;

  setBrightness(255);
  clearLeds();

  for (int i = 0 ; i < numReps ; i++) {
    // nightrider up
    for (int i = 0; i < 8; i++) {
      bitClear(leds, i-1);
      bitSet(leds, i);
      bitSet(leds, i+1);
      bitSet(leds, i+2);
      updateShiftRegister();
      delay(loopSpeed);
    }
    // nightrider down
    for (int i = 7; i >= 0; i--) {
      bitClear(leds, i+1);
      bitSet(leds, i);
      bitSet(leds, i-1);
      bitSet(leds, i-2);
      updateShiftRegister();
      delay(loopSpeed);
    }
  }
}

void fadeLoop(byte numReps) {
  byte maxBrightness = 64;
  byte fadeSpeed = 10;

  leds = B11111111;
  updateShiftRegister();

  for (byte i = 0 ; i < numReps ; i++) {  
    // bring up the lights
    for (byte b = 0; b < maxBrightness; b++) {
      setBrightness(b);
      delay(fadeSpeed);
    }
    // bring down the lights
    for (byte b = maxBrightness; b > 0; b--) {
      setBrightness(b);
      delay(fadeSpeed);
    }
  }
}
