#!/bin/bash

# Common script to run all language solutions
# Usage: source this script and call run_all_solutions "Title"

run_all_solutions() {
    local title="$1"
    
    echo "=== $title ==="
    cd "$(dirname "${BASH_SOURCE[1]}")"
    
    dotnet fsi solution.fsx
    
    if command -v dotnet-script &> /dev/null; then
        dotnet-script solution.cs
    else
        echo "C#: (dotnet-script not installed, skipping)"
    fi
    
    python3 solution.py
    clojure -M solution.clj
    
    if [ -f "Cargo.toml" ]; then
        cargo run --release --quiet
    else
        rustc solution.rs -o rust_solution && ./rust_solution && rm rust_solution
    fi
    
    if command -v zig &> /dev/null; then
        zig build-exe solution.zig -O ReleaseFast && ./solution && rm solution solution.o 2>/dev/null || true
    fi
    
    go run solution.go
}
