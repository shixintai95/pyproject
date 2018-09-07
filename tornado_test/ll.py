m = {'file': [{'filename': 'a.txt', 'body': b'this is a.txt\n', 'content_type': 'text/plain'}]}


for inputname in m:
     filelist = m[inputname]
     print("file:%s" % filelist)
     for fileObj in filelist:
         print("fileObj %s " % fileObj)
         l = fileObj['filename']
         print(l)
