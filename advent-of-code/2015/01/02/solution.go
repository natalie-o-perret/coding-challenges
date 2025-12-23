package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
)

func findBasementPosition(source string) int {
	floor := 0
	for position, char := range source {
		switch char {
		case '(':
			floor++
		case ')':
			floor--
		}

		if floor == -1 {
			return position + 1 // 1-indexed
		}
	}
	return 0
}

func main() {
	// Test cases with assertions
	if findBasementPosition(")") != 1 {
		panic("Test failed: )")
	}
	if findBasementPosition("()())") != 5 {
		panic("Test failed: ()())")
	}

	// Calculate and print the answer
	_, filename, _, _ := runtime.Caller(0)
	scriptDir := filepath.Dir(filename)
	inputPath := filepath.Join(scriptDir, "..", "input.txt")
	data, _ := os.ReadFile(inputPath)
	fmt.Printf("Go: %d\n", findBasementPosition(string(data)))
}
