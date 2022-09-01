def rol8(value, shift):
    return 0xff & (value << (shift % 8) | value >> 8 - (shift % 8))
def ror8(value, shift):
    return 0xff & (value >> (shift % 8) | value << 8 - (shift % 8))

enc_flag = [86, 27, 99, 246, 233, 136, 36, 51, 216, 27, 3, 243, 34, 236, 182, 105, 135, 89, 70, 211, 68, 53, 150, 88, 178, 25, 17, 179, 7, 229, 71, 104, 222, 155, 167, 34, 5, 229, 58, 104, 3, 155, 34, 179, 40, 185, 70, 61, 68, 80, 115, 70, 34, 236, 198, 61, 68, 208, 34, 179, 54, 133, 182, 101, 158, 136, 54, 22, 173, 149, 34, 59, 134, 89, 147, 86, 167, 136, 132, 101, 228, 89, 34, 179, 11, 244, 17, 123, 34, 206, 19, 211, 68, 245, 68, 59, 87, 155, 35, 86, 39, 244, 34, 95, 68, 206, 102, 214, 71, 244, 17, 83, 228, 213, 233, 34, 103, 134]
flag = [0 for i in range(len(enc_flag))]
# flag = '''
# hello=\"%s\";
# mixed=\"%s\";
# python=\"%s\";
# And=\"%s\";
# c=\"%s\";
# came=\"%s\";
# here=\"%s\";
# a=\"%s\";
# b=\"%s\";
# under=\"%s\";
# fmt=\"%s\";'
# '''


# v6 = 0
# while len(flag) - 1 > v6:
flag[0] = ord('h')
for v6 in range(len(enc_flag) - 2):
    if v6 % 2 == 0:
        flag[v6 + 1] = rol8(enc_flag[v6], 4)
    elif v6 % 3 == 0:
        flag[v6 + 1] = rol8(enc_flag[v6], v6 + 1)
    elif v6 % 4 == 0:
        flag[v6 + 1] = ror8(enc_flag[v6], v6 + 1)
    elif v6 % 5 == 0:
        flag[v6 + 1] = rol8(enc_flag[v6], v6 + 1)
    elif v6 % 6 == 0:
        flag[v6 + 1] = rol8(enc_flag[v6], v6 + 1)
    elif v6 % 7 == 0:
        flag[v6 + 1] = rol8(enc_flag[v6], v6 + 1)
    elif v6 % 8 == 0:
        flag[v6 + 1] = ror8(enc_flag[v6], v6 + 1)
    elif v6 % 9 == 0:
        flag[v6 + 1] = rol8(enc_flag[v6], v6 + 1)
    else:
        flag[v6 + 1] = rol8(enc_flag[v6], v6 + 1)
    # v6 += 1

print ''.join([chr(flag[i]) for i in range(len(flag))])