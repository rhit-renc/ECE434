////////////////////////////////////////
//	blinkLED.c
//	Blinks the USR3 LED.
//	Wiring:	None
//	Setup:
//	See:
////////////////////////////////////////
//	Tested: rcn-ee: 2021.12.15 - BBGG - 5.15.6-bone14

#include <stdio.h>
#include <unistd.h>

int main() {
	// FILE * trigger = fopen("/sys/class/leds/beaglebone:green:usr3/trigger", "w");
	FILE * trigger = fopen("/sys/class/gpio/gpio50/direction", "w");
	// FILE * brightness = fopen("/sys/class/leds/beaglebone:green:usr3/brightness", "w");
	FILE * brightness = fopen("/sys/class/gpio/gpio50/value", "w");
	int on = 0;
	
	// fprintf(trigger, "none\n");
	fprintf(trigger, "out\n");

	while(1) {
		fprintf(brightness, "%d\n", on);
		fflush(brightness);
		if(!on) 
			on = 1;
		else 
			on = 0;
		// usleep(500000);
		usleep(1);
	}
}
