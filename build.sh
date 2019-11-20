#!/bin/bash
set -e

python3 configure_ninja.py
ninja -C build
