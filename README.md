# pyRF95

HopeRF RF95 (and similar LoRa modules) python library

Based in RadioHead library code: http://www.airspayce.com/mikem/arduino/RadioHead/

Cloned from  https://github.com/ladecadence/pyRF95

Added Address header to David Pello's library, based from RadioHead

## Installation

Just import rf95 module in your python project

## Use

When creating the RF95 object, you need to pass the CS channel (On Raspberry Pi you have spidev 0 and 1 devices) and the external interrupt pin (Broadcom GPIO).

Then you can set channel, TX Power, and predefined modes of operation:

* Bw125Cr45Sf128 : Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on. Default medium range.
* Bw500Cr45Sf128 : Bw = 500 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on. Fast+short range.
* Bw31_25Cr48Sf512 : Bw = 31.25 kHz, Cr = 4/8, Sf = 512chips/symbol, CRC on. Slow+long range.
* Bw125Cr48Sf4096 : Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, CRC on. Slow+long range. 

You can also set custom modes using the rf95.set_modem_config_custom()and the following constants:

```
set_modem_config_custom(bandwidth, coding_rate, imp_header,
		spreading_factor, crc, continuous_tx,
		timeout, agc_auto)

Bandwidth:
rf95.BW_7K8HZ
rf95.BW_10K4HZ
rf95.BW_15K6HZ
rf95.BW_20K8HZ
rf95.BW_31K25HZ
rf95.BW_41K7HZ
rf95.BW_62K5HZ
rf95.BW_125KHZ
rf95.BW_250KHZ
rf95.BW_500KHZ

Coding Rate:
rf95.CODING_RATE_4_5
rf95.CODING_RATE_4_6
rf95.CODING_RATE_4_7
rf95.CODING_RATE_4_8

Implicit header:
rf95.IMPLICIT_HEADER_MODE_ON
rf95.IMPLICIT_HEADER_MODE_OFF

Spreading factor:
rf95.SPREADING_FACTOR_64CPS
rf95.SPREADING_FACTOR_128CPS
rf95.SPREADING_FACTOR_256CPS
rf95.SPREADING_FACTOR_512CPS
rf95.SPREADING_FACTOR_1024CPS
rf95.SPREADING_FACTOR_2048CPS
rf95.SPREADING_FACTOR_4096CPS

TX Continuous mode
rf95.TX_CONTINUOUS_MODE_ON
rf95.TX_CONTINUOUS_MODE_OFF

CRC:
rf95.RX_PAYLOAD_CRC_ON
rf95.RX_PAYLOAD_CRC_OFF

Timeout:
rf95.SYM_TIMEOUT_MSB

AGC Auto:
rf95.AGC_AUTO_ON
rf95.AGC_AUTO_OFF
```

run example.py as
python3 -Xfaulthandler example.py

