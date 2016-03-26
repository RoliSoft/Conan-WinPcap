from conans import ConanFile
from conans.tools import download, unzip, check_sha1
import os, shutil

class WinPcapConan(ConanFile):
	name = "WinPcap"
	version = "4.1.2"
	license = "BSD"
	url="http://github.com/RoliSoft/Conan-WinPcap"
	exports = ["FindWinPcap.cmake"]
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
		self.copy("FindWinPcap.cmake", dst=".", src=".")
		
		self.copy(pattern="*.h", dst="include", src="%s/Include" % self.FOLDER_NAME)
		self.copy(pattern="*.a", dst="lib",     src="%s/Include" % self.FOLDER_NAME, keep_path=False)
		
		if self.settings.arch == "x86":
			self.copy("wpcap.lib",  dst="lib", src="%s/Lib" % self.FOLDER_NAME, keep_path=False)
			self.copy("Packet.lib", dst="lib", src="%s/Lib" % self.FOLDER_NAME, keep_path=False)
		else:
			self.copy("wpcap.lib",  dst="lib", src="%s/Lib/x64" % self.FOLDER_NAME, keep_path=False)
			self.copy("Packet.lib", dst="lib", src="%s/Lib/x64" % self.FOLDER_NAME, keep_path=False)
	
	def package_info(self):
		self.cpp_info.libs = ['wpcap', 'Packet']
