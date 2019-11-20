import os
from ninja_syntax import Writer


def check_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


projRoot = os.getcwd()
srcRoot = os.path.join(projRoot, "src")
buildRoot = check_dir(os.path.join(projRoot, "build"))

CC = os.path.join(projRoot, "cross_compiler",
                  "i386elfgcc", "bin", "i386-elf-g++")
CFlag = "-ffreestanding -g"

linker = os.path.join(projRoot, "cross_compiler",
                      "i386elfgcc", "bin", "i386-elf-ld")
linkCross_flag = "-Ttext 0x1000"

with open(os.path.join(buildRoot, "build.ninja"), "w") as buildfile:
    n = Writer(buildfile)
    n.rule("compileASMbin", "nasm -i " + srcRoot + " -f bin $in -o $out")

    # Build for bootsect
    n.build(os.path.join(buildRoot, "bootsect.bin"),
            "compileASMbin", inputs=[os.path.join(srcRoot, "boot", "bootsect.asm")])

    n.default(os.path.join(buildRoot, "bootsect.bin"))
