#!/usr/bin/python3
"""UTF-8 validation module."""

def validUTF8(data):
    """
    Determines if a given list of integers represents a valid UTF-8 encoding.
    
    Args:
        data (List[int]): A list of integers representing bytes (0 <= byte <= 255)

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for byte in data:
        # Ensure byte is a valid 8-bit value
        if type(byte) != int or byte < 0 or byte > 255:
            return False

        if num_bytes == 0:
            # Determine number of bytes in the UTF-8 character
            if byte >> 7 == 0:
                continue  # 1-byte char
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False  # Invalid leading byte
        else:
            # Check that byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

