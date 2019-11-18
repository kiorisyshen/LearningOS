cmake_minimum_required (VERSION 2.6)
project (test)

set(CMAKE_VERBOSE_MAKEFILE on)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ffreestanding")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffreestanding")

add_library(kernel kernel.c)
target_link_libraries(kernel ${CMAKE_CURRENT_BINARY_DIR}/kernel_entry.o)
set_target_properties(kernel
            PROPERTIES LINK_FLAGS "-Ttext 0x1000 --oformat binary"
            )
set_target_properties(kernel PROPERTIES PREFIX "")
set_target_properties(kernel PROPERTIES OUTPUT_NAME "kernel" )
set_target_properties(kernel PROPERTIES SUFFIX ".bin")