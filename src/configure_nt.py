from ninja_tool import ninja_tool

import os

(
    # step to src
    ninja_tool.step_to_dir(os.path.dirname(os.path.abspath(__file__)))
    .add_build("link",
               out="kernel.bin",
               rule="link",
               inputs=["kernel_entry.o", "kernel.o", "drivers.o"],
               variables={"linkFflag": "--oformat binary"})
)