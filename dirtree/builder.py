from __future__ import print_function
import os


class Builder:
    def __init__(self):
        pass

    def buildPath(self, path, file):
        return path + '/' + file

    def buildRecursive(self, path, currDir, ignoreDirs):
        res = "{" + currDir + "}\n"
        lst = os.listdir(path)
        for i in sorted(lst):
            x = self.buildPath(path, i)

            if os.path.isdir(x):
                if i in ignoreDirs:
                    continue

            if os.path.isfile(x):
                f = i.replace("_", "\char`_")
                res += '[{' + str(f) + '},file]\n'
            elif os.path.isdir(x):
                res += self.buildRecursive(x, i, ignoreDirs)

        return "[" + res + "]"
