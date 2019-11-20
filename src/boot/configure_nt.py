from ninja_tool import ninja_tool
import os

(
    # step to src/boot
    ninja_tool.step_to_dir(os.path.dirname(os.path.abspath(__file__)))
    .add_build("compile",
               out="bootsect.bin",
               rule="compileASM",
               inputs=["bootsect.asm"],
               variables={"ASMFlag": "-f bin"})
    .add_build("compile",
               out="kernel_entry.o",
               rule="compileASM",
               inputs=["kernel_entry.asm"],
               variables={"ASMFlag": "-f elf"})
)
