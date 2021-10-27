import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import (
    CONF_ID,
    CONF_SENSOR,
    ICON_EMPTY,
    UNIT_WATT_HOURS,
)
from . import SML, CONF_SML_ID

AUTO_LOAD = ["sml"]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_SML_ID): cv.use_id(SML),
        cv.Optional("identification"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("p1_version"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("p1_version_be"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("timestamp"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("electricity_tariff"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("electricity_failure_log"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("message_short"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("message_long"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("gas_equipment_id"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("thermal_equipment_id"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("water_equipment_id"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
        cv.Optional("slave_equipment_id"): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
            }
        ),
    }
).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    hub = yield cg.get_variable(config[CONF_SML_ID])

    text_sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == text_sensor.TextSensor:
            var = cg.new_Pvariable(conf[CONF_ID])
            yield text_sensor.register_text_sensor(var, conf)
            cg.add(getattr(hub, f"set_{key}")(var))
            text_sensors.append(f"F({key})")

    cg.add_define(
        "SML_TEXT_SENSOR_LIST(F, sep)", cg.RawExpression(" sep ".join(text_sensors))
    )
