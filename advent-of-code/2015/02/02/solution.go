package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strconv"
	"strings"
)

func calculateRibbon(dimensions string) int {
	parts := strings.Split(dimensions, "x")
	dims := make([]int, 3)
	for i, p := range parts {
		dims[i], _ = strconv.Atoi(p)
	}
	sort.Ints(dims)

	// Smallest perimeter (using two smallest dimensions)
	perimeter := 2 * (dims[0] + dims[1])

	// Volume for bow
	volume := dims[0] * dims[1] * dims[2]

	return perimeter + volume
}

func main() {
	// Test cases with assertions
	if calculateRibbon("2x3x4") != 34 {
		panic("Test failed: 2x3x4")
	}
	if calculateRibbon("1x1x10") != 14 {
		panic("Test failed: 1x1x10")
	}

	// Read input and calculate total
	_, filename, _, _ := runtime.Caller(0)
	scriptDir := filepath.Dir(filename)
	inputPath := filepath.Join(scriptDir, "..", "input.txt")
	data, _ := os.ReadFile(inputPath)
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	total := 0
	for _, line := range lines {
		if line != "" {
			total += calculateRibbon(line)
		}
	}
	fmt.Printf("Go: %d\n", total)
}
