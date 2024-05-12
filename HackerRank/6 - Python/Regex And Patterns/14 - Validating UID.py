import re

for uid in [raw_input().strip() for _ in xrange(int(raw_input()))]:
	# Perform the regex match.
	# Groups 1 and 2 ((.).*\2) match repeating characters (this test must be
	# first because any prior matching test would consume the characters).
	# Group 3 ([^\da-zA-Z]) matches non-alphanumeric characters.
	# Group 4 ([A-Z]) matches capital leters.
	# Group 5 (\d) matches digits.
	match_iter = re.finditer(r'((.).*\2)|([^\da-zA-Z])|([A-Z])|(\d)', uid)

	# Get a list of matches, including which group each match belongs to.
	# matches is a list of 5-tuples. For each 5-tuple, the only element that 
	# is not None is the one corresponding to the group that caused the match
	# (except that groups 1 and 2 (tuple indices 0 and 1) will either both be
	# None or both be non-None).
	matches = [y.groups() for y in match_iter]

	# Transform from a match-oriented list to a group-oriented list.
	# zipped_matches is a 5 element long list of tuples. Each tuple corresponds to
	# one group from the regex match. Within each tuple, any value that is not None
	# corresponds to a match.
	zipped_matches = zip(*matches)

	# Count the non-None values within each tuple.
	# result is a list of 5 integers.
	# result[0] is the number of repetitions found, and it must be 0 for a valid
	#   UID. This may not be accurate for non-zero values, but result[0] == 0 IF
	#   AND ONLY IF there are no repetitions, and that's all we care about. If this
	#   is non-zero, then result[2:] will be inaccurate, but those values won't
	#   matter in that case because we already know the UID is invalid.
	# result[1] is identical to result[0].
	# result[2] is the number of non-alphanumeric characters and must be 0.
	# result[3] is the number of capital letters and must be greater than or equal
	#   to 2.
	# result[4] is the number of digits and must be greater than or equal to 3.
	result = [reduce(lambda a, b: a + int(bool(b)), x, 0) for x in zipped_matches]

	# Test for validity
	if len(uid) == 10 and result[0] == 0 and result[2] == 0 and result[3] >= 2 and result[4] >= 3:
		print 'Valid'
	else:
		print 'Invalid'
