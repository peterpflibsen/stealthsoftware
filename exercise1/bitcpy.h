#pragma once

#include <string.h>

/* globals */
extern const size_t bits_in_byte;

/* functions */
void* bitcpy(void* destination, const void* source, const size_t num_bits);
