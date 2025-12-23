package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
)

func calculateWrappingPaper(dimensions string) int {
	parts := strings.Split(dimensions, "x")
	l, _ := strconv.Atoi(parts[0])
	w, _ := strconv.Atoi(parts[1])
	h, _ := strconv.Atoi(parts[2])

	// Calculate surface area
	surfaceArea := 2*l*w + 2*w*h + 2*h*l

	// Find smallest side
	sides := []int{l * w, w * h, h * l}
	slack := sides[0]
	for _, side := range sides {
		if side < slack {
			slack = side
		}
	}

	return surfaceArea + slack
}

func main() {
	// Test cases with assertions
	if calculateWrappingPaper("2x3x4") != 58 {
		panic("Test failed: 2x3x4")
	}
	if calculateWrappingPaper("1x1x10") != 43 {
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
			total += calculateWrappingPaper(line)
		}
	}
	fmt.Printf("Go: %d\n", total)
}
