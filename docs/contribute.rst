=================
How to Contribute
=================

.. todo:: Github and Readthedocs workflow not described here.

You are welcome to correct any errors and contribute yourself to this documentation. 

Correct Mistakes
-----------------------------------

The easiest way is to send in patches for existing pages. 
All documentation is created using `restructured text <http://docutils.sourceforge.net/rst.html>`_  which basically means 
that you have to edit some text files.
You can get the existing source of any page by clicking on the 'Show Source' link on the left sidebar and adjust it to 
your liking. Unfortunately you will not be able to see the results unless you rebuild the documentation using the 
`Sphinx documentation generator <http://sphinx.pocoo.org/>`_ but you are more than welcome to send in untested 
text fragments and we will do our best to format and include them. If you want to include screenshots, just 
attach them and mark the place where to include them in your text file using a restructured text directive or
any other way that is understandable to an editor. We are happy about any bit of content we do not have to 
create ourselves.

Of course, proposals for new sections or documentation pages are also welcome as plain text, restructured 
text or any other format you are comforable with.

Download and Compile 
-----------------------------------------------------------

The documentation is in a subversion repository `here <https://nanosvn.mpibpc.mpg.de/svn/Software/Imspector/doc>`_. 
If you have no access to it yet, please write us a mail to mailto:support@imspector.de and request a username and 
password for it. It is the same repository that holds any custom plugin code that is shared and co-developed 
with external partners.
Currently there is only the trunk version but the structure of the repository may change. The current link will 
always be in the newest online documentation on this page. So if your 'update' or 'commit' does not work 
anymore, please check back here.

After checking out you also need to install Sphinx on your computer. Sphinx is well documented and you should 
not run into any trouble - I might add a tutorial here later (or you can update this page). Once everything 
is in place typing 

        | > make html

on a command prompt in the 'doc' directory should build the documentation. You can edit the .rst files 
with any editor. I am using 'gvim' which has syntax coloring for re-structured text. 
There is one feature added to the documentation that helps bringing up a source file in the editor 
which is currently viewed in the browser:

A sort of an IDE for restructured Text
--------------------------------------

The script includes a non-standard 'edit source' link in every page of your documentation. It will point to the 
source '.rst' file if you set up the correct 'edit_path' variable in 'conf.py'. Open 'conf.py' and find 
the 'html_context' dictionary and adjust the 'edit_path' value to the local, absolute path to your 'doc/source' 
directory. Then rebuilt your documentation (you may have to do a 'make clean' and then 
'make html' again in order to force rebuilding all the pages.)
Clicking on the 'edit source' link will now use the default editor for 'rst' file set in your browser. 
More than likely you have not set this application yet. In firefox you will therefore see the following
dialog:

.. image:: /images/firefox_rsttype1.png
   :align: center

Click 'Browse ..' and browse to your documentation sources. You will not see 'edit.bat' as the dialog only shows '.exe' files
but you can directly enter it into the filname edit box. Click ok and you are back in the dialog:

.. image:: /images/firefox_rsttype1.png
   :align: center

Make sure you check the 'Do this automatically ...' option and click 'OK'. If you do not want
to use gvim or if it is located at a different path, please copy edit.bat to another filename or location and
point firefox to your custom version. If you want to use notepad, just select it instead of edit.bat.

The default 'edit.bat' also located in the 'doc' directory opens an additional tab in a gvim 
instance already running giving you 'almost' and IDE:

.. image:: /images/gvim_indexrst.png
   :align: center


Committing
----------

If you feel confident about your changes, commit them. Otherwise send in the modified files to me by 
email. I agree that GIT or any other distributed source control would be better but subversion it is for now.
