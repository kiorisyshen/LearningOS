#!/bin/bash
set -e

SHELL_FORE_RED='\e[31m'
SHELL_FORE_GREEN='\e[32m'
SHELL_NC='\e[39m' # Default

############################
# First, install dependencies using brew, as written in:
# https://github.com/cfenollosa/os-tutorial/tree/master/11-kernel-crosscompiler#required-packages
############################


############################
# Second, Set variables
# Note: you may want to replace your gcc version
############################
export CC=/usr/local/bin/gcc-9
export LD=/usr/local/bin/gcc-9

mkdir -p i386elfgcc
export PREFIX="$(pwd)/i386elfgcc"
export TARGET=i386-elf
export PATH="$PREFIX/bin:$PATH"

# control binutil and gcc version here
BINUTIL=binutils-2.33.1
GCCNAME=gcc-9.2.0

############################
# Third, build binutils
############################
mkdir -p $(pwd)/tmp/src
pushd $(pwd)/tmp/src

if ! [ -f $BINUTIL.tar.gz ]; then
    printf "$SHELL_FORE_GREEN\nDownloading $BINUTIL $SHELL_NC\n"
    curl -O http://ftp.gnu.org/gnu/binutils/$BINUTIL.tar.gz # If the link 404's, look for a more recent version
fi

printf "$SHELL_FORE_GREEN\nExtracting $BINUTIL $SHELL_NC\n"
tar xf $BINUTIL.tar.gz

mkdir -p binutils-build
cd binutils-build
printf "$SHELL_FORE_GREEN\nBuilding $BINUTIL $SHELL_NC\n"
../$BINUTIL/configure --target=$TARGET --enable-interwork --enable-multilib --disable-nls --disable-werror --prefix=$PREFIX 2>&1 | tee configure.log
make all install 2>&1 | tee make.log

popd

############################
# Final, build gcc
############################
mkdir -p $(pwd)/tmp/src
pushd $(pwd)/tmp/src

if ! [ -f $BINUTIL.tar.gz ]; then
    printf "$SHELL_FORE_GREEN\nDownloading $BINUTIL $SHELL_NC\n"
    curl -O https://ftp.gnu.org/gnu/gcc/$GCCNAME/$GCCNAME.tar.gz
fi

printf "$SHELL_FORE_GREEN\nExtracting $GCCNAME $SHELL_NC\n"
tar xf gcc-9.2.0.tar.gz
mkdir -p gcc-build
cd gcc-build
printf "$SHELL_FORE_GREEN\nConfiguring $GCCNAME $SHELL_NC\n"
../$GCCNAME/configure --target=$TARGET --prefix="$PREFIX" --disable-nls --disable-libssp --enable-languages=c++ --without-headers --with-gmp=/usr/local --with-mpfr=/usr/local --with-mpc=/usr/local

printf "$SHELL_FORE_GREEN\nBuilding $GCCNAME $SHELL_NC\n"
make all-gcc -j4
make all-target-libgcc -j4
make install-gcc
make install-target-libgcc

popd

printf "$SHELL_FORE_GREEN\ncross compiler build done! $SHELL_NC\n"
