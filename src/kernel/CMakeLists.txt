add_library(kernel kernel.cpp)
target_link_libraries(kernel ports ${CMAKE_BINARY_DIR}/kernel_entry.o "-Ttext 0x1000 --oformat binary")
add_dependencies(kernel kernel_entry)

set_target_properties(kernel PROPERTIES LINKER_LANGUAGE CXX)
set_target_properties(kernel PROPERTIES PREFIX "")
set_target_properties(kernel PROPERTIES SUFFIX ".bin")