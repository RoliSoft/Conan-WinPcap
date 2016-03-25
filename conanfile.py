from conans import ConanFile
import os, shutil
from conans.tools import download, unzip, check_sha1
from conans import CMake

class WinPcapConan(ConanFile):
	name = "WinPcap"
	version = "4.1.2"
	license = "BSD"
	url = "https://github.com/RoliSoft/Conan-WinPcap"
	settings = {"os":   ["Windows"],
	            "arch": ["x86", "x86_64"]}
	FOLDER_NAME = "WpdPack"
	
	def source(self):
		zip_name = "WpdPack_4_1_2.zip"
		
		download("https://www.winpcap.org/install/bin/%s" % zip_name, zip_name)
		check_sha1(zip_name, "f5c80885bd48f07f41833d0f65bf85da1ef1727a")
		unzip(zip_name)
		os.unlink(zip_name)
	
	def package(self):
		self.copy(pattern="*.h", dst="include", src="%s/Include" % self.FOLDER_NAME)
		self.copy(pattern="*.a", dst="lib",     src="%s/Include" % self.FOLDER_NAME, keep_path=False)
		
		if self.settings.arch == "x86":
			self.copy(pattern="wpcap.lib",  dst="lib", src="%s/Lib" % self.FOLDER_NAME, keep_path=False)
			self.copy(pattern="Packet.lib", dst="lib", src="%s/Lib" % self.FOLDER_NAME, keep_path=False)
		else:
			self.copy(pattern="wpcap.lib",  dst="lib", src="%s/Lib/x64" % self.FOLDER_NAME, keep_path=False)
			self.copy(pattern="Packet.lib", dst="lib", src="%s/Lib/x64" % self.FOLDER_NAME, keep_path=False)
	
	def package_info(self):
		self.cpp_info.libs = ['WinPcap']
