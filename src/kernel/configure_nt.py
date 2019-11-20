from ninja_tool import ninja_tool
import os

(
    # step to src/kernel
    ninja_tool.step_to_dir(os.path.dirname(os.path.abspath(__file__)))
    .add_build("compile",
               out="kernel.o",
               rule="compileCPP",
               inputs=["kernel.cpp"])
)
