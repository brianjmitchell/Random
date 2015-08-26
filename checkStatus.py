def checkStatus():    

    import urllib
    from urllib.request import urlopen
    import xml.etree.ElementTree as ET
    jenkinsUrl = "http://ats-cismaster:8080/job/"
    jobName = ["LW-Automation-Tests", "Modspace-Automation-Tests", "Navigator-Automation-Tests", "Workbench-CI-Tests"]
    
    result = []
    
    for job in jobName:
        jenkinsStream   = urlopen( jenkinsUrl + job + "/lastBuild/api/xml" )
        tree = ET.parse(jenkinsStream)
        root = tree.getroot()
        
        for building in root.findall('building'):
            result.append(building.text)
            if building.text == "true":
                #urlopen( jenkinsUrl + "Workbench-CI-Tests/lastBuild/stop" )
                print("We have cancelled the job due to other test being run")
                return
    
    print("No other jobs running, carry on with the CI test")
    
checkStatus()       