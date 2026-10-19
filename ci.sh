#!/usr/bin/env bash
<<<<<<< HEAD
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
=======
# Складання, тестування та пакування для Linux/macOS (і Git Bash на Windows).
set -euo pipefail
cd "$(dirname "$0")"

echo "==> cargo build --release"
cargo build --release

echo "==> cargo test --release"
cargo test --release

echo "==> packaging into dist/"
mkdir -p dist
BIN=hello
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) BIN=hello.exe ;;
esac
cp "target/release/$BIN" "dist/$BIN"

echo "==> running dist/$BIN"
OUT="$("./dist/$BIN")"
echo "$OUT"
echo "$OUT" | grep -q "Hello, World!"

echo "CI OK"
>>>>>>> origin/develop
