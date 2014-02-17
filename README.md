draft-transforms
================

tools for modifying drafts of Connexions content in a batch manner, from the
commandline.

Needs an installable version of requests-toolbelt, which seems to mean 
version > 0.1.2

This repo installs a single master command `draft-transform`, which performs
operations on all the modules in a particular legacy Connexions workgroup.
This command will do a checkout on any modules in the 'published' state, as well.

Common options to all commands are:
  -h help
  -H --host hostname requires https access for non-localhost
        defaults to qa.cnx.org
  -a --auth username:password (required)
  -w --workgroup ID  Workgroup to operate against
        defaults to private workspace
  -u --upload Send transformed content back to workgroup
  -p --publish message Publish the modules after upload
  -P publish_only message Publish all modules in workgroup, no download or upload
  -s --save-dir directory save intermediate results to this directory, named <id>.xml
        will create the directort if necessary
  

Available subcommands are:
    download [directory]
        download the module body, save it in directly (same as -s above, but no
        transform)
    xslt file.xsl apply xslt from file.xsl to each module contents.

Examples:

draft-transform -H qa.cnx.org -a 'me:mypass' download my_modules
    dowloads and saves all modules from private workspace to the directly my_modules

draft-transform -H cnx.org -a 'me:mypass' -w wg123 -s fixed_files xslt myfix.xsl
    downloads, transforms and saves transformed content

draft-transform -H cnx.org -a 'me:mypass' -w wg123 -s fixed_files -u xslt myfix.xsl
    downloads, transforms, saves, and uploads transformed content

draft-transform -H cnx.org -a 'me:mypass' -w wg123 -P 'Fixes that markup bug'
    Publishes all the modules in the workgroup

draft-transform -H cnx.org -a 'me:mypass' -w wg123 -s fixed_files -u -p 'Fixed that markup bug' xslt myfix.xsl
    downloads, transforms, saves, and uploads, and publishes transformed content

