EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:PCR-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "PCR_Schematic"
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L BC413 Q1
U 1 1 58409174
P 5850 5000
F 0 "Q1" H 6050 5075 50  0000 L CNN
F 1 "BC413" H 6050 5000 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x03_Pitch2.54mm" H 6050 4925 50  0001 L CIN
F 3 "" H 5850 5000 50  0000 L CNN
	1    5850 5000
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 584091EE
P 7050 4950
F 0 "R2" V 7130 4950 50  0000 C CNN
F 1 "Nichrome Wire" V 7050 4950 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02_Pitch2.54mm" V 6980 4950 50  0001 C CNN
F 3 "" H 7050 4950 50  0000 C CNN
	1    7050 4950
	1    0    0    -1  
$EndComp
$Comp
L D D1
U 1 1 58409226
P 6750 5000
F 0 "D1" H 6750 5100 50  0000 C CNN
F 1 "D" H 6750 4900 50  0000 C CNN
F 2 "Resistors_ThroughHole:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" H 6750 5000 50  0001 C CNN
F 3 "" H 6750 5000 50  0000 C CNN
	1    6750 5000
	0    1    1    0   
$EndComp
$Comp
L R R1
U 1 1 584099E6
P 5500 5650
F 0 "R1" V 5580 5650 50  0000 C CNN
F 1 "R" V 5500 5650 50  0000 C CNN
F 2 "Resistors_ThroughHole:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 5430 5650 50  0001 C CNN
F 3 "" H 5500 5650 50  0000 C CNN
	1    5500 5650
	1    0    0    -1  
$EndComp
$Comp
L Arduino U2
U 1 1 58C090EE
P 5300 3800
F 0 "U2" H 5450 3650 60  0000 C CNN
F 1 "Arduino" H 5450 4000 60  0000 C CNN
F 2 "PCR:arduino_pin_header" H 5400 3200 60  0001 C CNN
F 3 "" H 5400 3200 60  0001 C CNN
	1    5300 3800
	1    0    0    -1  
$EndComp
$Comp
L Amplifier U3
U 1 1 58C20272
P 7450 3300
F 0 "U3" H 7350 3550 60  0001 C CNN
F 1 "Amplifier" H 7350 3700 60  0000 C CNN
F 2 "PCR:thermo_amp" H 7350 3700 60  0001 C CNN
F 3 "" H 7350 3700 60  0001 C CNN
	1    7450 3300
	1    0    0    -1  
$EndComp
$Comp
L Amplifier U4
U 1 1 58C20290
P 7950 4600
F 0 "U4" H 7850 4850 60  0001 C CNN
F 1 "Amplifier" H 7850 5000 60  0000 C CNN
F 2 "PCR:thermo_amp" H 7850 5000 60  0001 C CNN
F 3 "" H 7850 5000 60  0001 C CNN
	1    7950 4600
	1    0    0    -1  
$EndComp
$Comp
L Thermocouple TC1
U 1 1 58C1FAB1
P 8400 3125
F 0 "TC1" H 8280 3275 50  0000 C CNN
F 1 "Thermocouple" H 8200 2965 50  0000 L CNN
F 2 "" H 7825 3175 50  0001 C CNN
F 3 "" H 7825 3175 50  0001 C CNN
	1    8400 3125
	-1   0    0    -1  
$EndComp
$Comp
L Thermocouple TC2
U 1 1 58C1FAFF
P 8950 4425
F 0 "TC2" H 8830 4575 50  0000 C CNN
F 1 "Thermocouple" H 8750 4265 50  0000 L CNN
F 2 "" H 8375 4475 50  0001 C CNN
F 3 "" H 8375 4475 50  0001 C CNN
	1    8950 4425
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5950 6100 5950 5200
Wire Wire Line
	4450 6100 5950 6100
Wire Wire Line
	5250 6100 5250 5800
Connection ~ 5250 5800
Wire Wire Line
	6850 5550 6850 5550
Wire Wire Line
	6850 5150 6850 6325
Wire Wire Line
	6750 5150 7050 5150
Wire Wire Line
	7050 5150 7050 5100
Connection ~ 6850 5150
Wire Wire Line
	6750 4850 6750 4800
Wire Wire Line
	6750 4800 7050 4800
Wire Wire Line
	6900 4800 5950 4800
Connection ~ 6900 4800
Connection ~ 5950 6100
Wire Wire Line
	4850 5800 5500 5800
Wire Wire Line
	4850 3950 4850 5800
Wire Wire Line
	6100 4450 6100 4650
Wire Wire Line
	6100 4650 5650 4650
Wire Wire Line
	5650 4650 5650 5000
Wire Wire Line
	5500 5500 5500 5000
Wire Wire Line
	5500 5000 5650 5000
Wire Wire Line
	6100 3300 6400 3300
Wire Wire Line
	6400 3300 6400 3000
Wire Wire Line
	6400 3000 6800 3000
Wire Wire Line
	6100 3450 6500 3450
Wire Wire Line
	6500 3450 6500 3200
Wire Wire Line
	6500 3200 6800 3200
Wire Wire Line
	6100 3600 6650 3600
Wire Wire Line
	6650 3600 6650 3400
Wire Wire Line
	6650 3400 6800 3400
Wire Wire Line
	4850 2550 4850 3525
Wire Wire Line
	4850 2550 7200 2550
Wire Wire Line
	6100 3100 6100 2350
Wire Wire Line
	6100 2350 7800 2350
Wire Wire Line
	7425 2350 7425 2550
Wire Wire Line
	6100 4300 6700 4300
Wire Wire Line
	6700 4300 6700 4700
Wire Wire Line
	6700 4700 7300 4700
Wire Wire Line
	6100 4150 6800 4150
Wire Wire Line
	6800 4150 6800 4500
Wire Wire Line
	6800 4500 7300 4500
Wire Wire Line
	6100 4000 6900 4000
Wire Wire Line
	6900 4000 6900 4300
Wire Wire Line
	6900 4300 7300 4300
Wire Wire Line
	6850 2550 6850 3850
Wire Wire Line
	6850 3850 7700 3850
Connection ~ 6850 2550
Wire Wire Line
	7800 2350 7800 3850
Wire Wire Line
	7800 3850 7925 3850
Connection ~ 7425 2350
Wire Wire Line
	8350 4325 8850 4325
Wire Wire Line
	8850 4600 8350 4600
Wire Wire Line
	8850 4525 8850 4600
Wire Wire Line
	8300 3300 7850 3300
Wire Wire Line
	8300 3225 8300 3300
Wire Wire Line
	7850 3025 8300 3025
Wire Wire Line
	4450 6100 4450 3800
Wire Wire Line
	4450 3800 4850 3800
Connection ~ 5250 6100
Wire Wire Line
	6850 6325 4200 6325
Wire Wire Line
	4200 6325 4200 3650
Wire Wire Line
	4200 3650 4850 3650
$EndSCHEMATC
