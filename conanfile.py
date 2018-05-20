from conans import ConanFile, CMake, tools

class PgnextractConan(ConanFile):
    name = "pgn-extract"
    version = "17.55"
    license = "GPLv3. ftp://ftp.cs.kent.ac.uk/pub/djb/pgn-extract/COPYING"
    url = "https://github.com/mathplayer/conan-pgn-extract"
    description = " ".join([
        "A Portable Game Notation (PGN) Manipulator for Chess Games. "
        "https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/"
    ])
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/mathplayer/pgn-extract.git")
        self.run("cd {} && git checkout {}".format(self.name, self.version))

    def build(self):
        self.run("make -C {}".format(self.name))

    def package(self):
        self.copy("pgn-extract", dst="bin", src="pgn-extract")

    #def package_info(self):
    #    self.cpp_info.libs = ["hello"]

