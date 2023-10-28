from org.apache.commons.io import IOUtils

# Read the content of the FlowFile
flowFile = session.get()
if flowFile is not None:
    try:
        content = IOUtils.toString(flowFile)
        # Perform your processing on the content here

        # Transfer the FlowFile to the success relationship
        session.transfer(flowFile, REL_SUCCESS)
    except Exception as e:
        # If an exception occurs during processing, transfer to failure
        session.transfer(flowFile, REL_FAILURE)
else:
    # If no FlowFile is available, transfer to failure
    session.transfer(flowFile, REL_FAILURE)
