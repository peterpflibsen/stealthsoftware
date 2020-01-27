#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>

#include "bitcpy.h"

int main() {
    printf("Hello, World!\n");

    /* memory declaration */
    const size_t number_elements = 10;
    uint8_t destination[10];
    uint8_t source[10];
    memset(source, 0xFFFFFFFF, number_elements * sizeof(uint8_t));

    /* test case 1 */
    memset(destination, 0, number_elements * sizeof(uint8_t));
    bitcpy(destination, source, 5 * bits_in_byte);

    /* test case 2 */
    memset(destination, 0, number_elements * sizeof(uint8_t));
    bitcpy(destination, source, 34);

    return 0;
}
