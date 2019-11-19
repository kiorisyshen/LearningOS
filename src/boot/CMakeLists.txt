# Build bootsect
# add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/bootsect.bin
#                    COMMAND nasm -i ${CMAKE_CURRENT_SOURCE_DIR} -f bin ${CMAKE_CURRENT_SOURCE_DIR}/bootsect.asm -o ${CMAKE_BINARY_DIR}/bootsect.bin)
add_custom_target(bootsect
                   nasm -i ${CMAKE_CURRENT_SOURCE_DIR} -f bin ${CMAKE_CURRENT_SOURCE_DIR}/bootsect.asm -o ${CMAKE_BINARY_DIR}/bootsect.bin
                   )
# Build kernel entry in elf ABI
# add_custom_command(OUTPUT ${CMAKE_BINARY_DIR}/kernel_entry.o
#                    COMMAND nasm -f elf ${CMAKE_CURRENT_SOURCE_DIR}/kernel_entry.asm -o ${CMAKE_BINARY_DIR}/kernel_entry.o)
add_custom_target(kernel_entry
                   nasm -f elf ${CMAKE_CURRENT_SOURCE_DIR}/kernel_entry.asm -o ${CMAKE_BINARY_DIR}/kernel_entry.o
                   )