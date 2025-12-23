package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
)

func calculateFloor(source string) int {
	floor := 0
	for _, char := range source {
		switch char {
		case '(':
			floor++
		case ')':
			floor--
		}
	}
	return floor
}

func main() {
	// Test cases with assertions
	if calculateFloor("(())") != 0 {
		panic("Test failed: (())")
	}
	if calculateFloor("()()") != 0 {
		panic("Test failed: ()()")
	}
	if calculateFloor("(((") != 3 {
		panic("Test failed: (((")
	}
	if calculateFloor("(()(()(") != 3 {
		panic("Test failed: (()(()(")
	}
	if calculateFloor("))(((((") != 3 {
		panic("Test failed: ))(((((")
	}
	if calculateFloor("())") != -1 {
		panic("Test failed: ())")
	}
	if calculateFloor("))(") != -1 {
		panic("Test failed: ))(")
	}
	if calculateFloor(")))") != -3 {
		panic("Test failed: )))")
	}
	if calculateFloor(")())())") != -3 {
		panic("Test failed: )())())")
	}

	// Calculate and print the answer
	_, filename, _, _ := runtime.Caller(0)
	scriptDir := filepath.Dir(filename)
	inputPath := filepath.Join(scriptDir, "..", "input.txt")
	input, _ := os.ReadFile(inputPath)
	fmt.Printf("Go: %d\n", calculateFloor(string(input)))
}
