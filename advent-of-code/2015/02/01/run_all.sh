#!/bin/bash

# Script to run all language solutions for Part 1

echo "=== Advent of Code 2015 - Day 2: I Was Told There Would Be No Math, Part 1 ==="
cd "$(dirname "$0")"
dotnet fsi solution.fsx
if command -v dotnet-script &> /dev/null; then
    dotnet-script solution.cs
else
    echo "C#: (dotnet-script not installed, skipping)"
fi
python3 solution.py
clojure -M solution.clj
rustc solution.rs -o rust_solution && ./rust_solution && rm rust_solution
zig run solution.zig && rm -rf zig-out
go run solution.go
