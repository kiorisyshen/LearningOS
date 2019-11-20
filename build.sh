#!/bin/bash
set -e

rm -rf build
python3 configure.py
ninja -C build
