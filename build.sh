#!/bin/bash
set -e

SHELL_FORE_RED='\e[31m'
SHELL_FORE_GREEN='\e[32m'
SHELL_NC='\e[39m' # Default

mkdir -p build
rm -rf build/*
pushd build

###############
# 1. Build boot loader
###############
printf "$SHELL_FORE_GREEN\nBuilding boot loader$SHELL_NC\n"
set -x
nasm -i ../ -f bin ../bootsect.asm -o bootsect.bin
set +x

###############
# 2. Build kernel entry
###############
printf "$SHELL_FORE_GREEN\nBuild kernel entry$SHELL_NC\n"
set -x
nasm ../kernel_entry.asm -f elf -o kernel_entry.o
set +x

popd

###############
# 3. Build C kernel
###############
printf "$SHELL_FORE_GREEN\nBuild kernel$SHELL_NC\n"
ninja -v


###############
# 4. Cat kernel to bootsect
###############
printf "$SHELL_FORE_GREEN\nGenerat os-image.bin$SHELL_NC\n"
pushd build
set -x
cat bootsect.bin kernel.bin > os-image.bin
set +x
popd

printf "$SHELL_FORE_GREEN\nbuild done! Output files in ./build$SHELL_NC\n"
