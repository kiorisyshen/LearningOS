#!/bin/bash
set -e

rm -rf build/*
python3 configure_nt.py
ninja -C build
