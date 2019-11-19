ninja debug -v
qemu-system-i386 -s -S -fda build/os-image.bin & cross_compiler/i386elfgcc/bin/i386-elf-gdb -ex "target remote localhost:1234" -ex "symbol-file build/kernel.elf"