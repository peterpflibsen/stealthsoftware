#include <string.h>
#include <stdint.h>

/* globals */
const size_t bits_in_byte = 8;


/* functions */
uint8_t bitmask_from_count(const uint8_t count) {
    uint8_t result = 0;

    for(uint8_t it = 0; it < count; it++) {
        result |= (1 << it);
    }

    return result;
}

void* bitcpy(void* destination, const void* source, const size_t num_bits) {
    const size_t num_bytes = num_bits / bits_in_byte;
    const size_t remaining_bits = num_bits % bits_in_byte;

    if(num_bytes > 0) {
        memcpy(destination, source, num_bytes);
    }

    if(remaining_bits > 0) {
        /* calculate pointer positions */
        uint8_t* const cast_start_destination = (uint8_t*) destination;
        const uint8_t* const cast_start_source = (uint8_t*) source;
        uint8_t* const cast_bits_destination = &cast_start_destination[num_bytes];
        const uint8_t* const cast_bits_source = &cast_start_source[num_bytes];

        const uint8_t keep_bits_mask = bitmask_from_count(remaining_bits);

        /* do assignment of masked bits
         * and update destination */
        const uint8_t source_bits_to_copy = (*cast_bits_source) & keep_bits_mask;
        (*cast_bits_destination) |= source_bits_to_copy;
    }

    /* same behavior as memcpy */
    return destination;
}