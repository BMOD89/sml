# custom component for SML energy meter

External repository for [ESPHome](https://esphome.io/) to support SML energy meter.


## 1. Usage

Use latest [ESPHome](https://esphome.io/) (at least v1.18.0)
with external components and add this to your `.yaml` definition:

```yaml
external_components:
  - source: github://BMOD89/sml
```

## 2. Example Configuration

with two energy meters connected to one esp8266

```yaml
uart:
   - id: uart_haus
     baud_rate: 9600
     rx_pin: D2
     tx_pin: D6
   - id: uart_heizung
     baud_rate: 9600
     rx_pin: D1
     tx_pin: D5

sml:
  - id: sml_id_haus
    uart_id: uart_haus
  - id: sml_id_heizung
    uart_id: uart_heizung
    
sensor:
  - platform: sml
    sml_id: sml_id_haus
    energy_delivered:
      name: "Haus-Wirkenergie"
      accuracy_decimals: 2
      filters:
        - multiply: 0.0001
    power_delivered:
      name: "Haus-Wirkleistung"
  - platform: sml
    sml_id: sml_id_heizung
    energy_delivered:
      name: "Heizung-Wirkenergie"
      accuracy_decimals: 2
      filters:
        - multiply: 0.0001
    power_delivered:
      name: "Heizung-Wirkleistung"
```
