#!/bin/bash
set -e

mkdir -p build
cd build

###############
# 1. Build boot loader
###############
echo "[Start] Build boot loader"
nasm -i ../ -f bin ../bootsect.asm -o bootsect.bin
echo "[Done] Build boot loader"

###############
# 2. Build kernel entry
###############
echo "[Start] Build kernel entry"
nasm ../kernel_entry.asm -f elf -o kernel_entry.o
echo "[Done] Build kernel entry"

###############
# 3. Build C kernel
###############
echo "[Start] Build kernel"
cmake -GNinja ..
ninja -v
# cmake --build . #-- -j4
echo "[Done] Build kernel"

###############
# 4. Cat kernel to bootsect
###############
cat bootsect.bin kernel.bin > os-image.bin