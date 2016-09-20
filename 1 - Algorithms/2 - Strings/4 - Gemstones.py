def count_gem_elements(gems):
	gem_sets = map(set, gems)
	common_gem_elements = intersection(gem_sets)
	return len(common_gem_elements) 


N = int(input())
gems = [input() for i in range(N)]
print(count_gem_elements(gems))
