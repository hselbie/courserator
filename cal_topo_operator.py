from sartopo_python import SartopoSession
import time
  
sts=SartopoSession("localhost:8080","<offlineMapID>")
fid=sts.addFolder("MyFolder")
sts.addMarker(39,-120,"stuff")
sts.addMarker(39.01,-120.01,"myStuff",folderId=fid)
r=sts.getFeatures("Marker")
print("r:"+str(r))
print("moving the marker after a pause:"+r[0]['id'])
time.sleep(5)
sts.addMarker(39.02,-120.02,r[0]['properties']['title'],existingId=r[0]['id'])