    var token = init_token();

                    // float 32 -- 0xca
                    // float 64 -- 0xcb
                    token[0xca] = writeN(0xca, 4, writeFloatBE);
                    token[0xcb] = writeN(0xcb, 8, writeDoubleBE);

                    return token;
                }

                // Node.js and browsers with TypedArray

                function init_token() {
                    // (immediate values)
                    // positive fixint -- 0x00 - 0x7f
                    // nil -- 0xc0
                    // false -- 0xc2
                    // true -- 0xc3
                    // negative fixint -- 0xe0 - 0xff
                    var token = uint8.slice();

                    // bin 8 -- 0xc4
                    // bin 16 -- 0xc5
                    // bin 32 -- 0xc6
                    token[0xc4] = write1(0xc4);
                    token[0xc5] = write2(0xc5);
