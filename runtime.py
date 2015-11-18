#!/usr/bin/env python

import pprint

from LeanTestingSDK.PyClient import PyClient as LeanTestingClient

p = pprint.PrettyPrinter()

LT = LeanTestingClient()
LT.attachToken('3UsdKZXpGPnvHuJ9di1SeAFqrp14GKvQQMyclGRk')

# METHOD DEMONSTRATIONS

#####################################################################################

# Get USER Information
# p.pprint( LT.user.getInformation() )

# Get USER Organizations
# p.pprint( LT.user.organizations.all().toArray() )

#####################################################################################

# List All PROJECTS
# p.pprint( LT.projects.all().toArray() )

# Create A New PROJECT
# newProject = LT.projects.create({
# 	'name': 'Project0253',
# 	'organization_id': 5779
# })
# p.pprint( newProject.data )

# Retrieve An Existing PROJECT
# p.pprint( LT.projects.find(3515).data )


# List PROJECT Sections
# p.pprint( LT.projects.find(3515).sections.all().toArray() )

# Adding A PROJECT Section
# newSection = LT.projects.find(3515).sections.create({
# 	'name': 'AnotherSctNm1'
# })
# p.pprint( newSection.data )


# List PROJECT Versions
# p.pprint( LT.projects.find(3515).versions.all().toArray() )

# Adding A PROJECT Version
# newVersion = LT.projects.find(3515).versions.create({
# 	'number': 'v0.2.7889'
# })
# p.pprint( newVersion.data )

# List PROJECT Users
# p.pprint( LT.projects.find(3515).users.all().toArray() )


# List Bug Type Scheme
# p.pprint( LT.projects.find(3515).bugTypeScheme.all().toArray() )

# List Bug Status Scheme
# p.pprint( LT.projects.find(3515).bugStatusScheme.all().toArray() )

# List Bug Severity Scheme
# p.pprint( LT.projects.find(3515).bugSeverityScheme.all().toArray() )

# List Bug Reproducibility Scheme
# p.pprint( LT.projects.find(3515).bugReproducibilityScheme.all().toArray() )

#####################################################################################

# List All BUGS In A Project
# p.pprint( LT.projects.find(3515).bugs.all().toArray() )

# Create A New BUG
#TODO this

# Retrieve Existing BUG
# p.pprint( LT.bugs.find(38483).data )

# Update A BUG
#TODO this

# Delete A BUG
#TODO this

#####################################################################################

# List Bug COMMENTS
# p.pprint( LT.bugs.find(38483).comments.all().toArray() )

#####################################################################################

# List Bug ATTACHMENTS
# p.pprint( LT.bugs.find(38483).attachments.all().toArray() )

# Upload An ATTACHMENT
#TODO this

# Retrieve An Existing ATTACHMENT
# p.pprint( LT.attachments.find(21515).data )

# Delete An ATTACHMENT
#TODO this

#####################################################################################

# List PLATFORM Types
# p.pprint( LT.platform.types.all().toArray() )

# Retrieve PLATFORM Type
#TODO wait for fix


# List PLATFORM Devices
#TODO wait for fix

# Retrieve Existing  Device
#TODO wait for fix


# List OS
# p.pprint( LT.platform.os.all().toArray() )

# Retrieve Existing OS
#TODO wait for fix

# List OS Versions
#TODO wait for fix


# List Browsers
#TODO wait for fix

# List Browser Versions
#TODO wait for fix


