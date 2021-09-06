#ifndef SML_INCLUDE_MAPPING_H
#define SML_INCLUDE_MAPPING_H

namespace sml_fields {

const unsigned char sml_map_energy_delivered[] = {1, 0, 1, 8, 0};
const unsigned char sml_map_energy_delivered_tariff1[] = {1, 0, 1, 8, 1};
const unsigned char sml_map_energy_delivered_tariff2[] = {1, 0, 1, 8, 2};

const unsigned char sml_map_energy_returned[] = {1, 0, 2, 8, 0};
const unsigned char sml_map_energy_returned_tariff1[] = {1, 0, 2, 8, 1};
const unsigned char sml_map_energy_returned_tariff2[] = {1, 0, 2, 8, 2};

const unsigned char sml_map_power_delivered[] = {1, 0, 16, 7, 0}; // e.g. efr SGM-C4
const unsigned char sml_map_power_delivered_2[] = {1, 0, 15, 7, 0}; // e.g. Iskra MT681

const unsigned char sml_map_voltage_l1[] = {1, 0, 32, 7, 0};
const unsigned char sml_map_voltage_l2[] = {1, 0, 52, 7, 0};
const unsigned char sml_map_voltage_l3[] = {1, 0, 72, 7, 0};

const unsigned char sml_map_current_l1[] = {1, 0, 31, 7, 0};
const unsigned char sml_map_current_l2[] = {1, 0, 51, 7, 0};
const unsigned char sml_map_current_l3[] = {1, 0, 71, 7, 0};

const unsigned char sml_map_phase_angle_u_l2_u_l1[] = {1, 0, 81, 7, 1};
const unsigned char sml_map_phase_angle_u_l3_u_l1[] = {1, 0, 81, 7, 2};

const unsigned char sml_map_phase_angle_i_l1_u_l1[] = {1, 0, 81, 7, 4};
const unsigned char sml_map_phase_angle_i_l2_u_l2[] = {1, 0, 81, 7, 15};
const unsigned char sml_map_phase_angle_i_l3_u_l3[] = {1, 0, 81, 7, 26};

const unsigned char sml_map_frequency[] = {1, 0, 14, 7, 0};
}

#endif // SML_INCLUDE_MAPPING_H
