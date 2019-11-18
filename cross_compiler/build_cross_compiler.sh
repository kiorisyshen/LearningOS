#!/bin/bash
set -e

############################
# First, install dependencies using brew, as written in:
# https://github.com/cfenollosa/os-tutorial/tree/master/11-kernel-crosscompiler#required-packages
############################


############################
# Second, Set environment variables
# Note: you may want to replace your gcc version
############################
export CC=/usr/local/bin/gcc-9
export LD=/usr/local/bin/gcc-9

mkdir -p i386elfgcc
export PREFIX="$(pwd)/i386elfgcc"
export TARGET=i386-elf
export PATH="$PREFIX/bin:$PATH"


############################
# Third, build binutils
############################
mkdir -p $(pwd)/tmp/src
pushd $(pwd)/tmp/src

curl -O http://ftp.gnu.org/gnu/binutils/binutils-2.33.1.tar.gz # If the link 404's, look for a more recent version
tar xf binutils-2.33.1.tar.gz
mkdir binutils-build
cd binutils-build
../binutils-2.33.1/configure --target=$TARGET --enable-interwork --enable-multilib --disable-nls --disable-werror --prefix=$PREFIX 2>&1 | tee configure.log
make all install 2>&1 | tee make.log

popd

############################
# Final, build gcc
############################
mkdir -p $(pwd)/tmp/src
pushd $(pwd)/tmp/src

curl -O https://ftp.gnu.org/gnu/gcc/gcc-9.2.0/gcc-9.2.0.tar.gz
tar xf gcc-9.2.0.tar.gz
mkdir gcc-build
cd gcc-build
../gcc-9.2.0/configure --target=$TARGET --prefix="$PREFIX" --disable-nls --disable-libssp --enable-languages=c --without-headers
make all-gcc 
make all-target-libgcc 
make install-gcc 
make install-target-libgcc 

popd