cmake_minimum_required(VERSION 3.15)

set(CMAKE_SYSTEM_NAME Generic)

set(CMAKE_C_COMPILER ${CMAKE_SOURCE_DIR}/cross_compiler/i386elfgcc/bin/i386-elf-gcc)
set(CMAKE_CXX_COMPILER ${CMAKE_SOURCE_DIR}/cross_compiler/i386elfgcc/bin/i386-elf-g++)

SET(CMAKE_FIND_ROOT_PATH  ${CMAKE_SOURCE_DIR}/cross_compiler/i386elfgcc)
# search for programs in the build host directories
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

set(CMAKE_TRY_COMPILE_TARGET_TYPE "STATIC_LIBRARY")

project(LearningOS)

set(CMAKE_C_LINK_EXECUTABLE ${CMAKE_SOURCE_DIR}/cross_compiler/i386elfgcc/bin/i386-elf-ld)
set(CMAKE_CXX_LINK_EXECUTABLE ${CMAKE_C_LINK_EXECUTABLE})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ffreestanding -g")

include_directories(${CMAKE_SOURCE_DIR}/src)

add_subdirectory(src)

add_custom_target(osImage ALL 
                COMMAND cat ${CMAKE_BINARY_DIR}/bootsect.bin ${CMAKE_BINARY_DIR}/kernel.bin > ${CMAKE_BINARY_DIR}/osImage.bin
                DEPENDS bootsect kernel)

# Log out configuration variables
message(STATUS "C compiler: \t" ${CMAKE_C_COMPILER})
message(STATUS "C++ compiler:" ${CMAKE_CXX_COMPILER})
message(STATUS "C linker: \t" ${CMAKE_C_LINK_EXECUTABLE})
message(STATUS "C++ linker: \t" ${CMAKE_CXX_LINK_EXECUTABLE})
message(STATUS "Ar: \t\t" ${CMAKE_AR})
message(STATUS "Ranlib: \t" ${CMAKE_RANLIB})