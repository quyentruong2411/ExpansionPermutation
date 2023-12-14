def expansion_permutation(key: str) -> str:
    # Convert key sang nhị phân
    key = bin(int(key, 16))[2:].zfill(64)

    # Áp dụng expansion permutation
    expansion_table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]
    
    expanded_key = ''.join([key[i - 1] for i in expansion_table])

    # Chia nhỏ key
    keys = [expanded_key[i:i + 48] for i in range(0, 768, 48)]

    return keys
