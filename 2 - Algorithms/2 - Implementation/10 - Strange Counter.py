t = 22#int(input())

# 1st cycle: (1, 3), (2, 2), (3, 1)
# 2nd cycle: (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9 , 1)
# 3rd cycle: (10, 12), (11, 11), (12, 10), (13, 9), (14, 8)...(21, 1)

# 3, 6, 12 => 1st cycle item value = 3 * 2 ** cycle (0-based)
# if t is within cycle starting at: 3 * 2 ** cycle


