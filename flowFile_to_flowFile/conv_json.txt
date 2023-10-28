import json
from datetime import datetime
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import os


class ModJSON(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        array = []
        input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        input_data = json.loads(input_text)
        for item in input_data:
            temp_json = {
                "id":item["id"],
                "challan_id":item["challan_id"],
                "mobile":item["mobile"]
            }
            array.append(temp_json)
        output_json = json.dumps(array)
        outputStream.write(output_json)


flowFile = session.get()
if (flowFile != None):
    try:
        flowFile = session.write(flowFile, ModJSON())
        session.transfer(flowFile, REL_SUCCESS)
    except:
        session.transfer(flowFile, REL_FAILURE)

session.commit()
