#include "sml.h"
#include "esphome/core/log.h"
#include <sml/sml_value.h>

namespace esphome {
namespace sml_ {

static const char *TAG = "sml";

void Sml::loop() {
  this->receive_telegram();
}

void Sml::receive_telegram() {
  while (available()) {
    const char c = read();
    if (header_found_ == false){
      if (c == HEADER_PATTERN[i_header_]) {
        telegram_[i_header_] = c;
        i_header_++;
        if (i_header_ == sizeof(HEADER_PATTERN))
        {
          header_found_ = true;
          telegram_len_ = i_header_;
          i_header_ = 0;
          i_footer_ = 0;
        }
      }
      else
      {
        i_header_ = 0;
      }
      continue;
    }

    if (telegram_len_ >= MAX_TELEGRAM_LENGTH) {  // Buffer overflow
      header_found_ = false;
      i_header_ = 0;
      i_footer_ = 0;
      ESP_LOGE(TAG, "Error: Message larger than buffer");
      continue;
    }

    telegram_[telegram_len_] = c;
    telegram_len_++;

    if (c == FOOTER_PATTERN[i_footer_]) {
      i_footer_++;
      if (i_footer_ == sizeof(FOOTER_PATTERN))
      {
        header_found_ = false;
        i_header_ = 0;
        i_footer_ = 0;
        if (parse_telegram())
          return;
      }
    }
    else
      i_footer_ = 0;
  }
}

bool Sml::parse_telegram() {
  sml_file *file = sml_file_parse((unsigned char *)telegram_ + sizeof(HEADER_PATTERN), telegram_len_ - sizeof(HEADER_PATTERN) - sizeof(FOOTER_PATTERN));

  // for (int i = 0; i < file->messages_len; i++)
  // {
  //   ESP_LOGV(TAG, "SML message %4.X", *(file->messages[i]->message_body->tag));
  //   sml_message *message = file->messages[i];
  //   if (*message->message_body->tag == SML_MESSAGE_GET_LIST_RESPONSE)
  //   {
  //     sml_list *entry;
  //     sml_get_list_response *body;
  //     body = (sml_get_list_response *)message->message_body->data;
  //     for (entry = body->val_list; entry != NULL; entry = entry->next)
  //     {
  //       if (!entry->value)
  //       { // do not crash on null value
  //         ESP_LOGV(TAG, "Error in data stream. entry->value should not be NULL. Skipping this.");
  //         continue;
  //       }
  //       if (entry->value->type == SML_TYPE_OCTET_STRING)
  //       {
  //         char *str;
  //         ESP_LOGV(TAG, "SML_TYPE_OCTET_STRING:");
  //         ESP_LOGV(TAG, "%d-%d:%d.%d.%d*%d#%s#",
  //                 entry->obj_name->str[0], entry->obj_name->str[1],
  //                 entry->obj_name->str[2], entry->obj_name->str[3],
  //                 entry->obj_name->str[4], entry->obj_name->str[5],
  //                 sml_value_to_strhex(entry->value, &str, true));
  //         free(str);
  //       }
  //       else if (entry->value->type == SML_TYPE_BOOLEAN)
  //       {
  //         ESP_LOGV(TAG, "SML_TYPE_BOOLEAN");
  //         ESP_LOGV(TAG, "%d-%d:%d.%d.%d*%d#%s#",
  //                 entry->obj_name->str[0], entry->obj_name->str[1],
  //                 entry->obj_name->str[2], entry->obj_name->str[3],
  //                 entry->obj_name->str[4], entry->obj_name->str[5],
  //                 entry->value->data.boolean ? "true" : "false");
  //       }
  //       else if (((entry->value->type & SML_TYPE_FIELD) == SML_TYPE_INTEGER) ||
  //                 ((entry->value->type & SML_TYPE_FIELD) == SML_TYPE_UNSIGNED))
  //       {
  //         ESP_LOGV(TAG, "SML_TYPE_INTEGER/SML_TYPE_UNSIGNED");
  //         double value = sml_value_to_double(entry->value);
  //         int scaler = (entry->scaler) ? *entry->scaler : 0;
  //         int prec = -scaler;
  //         if (prec < 0)
  //           prec = 0;
  //         value = value * pow(10, scaler);
  //         ESP_LOGV(TAG, "%d-%d:%d.%d.%d*%d#%.*f#",
  //                 entry->obj_name->str[0], entry->obj_name->str[1],
  //                 entry->obj_name->str[2], entry->obj_name->str[3],
  //                 entry->obj_name->str[4], entry->obj_name->str[5], prec, value);
  //         const char *unit = NULL;
  //       }
  //     }
  //   }
  // }

  publish_sensors(file);

  // free the malloc'd memory
	sml_file_free(file);

  return true;
}

void Sml::dump_config() {
  ESP_LOGCONFIG(TAG, "sml:");

#define SML_LOG_SENSOR(s) LOG_SENSOR("  ", #s, this->s_##s##_);
  SML_SENSOR_LIST(SML_LOG_SENSOR, )

#define SML_LOG_TEXT_SENSOR(s) LOG_TEXT_SENSOR("  ", #s, this->s_##s##_);
  SML_TEXT_SENSOR_LIST(SML_LOG_TEXT_SENSOR, )
}

}  // namespace sml_
}  // namespace esphome
