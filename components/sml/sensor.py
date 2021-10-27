import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    ICON_EMPTY,
    LAST_RESET_TYPE_NEVER,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_NONE,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_DEGREES,
    UNIT_HERTZ,
    UNIT_VOLT,
    UNIT_WATT,
)
from . import SML, CONF_SML_ID

AUTO_LOAD = ["sml"]


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_SML_ID): cv.use_id(SML),
        cv.Optional("energy_delivered"): sensor.sensor_schema(
            "kWh",
            ICON_EMPTY,
            3,
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            LAST_RESET_TYPE_NEVER,
        ),
        cv.Optional("energy_delivered_tariff1"): sensor.sensor_schema(
            "kWh",
            ICON_EMPTY,
            3,
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            LAST_RESET_TYPE_NEVER
        ),
        cv.Optional("energy_delivered_tariff2"): sensor.sensor_schema(
            "kWh",
            ICON_EMPTY,
            3,
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            LAST_RESET_TYPE_NEVER,
        ),
        cv.Optional("energy_returned"): sensor.sensor_schema(
            "kWh",
            ICON_EMPTY,
            3,
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            LAST_RESET_TYPE_NEVER,
        ),
        cv.Optional("energy_returned_tariff1"): sensor.sensor_schema(
            "kWh",
            ICON_EMPTY,
            3,
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            LAST_RESET_TYPE_NEVER,
        ),
        cv.Optional("energy_returned_tariff2"): sensor.sensor_schema(
            "kWh",
            ICON_EMPTY,
            3,
            DEVICE_CLASS_ENERGY,
            STATE_CLASS_TOTAL_INCREASING,
            LAST_RESET_TYPE_NEVER,
        ),
        cv.Optional("power_delivered"): sensor.sensor_schema(
            UNIT_WATT, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("power_delivered_2"): sensor.sensor_schema(
            UNIT_WATT, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("current_l1"): sensor.sensor_schema(
            UNIT_AMPERE, ICON_EMPTY, 1, DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("current_l2"): sensor.sensor_schema(
            UNIT_AMPERE, ICON_EMPTY, 1, DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("current_l3"): sensor.sensor_schema(
            UNIT_AMPERE, ICON_EMPTY, 1, DEVICE_CLASS_CURRENT, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("voltage_l1"): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 1, DEVICE_CLASS_VOLTAGE, STATE_CLASS_NONE
        ),
        cv.Optional("voltage_l2"): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 1, DEVICE_CLASS_VOLTAGE, STATE_CLASS_NONE
        ),
        cv.Optional("voltage_l3"): sensor.sensor_schema(
            UNIT_VOLT, ICON_EMPTY, 1, DEVICE_CLASS_VOLTAGE, STATE_CLASS_NONE
        ),
        cv.Optional("phase_angle_u_l2_u_l1"): sensor.sensor_schema(
            UNIT_DEGREES, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("phase_angle_u_l3_u_l1"): sensor.sensor_schema(
            UNIT_DEGREES, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("phase_angle_i_l1_u_l1"): sensor.sensor_schema(
            UNIT_DEGREES, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("phase_angle_i_l2_u_l2"): sensor.sensor_schema(
            UNIT_DEGREES, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("phase_angle_i_l3_u_l3"): sensor.sensor_schema(
            UNIT_DEGREES, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
        cv.Optional("frequency"): sensor.sensor_schema(
            UNIT_HERTZ, ICON_EMPTY, 3, DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT
        ),
    }
).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    hub = yield cg.get_variable(config[CONF_SML_ID])

    sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == sensor.Sensor:
            s = yield sensor.new_sensor(conf)
            cg.add(getattr(hub, f"set_{key}")(s))
            sensors.append(f"F({key})")

    cg.add_define("SML_SENSOR_LIST(F, sep)", cg.RawExpression(" sep ".join(sensors)))
