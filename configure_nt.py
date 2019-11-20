
from ninja_tool import ninja_tool
import os

srcRoot = os.path.join(ninja_tool.projRoot, "src")

ninja_tool.ASM = "nasm"
ninja_tool.ASMFlag = ""

ninja_tool.CC = os.path.join(ninja_tool.projRoot, "cross_compiler", "i386elfgcc", "bin", "i386-elf-g++")
ninja_tool.CFlag = "-ffreestanding -g"

ninja_tool.linker = os.path.join(ninja_tool.projRoot, "cross_compiler", "i386elfgcc", "bin", "i386-elf-ld")
ninja_tool.linkFflag = "-Ttext 0x1000"

(
    ninja_tool
    .add_rule("compileASM",
              ninja_tool.ASM + " $in -o $out -i " + srcRoot + " " + ninja_tool.ASMFlag + " $ASMFlag")
    .add_rule("compileCPP",
              ninja_tool.CC + " -c $in -o $out -I " + srcRoot + " " + ninja_tool.CFlag + " $CFlag")
    .add_rule("link",
              ninja_tool.linker + " $in -o $out " + ninja_tool.linkFflag + " $linkFflag")
    .add_rule("cat",
              "cat $in > $out")
)

import src.boot.configure_nt
import src.drivers.configure_nt
import src.kernel.configure_nt
import src.configure_nt

(
    # step to .
    ninja_tool.step_to_dir(os.path.dirname(os.path.abspath(__file__)))
    .add_build("link",
               out="os-image.bin",
               rule="cat",
               inputs=["bootsect.bin", "kernel.bin"])
    .add_default("os-image.bin")
)
