import os

from conans import ConanFile, CMake, tools


class PgnextractTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def imports(self):
        self.copy("pgn-extract", dst="bin", src="bin")

    def test(self):
        self.run("{} --version".format(os.path.join(
            os.getcwd(), "bin", "pgn-extract")))
