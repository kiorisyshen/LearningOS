add_library(kernel kernel.cpp)
target_link_libraries(kernel drivers)
add_dependencies(kernel kernel_entry)

set_target_properties(kernel PROPERTIES LINKER_LANGUAGE CXX)
set_target_properties(kernel PROPERTIES PREFIX "")
set_target_properties(kernel PROPERTIES SUFFIX ".bin")
set_target_properties(kernel PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})