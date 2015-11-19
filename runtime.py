#!/usr/bin/env python

import pprint

from LeanTestingSDK.PyClient import PyClient as LeanTestingClient

p = pprint.PrettyPrinter()

LT = LeanTestingClient()
LT.attachToken('3UsdKZXpGPnvHuJ9di1SeAFqrp14GKvQQMyclGRk')

# METHOD DEMONSTRATIONS

#####################################################################################

# Including Lean Testing Python SDK
# from LeanTestingSDK.PyClient import PyClient as LeanTestingClient

# Creating A New INSTANCE
# LT = LeanTestingClient()

#####################################################################################

# Get Current TOKEN
# LT.getCurrentToken()

# Attach New TOKEN
# LT.attachToken('9ErdKZXpGPnvHuJ9di92eAFqrp14GKvfHMyclGGh')

# Generate Authorization URL
# generatedURL = LT.auth.generateAuthLink(
#   'RBxaSvtplj1Xos4vbEbwGKkXRu0GJmd5Rdha2HHa',
#   'http://lev.it.cx:17600/lean/',
#   'admin',
#   'a3ahdh2iqhdasdasfdjahf26'
# )
# p.pprint(generatedURL)

# Exchange Authorization Code For Access TOKEN
# token = LT.auth.exchangeAuthCode(
#   'RBxaSvtplj1Xos4vbEbwGKkXRu0GJmd5Rdha2HHa',
#   'FpOZxNbe9VEwVbjUINoAepOhgS8FNQsOkpE4CtPO',
#   'authorization_code',
#   '3UwWk6uGccGTnV1wG1kA1WSeTM278zFmPwjAzThS',
#   'http://lev.it.cx:17600/lean/'
# )
# p.pprint( token )

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
#   'name': 'Project0253',
#   'organization_id': 5779
# })
# p.pprint( newProject.data )

# Retrieve An Existing PROJECT
# p.pprint( LT.projects.find(3515).data )


# List PROJECT Sections
# p.pprint( LT.projects.find(3515).sections.all().toArray() )

# Adding A PROJECT Section
# newSection = LT.projects.find(3515).sections.create({
#   'name': 'AnotherSctNm1'
# })
# p.pprint( newSection.data )


# List PROJECT Versions
# p.pprint( LT.projects.find(3515).versions.all().toArray() )

# Adding A PROJECT Version
# newVersion = LT.projects.find(3515).versions.create({
#   'number': 'v0.2.7889'
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
# newBug = LT.projects.find(3515).bugs.create({
#   'title': 'Something bad happened...',
#   'status_id': 1,
#   'severity_id': 2,
#   'project_version_id': 10242
# })
# p.pprint( newBug.data )

# Retrieve Existing BUG
# p.pprint( LT.bugs.find(38483).data )

# Update A BUG
# updatedBug = LT.bugs.update(118622, {
#   'title': 'Updated title happened...',
#   'status_id': 1,
#   'severity_id': 2,
#   'project_version_id': 10242
# })
# p.pprint( updatedBug.data )

# Delete A BUG
# p.pprint( LT.bugs.delete(118622) )

#####################################################################################

# List Bug COMMENTS
# p.pprint( LT.bugs.find(38483).comments.all().toArray() )

#####################################################################################

# List Bug ATTACHMENTS
# p.pprint( LT.bugs.find(38483).attachments.all().toArray() )

# Upload An ATTACHMENT
# filePath = '/store1/Downloads/Faine/1370240743_2294218.jpg'
# newAttachment = LT.bugs.find(38483).attachments.upload(filePath)
# p.pprint( newAttachment.data )

# Retrieve An Existing ATTACHMENT
# p.pprint( LT.attachments.find(21515).data )

# Delete An ATTACHMENT
# p.pprint( LT.attachments.delete(75258) )

#####################################################################################

# List PLATFORM Types
# p.pprint( LT.platform.types.all().toArray() )

# Retrieve PLATFORM Type
# p.pprint( LT.platform.types.find(1).data )


# List PLATFORM Devices
# p.pprint( LT.platform.types.find(1).devices.all().toArray() )

# Retrieve Existing Device
# p.pprint( LT.platform.devices.find(11).data )


# List OS
# p.pprint( LT.platform.os.all().toArray() )

# Retrieve Existing OS
# p.pprint( LT.platform.os.find(1).data )

# List OS Versions
# p.pprint( LT.platform.os.find(1).versions.all().toArray() )


# List Browsers
# p.pprint( LT.platform.browsers.all().toArray() )

# Retrieve Existing Browser
# p.pprint( LT.platform.browsers.find(1).data )

# List Browser Versions
# p.pprint( LT.platform.browsers.find(1).versions.all().toArray() )
