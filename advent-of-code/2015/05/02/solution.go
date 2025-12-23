package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func isNice(s string) bool {
	// Check for a pair that appears at least twice without overlapping
	hasPair := false
	for i := 0; i < len(s)-1; i++ {
		pair := s[i : i+2]
		// Look for the same pair starting at least 2 positions later
		if strings.Contains(s[i+2:], pair) {
			hasPair = true
			break
		}
	}
	if !hasPair {
		return false
	}

	// Check for a letter that repeats with exactly one letter between
	hasRepeat := false
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+2] {
			hasRepeat = true
			break
		}
	}

	return hasRepeat
}

func main() {
	// Test cases with assertions
	if !isNice("qjhvhtzxzqqjkmpb") {
		panic("Test failed: isNice(\"qjhvhtzxzqqjkmpb\") != true")
	}
	if !isNice("xxyxx") {
		panic("Test failed: isNice(\"xxyxx\") != true")
	}
	if isNice("uurcxstgmygtbstg") {
		panic("Test failed: isNice(\"uurcxstgmygtbstg\") != false")
	}
	if isNice("ieodomkazucvgmuy") {
		panic("Test failed: isNice(\"ieodomkazucvgmuy\") != false")
	}

	// Read input and calculate result
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	inputPath := filepath.Join(dir, "..", "input.txt")
	content, err := os.ReadFile(inputPath)
	if err != nil {
		panic(err)
	}
	strings_list := strings.Split(strings.TrimSpace(string(content)), "\n")

	count := 0
	for _, s := range strings_list {
		if isNice(s) {
			count++
		}
	}

	fmt.Printf("Go: %d\n", count)
}
