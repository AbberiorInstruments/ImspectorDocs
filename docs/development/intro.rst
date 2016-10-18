A little KB
=============

There is no comprehensive guide to the data model, the SDK and the class hierarchy in Imspector and most probably this
will only become available after adding python scripting support. For now, there is a small collection of topics
that we stumble upon. The following information may be incomplete, inaccurate or plain wrong depending on when it was
added and what was changed afterwards.

SpecDll versions, revisions and module revisions
-------------------------------------------------

The Imspector solution and/or SDK contains a few python scripts and associated batch files that add the current
subversion revision of various modules to header files as defines. Currently the rationale is as follows:
A plugin's file where the CWinApp::InitInstance method is implemented imports either <SpecInitialize.h>:


.. code-block:: cpp

   #include "rev.h"
   #include <SpecInitialize.h>

where <SpecInitialize.h> looks like this:

.. code-block:: cpp
   
   #ifndef SPECDLL_VERSION
        // The SpecDll Version. This would change with branches. Possibly
        // we have it consistent with the name.
        // The rule is: if this: if this changes, the API definitely breaks and the
        // plugin will not be loaded. 
   #	ifndef SPECDLL_REVISION
   #		include <SpecRevision.h>
   #	endif
   
   #	ifndef MODULE_REVISION
   #		define MODULE_REVISION 0
   #	endif
   
   #	include <SPECInit.h>
   #endif

where SPECInit.h defines the functions

.. code-block:: cpp

   #ifndef SPECDLL_VERSION
	   // The SpecDll Version. This would change with branches. Possibly
	   // we have it consistent with the name.
	   // The rule is: if this: if this changes, the API definitely breaks and the
	   // plugin will not be loaded. 
   #	define SPECDLL_VERSION (0x0010 | (SPECDLL_REVISION << 16))
	   
	   //! Call this function to add the resource handle of the dll to the chain
	   //! in your plugin or application.
	   //! SpecDll_Init() will fail if your version is larger than that of
	   //! the loaded dll or if your major version is not binary compatible
	   //! with the dll version loaded.
	   SPEC_EXT_CLASS BOOL SpecDll_Init(
				   DWORD winnt = _WIN32_WINNT,
				   DWORD specver = SPECDLL_VERSION,
				   LPCTSTR modname = __MODULE__,
				   DWORD modrev  = MODULE_REVISION);
	   
	   //! One simple line for the lazy ones. Put this into InitInstance() of
	   //! your dll's CWinApp object.
	   #define SpecDll_Initialize() \
		   if (! SpecDll_Init()) return FALSE;
   
	   //! Get the version of the dll actually loaded in memory. You can
	   //! use SPECDLL_VERSION in your code anywhere for the version you
	   //! compiled against. e.g. SPECDLL_VERSION == SpecDll_GetVersion()
	   //! is TRUE if they are the same.
	   SPEC_EXT_CLASS DWORD SpecDll_GetVersion();
   
	   //! Get the human-readable form of the version
	   SPEC_EXT_CLASS LPCTSTR SpecDll_GetVersionName(DWORD specver);	
   #endif

The file <SpecRevision.h> includes a define for SPECDLL_REVISION which is the last revision when any relevant code of SpecDll
including SpecLib was updated. This importantly includes all the helper libraries, too. This revision is likely to
mark a change in the way the library behaves.
The file SpecRevision.h is written by the WriteSpecRev.bat script which does NOT FAIL if there is no valid python installation
accessible. In this case the file remains unchanged.
The SPECDLL_VERSION should manually be updated any time the header files change, i.e. when the binary compatibility is
sure to break. The above section is subject to change.

A plugin simply calling SpecDll_Initialize() will thus tell the library at runtime against which revision of it it 
has been compiled but it will not tell which revision of the repository it was compiled from itself.
   
Alternatively a plugin can call 'WriteRev.bat' as a pre-build step. If there is a valid python configuration it will write
a file "rev.h" including the current SpecDll revision (the same as written in <SpecRevision.h>) and a definition for
MODULE_REVISION which is passed into SpecDll at runtime.
Instead of including <SpecInitialize.h> such a plugin should then

.. code-block:: cpp

   #include "rev.h"

Why so complicated? Well, the problem is that we may well change some of the cpp code in SpecDll and therefore the revision
of SpecDll will change but no re-compile of the plugins is necessary. If the plugin would include <SpecRevision.h> or includes
<SpecInitialize.h> it will then be re-compiled due to the change in <SpecRevision.h>. 
This is unacceptable in a development cycle. "rev.h" on the other hand will change only when the pre-build step for
the module is triggered, i.e. when the build system has in fact determined that the module needs updating. It will then ensure 
that the correct value for SPECDLL_REVISION and MODULE_REVISION is put in. 
Please not that MODULE_REVISION is NOT the last changed revision but the revision of the whole repository at compile 
time.

Imspector treats a module compiled against a different version of SpecDll an error but if the SPECDLL_REVISION of a module
(revision when module was compiled) and that of SpecDll (revision when SpecDll was compiled) are different only a 
warning is logged to the log file.


Exception Handling and Crash Reporting
--------------------------------------

At the moment all code is compiled in Microscoft C++ with the /EHsc option. That is, C++ exceptions are of course enabled
but win32 exceptions are not handled by the catch(...) block and clean-up code is not compiled into any try-block that 
can throw a C++ exception. Whether or not clean-up code is compiled into it and the stack is properly unwound may
depend on compiler optimization.
There is an excellent article at http://www.thunderguy.com/semicolon/2002/08/15/visual-c-exception-handling/ about this.
In short there are three solutions to the problem

1. Compile with /EHs or /EHsc. Your win32 exceptions will end up in a __catch(translator) {} block if you have it.
   the stack will not be unwound and from there you can do whatever you want. (Mostly you can pass the exception up
   or you can enter the handler. Continuing execution is not really an option for most exceptions.
2. Compile with /EHa and make sure you have catch(...) handlers wherever needed to ensure proper stack unwinding
   (that means that you need a try .. catch wherever a win32 exception is expected. 
3. Compile with /EHa and throw a C++ exception in your default translator. This does not play well when compiling 
   with /EHs because the compiler does not know that functions without a throw() statement can throw c++ exceptions
   and will omit the clean-up code and the handler in these functions. 

Currently we have option 3 for handling unexpected exceptions but not with the necessary /EHa compiler option 
(at least not for all modules). The reason why this is OK IMHO is that we do not set the default
translator but rather SetUnhandledExceptionFilter() which will be called only if there is not appropriate __catch() 
statement. Therefore whenever the filter is called  a serious occurred and we will live with the stack not
being properly unwound before we reach our error handling code. In fact this may even be good as we don't know whether
the program is in some bad condition. 
In 
addition there is a problem as MFC includes some exception handling in the windows callback functions:

On 64bit systems running a 32bit application the process will usually 
swallow exceptions behind a window callback.
This is a windows bug which may stay in place because it has been there
for a long time. See `Microsoft KB 976038`__ and `this forum post`__ for details.

__ http://support.microsoft.com/kb/976038
__ http://connect.microsoft.com/VisualStudio/feedback/details/550944/hardware-exceptions-on-x64-machines-are-silently-caught-in-wndproc-messages

Calling this function will enable the hotfix and cause an 
an application error dialog to appear instead. Importantly the exception
is still not propagated upwards, i.e. there is no stack unwinding to a possible
exception handler before the callback. I have still to test whether this is true for all exceptions and
whether it depends on the exception model we compile with. The behaviour of the hotfix
is to enter an exception handler that ultimately crashes the program.

For some applications, enabling the hotfix is not enough. They rely on 
being able to catch the exception and do e.g. some data recovery before 
exiting or they roll their own diagnostics.
There is no known way to make the exception go past the callback but with 
this function you can wrap the default windows procedure in MFC with a 
procedure that handles exceptions. The easiest way to do this is shown
in the comment below.

.. note::
   Subclassing in MFC is a little complicated as there is both the windows procedures (and the default MFC windows procedure calls the 
   MFC CWnd::WindowProc implementation which can be overwritten). So basically
   MFC windows can be subclassed by (1) overwriting the virtual 
   WindowProc function, (2) adding entries to the message map handled by the 
   standard implementation and (3) subclassing in the windows sense, that is
   by calling SetWindowLong(). 
   We do not want to call SetWindowLong on each and every window, maintain
   a map of previous functions etc. Rather we replace the function pointer 
   that is used by _AfxCbtFilterHook() to set the subclass the window 
   making it call some windows procedure that will actually call the member
   function.

.. note::
   This explanation, even the way MFC handles this may change and then 
   the code may stop working. If that happens, find out where the new 
   MFC version calls SetWindowLong() to subclass the windows and replace
   the pointer it uses by the installed windows procedure.

.. note::
   One should also look at context switching. Exceptions occurring behind a context switch will be
   caught and rethrown, obscuring their
   origin. In order to avoid this, call AfxSetAmbientActCtx(FALSE);
   in every InitInstance() function.

See `this forum post`__ for details.

__ http://connectppe.microsoft.com/VisualStudio/feedback/details/563622/mfc-default-exception-handling-causes-problems-with-activation-context
