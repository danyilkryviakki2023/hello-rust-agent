#!/usr/bin/env bash
set -euo pipefail

cargo build --release
cargo test --release

mkdir -p dist
if [[ -f target/release/hello.exe ]]; then
    binary=target/release/hello.exe
    artifact=dist/hello.exe
else
    binary=target/release/hello
    artifact=dist/hello
fi
cp "$binary" "$artifact"

output=$("$artifact")
grep -Fq "Hello, World!" <<< "$output"
grep -Fq "2 + 3 = 5" <<< "$output"
