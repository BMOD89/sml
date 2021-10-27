import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import (
    CONF_ID,
    CONF_UART_ID,
)

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "text_sensor"]

CONF_SML_ID = "sml_id"

sml_ns = cg.esphome_ns.namespace("sml_")
SML = sml_ns.class_("Sml", cg.Component, uart.UARTDevice)


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(SML),
    }
).extend(uart.UART_DEVICE_SCHEMA)


def to_code(config):
    uart_component = yield cg.get_variable(config[CONF_UART_ID])
    var = cg.new_Pvariable(config[CONF_ID], uart_component)
    yield cg.register_component(var, config)

    # https://github.com/volkszaehler/libsml/blob/master/library.json
    cg.add_library("libsml", None, "https://github.com/volkszaehler/libsml")
