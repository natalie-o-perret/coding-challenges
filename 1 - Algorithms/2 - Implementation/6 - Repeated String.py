s = input()
n = int(input())
segment_length = len(s)
segment_count = s.count("a")
ratio = n // segment_length
remainder = segment_length - n % segment_length
first_segments_count = ratio * segment_count
last_partial_segment_count = s.count("a", 0, segment_length - remainder)
result = first_segments_count + last_partial_segment_count
print(result)
