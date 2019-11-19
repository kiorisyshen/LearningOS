/* This will force us to create a kernel entry function instead of jumping to
 * kernel.c:0x00 */
void dummy_test_entrypoint() {
}

class testCpp {
   public:
    char outputStr[5] = {'X', '_', 'c', 'p', 'p'};
};

void main() {
    testCpp testcpp;

    char *video_memory = (char *)0xb8000;

    for (int i = 0; i < sizeof(testcpp.outputStr); ++i) {
        *video_memory = testcpp.outputStr[i];
        video_memory += 2;
    }
}