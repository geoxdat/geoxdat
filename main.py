from geox import GeoX


geox = GeoX(api_key='iI5NXd5VvrblQ4RBpssF3PReuOQMLP9U')
project = geox.read_project('TST000')
# project_versions = project.read_all_project_versions()
project_version = project.read_project_version('qYTqTkiPfOY45o4gHNUBzcgcpHjqSzbG')
project_version.read_alteration_data(save_to_file=False)
print(geox._timestamp)