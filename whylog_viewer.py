# NotebookProfileVisualizer is not available in whylogs v0
# A browser based visualization tool for a single profile can be launched with the following. 

from whylogs.viz import profile_viewer
profile_viewer()

# Users can provide a profile’s json to this tool located in the following path
# output/{dataset_name}/{session_id}/json/dataset_profile.json