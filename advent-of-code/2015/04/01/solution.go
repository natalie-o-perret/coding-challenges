package main

import (
	"crypto/md5"
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func findAdventCoin(secretKey string) int {
	number := 1
	for {
		text := fmt.Sprintf("%s%d", secretKey, number)
		hash := md5.Sum([]byte(text))
		// Check if first 2.5 bytes are zero (5 hex digits)
		if hash[0] == 0 && hash[1] == 0 && (hash[2]&0xF0) == 0 {
			return number
		}
		number++
	}
}

func main() {
	// Test cases with assertions
	if findAdventCoin("abcdef") != 609043 {
		panic("Test failed: findAdventCoin(\"abcdef\") != 609043")
	}
	if findAdventCoin("pqrstuv") != 1048970 {
		panic("Test failed: findAdventCoin(\"pqrstuv\") != 1048970")
	}

	// Read input and calculate result
	_, filename, _, _ := runtime.Caller(0)
	dir := filepath.Dir(filename)
	inputPath := filepath.Join(dir, "..", "input.txt")
	content, err := os.ReadFile(inputPath)
	if err != nil {
		panic(err)
	}
	secretKey := strings.TrimSpace(string(content))

	result := findAdventCoin(secretKey)
	fmt.Printf("Go: %d\n", result)
}
