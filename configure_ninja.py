import os
from ninja_syntax import Writer


def check_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


projRoot = os.getcwd()
srcRoot = os.path.join(projRoot, "src")
buildRoot = check_dir(os.path.join(projRoot, "build"))

ASM = "nasm"
ASMFlag = ""

CC = os.path.join(projRoot, "cross_compiler", "i386elfgcc", "bin", "i386-elf-g++")
CFlag = "-ffreestanding"

linker = os.path.join(projRoot, "cross_compiler", "i386elfgcc", "bin", "i386-elf-ld")
linkFflag = "-Ttext 0x1000"


with open(os.path.join(buildRoot, "build.ninja"), "w") as buildfile:
    n = Writer(buildfile)

    def compileASM(out, inputs, asmflags):
        n.build(os.path.join(buildRoot, out),
                rule="compileASM",
                inputs=inputs,
                variables={"ASMFlag": ASMFlag + " " + asmflags})

    def compileCPP(out, inputs, cflags):
        n.build(os.path.join(buildRoot, out),
                rule="compileCPP",
                inputs=inputs,
                variables={"CFlag": CFlag + " " + cflags})

    def link(out, inputs, linkflags):
        n.build(os.path.join(buildRoot, out),
                rule="link",
                inputs=[os.path.join(buildRoot, obj) for obj in inputs],
                variables={"linkFflag": linkFflag + " " + linkflags})

    def packImage(out, inputs):
        n.build(os.path.join(buildRoot, out),
                rule="cat",
                inputs=[os.path.join(buildRoot, obj) for obj in inputs])

    n.rule("compileASM", ASM + " $in -o $out -i " + srcRoot + " $ASMFlag")
    n.rule("compileCPP", CC + " -c $in -o $out -I " + srcRoot + " $CFlag")
    n.rule("link", linker + " $in -o $out $linkFflag")
    n.rule("cat", "cat $in > $out")

    # Build use compileASM
    compileASM(out="bootsect.bin",
               inputs=[os.path.join(srcRoot, "boot", "bootsect.asm")],
               asmflags="-f bin")

    compileASM(out="kernel_entry.o",
               inputs=[os.path.join(srcRoot, "boot", "kernel_entry.asm")],
               asmflags="-f elf")

    # Build use compileCPP
    # TODO: scan folder?
    # src/drivers
    compileCPP(out="drivers.o",
               inputs=[os.path.join(srcRoot, "drivers", "ports.cpp")],
               cflags="-g")
    # src/kernel
    compileCPP(out="kernel.o",
               inputs=[os.path.join(srcRoot, "kernel", "kernel.cpp")],
               cflags="-g")
    # link kernel & driver
    link(out="kernel.bin",
         inputs=["kernel_entry.o", "kernel.o", "drivers.o"],
         linkflags="--oformat binary")

    packImage(out="os-image.bin",
              inputs=["bootsect.bin", "kernel.bin"])

    n.default(os.path.join(buildRoot, "os-image.bin"))

print("Configuring done!")
