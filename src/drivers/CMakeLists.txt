set(driverSrc ports.cpp)

add_custom_target(drivers
                   ${CMAKE_CXX_COMPILER} ${CMAKE_CXX_FLAGS} ${driverSrc} -o drivers.o -I${CMAKE_CURRENT_SOURCE_DIR}
                   )
