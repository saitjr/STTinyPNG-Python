import tinify
import os
import os.path

tinify.key = "Jp0V-TmAcz3T31zfyA-lm_HAwuMOKFgM"
fromFilePath = "/Users/tangjr/Desktop/test1"
toFilePath = "/Users/tangjr/Desktop/test2"

for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg':
			toFullPath = toFilePath + root[len(fromFilePath):]
			toFullName = toFullPath + '/' + name

			if os.path.isdir(toFullPath):
				pass
			else:
				os.mkdir(toFullPath)

			source = tinify.from_file(root + '/' + name)
			source.to_file(toFullName)
			
			with open(toFullName, 'rb') as source:
			    source_data = source.read()
			    result_data = tinify.from_buffer(source_data).to_buffer()