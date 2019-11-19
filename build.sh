#!/bin/bash
set -e

SHELL_FORE_RED='\e[31m'
SHELL_FORE_GREEN='\e[32m'
SHELL_NC='\e[39m' # Default

printf "$SHELL_FORE_GREEN\nClean build folder$SHELL_NC\n"
set -x
mkdir -p build
rm -rf build/*
set +x

printf "$SHELL_FORE_GREEN\nBuild kernel$SHELL_NC\n"
ninja -v

printf "$SHELL_FORE_GREEN\nbuild done! Output files in ./build$SHELL_NC\n"
