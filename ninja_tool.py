import os
from ninja_syntax import Writer
import inspect


def check_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


class ninja_tool_class:
    projRoot = ""
    buildRoot = ""
    buildfile = None
    ninjaWriter = None
    objPathDict = {}

    ASM = None
    ASMFlag = None
    CC = None
    CFlag = None
    linker = None
    linkFflag = None

    currPath = None

    _build_types = {"compile": "compile", "link": "link"}

    def __init__(self):
        self.projRoot = os.getcwd()
        self.currPath = self.projRoot
        self.buildRoot = check_dir(os.path.join(self.projRoot, "build"))
        try:
            self.buildfile = open(os.path.join(self.buildRoot, "build.ninja"), "w")
            self.ninjaWriter = Writer(self.buildfile)
        except IOError:
            print("[Error] Failed to init build.ninja file: " + os.path.join(self.buildRoot, "build.ninja"))

    def __del__(self):
        self.buildfile.close()

    def step_to_dir(self, currentPath):
        self.currPath = currentPath
        return self

    def add_default(self, target):
        self.ninjaWriter.default(self.objPathDict[target])

    def add_rule(self, name, command):
        self.ninjaWriter.rule(name, command)
        return self

    def add_build(self, buildType, out, rule, inputs, variables=None):
        # Calculate source path & product path
        relPath = os.path.relpath(self.currPath, start=self.projRoot)
        productPath = check_dir(os.path.join(self.buildRoot, relPath))

        print("Add build for folder: " + relPath)
        print("Product path: " + productPath)

        outputs = os.path.join(productPath, out)

        # Add build command
        if buildType == self._build_types["compile"]:
            self.ninjaWriter.build(outputs=outputs,
                                   rule=rule,
                                   inputs=[os.path.join(self.currPath, f_code) for f_code in inputs],
                                   variables=variables
                                   )
        elif buildType == self._build_types["link"]:
            self.ninjaWriter.build(outputs=outputs,
                                   rule=rule,
                                   inputs=[self.objPathDict[obj] for obj in inputs],
                                   variables=variables
                                   )
        else:
            print("[Error] Unrecogonized buildType: " + buildType)

        # save product name and its path
        self.objPathDict[out] = outputs
        return self


ninja_tool = ninja_tool_class()
