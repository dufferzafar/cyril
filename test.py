import glob
import os
import unittest


if __name__ == '__main__':
    names = []
    for filename in glob.glob("test/test_*.py"):
        name = os.path.splitext(os.path.basename(filename))[0]
        names.append("test." + name)

    tests = unittest.defaultTestLoader.loadTestsFromNames(names)
    runner = unittest.TextTestRunner(verbosity=2)

    testresult = runner.run(tests)
