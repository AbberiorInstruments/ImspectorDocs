========================
The File Format
========================

The Imspector MSR File Format
------------------------------

The Imspector '.msr' file format is a native binary format and now api exists to read or write it in its entirety.
As window positions, data dependencies, hardware configuration and settings measurement state and configuration 
settings are saved in each document reading the entirety of this information is hardly desireable for other programs. 
The file format evolves with Imspector but old files will always remain readable with newer versions of Imspector 
or a conversion tool will be made available.

The data and directly associated meta-data contained in any Imspector file is organized according to the specification
of the OBF (\*.obf) file format and Imspector also reads OBF files in an intuitive way. There are bindins for OBF to
both c++, MATLAB and JAVA and we are working on Labview and Python bindings to allow reading of Imspector data into 
most applications used in scientific data analysis and to allow writing to an Imspector-readable format 
from Labview. 

The C++ API for OBF will be rather stable as the file format evolves. The format itself is forward and backwards 
compatible between all versions released. 

.. note:: 
   The fact that OBF is compatible in both directions helps when reading a newer version .msr file with
   an old Imspector copy. While window positions and some analysis related data is omitted, all physical data and 
   the associated meta-data remains readable. Just (temporally) rename the file to .obf and open it in Imspector.

.. note:: 
   Some older versions of Imspector do not write OBF files and used the DBL (\*.dbl) format as an exchange 
   file format. This format is also documented below for completeness.


The OBF File Format
--------------------

While it is recommended that you use the ANSI-C or C++ interface provided by the **OmasIo**
dll to read and write OBF files the file structure is relatively 
simple and it should be straightforward to implement a reader or writer for OBF files. 
A native OBF file starts with the following binary file header. Please note that alll structures saved in
binary format into an OBF file have packsize 1 and that all binary data is stored in little endian 
byte order (i.e. the byte order used on x86, x64, Itanium and Alpha platforms) 

.. code-block:: cpp

   typedef struct _OBF_FILE_HEADER
   {
        //! Must be "OMAS_BF\n" followed by 0xff 0xff 
        char magic_header[10]; 
        //! The actual format version of the file.
        omas_UINT32 format_version;
        //! The position of the first stack header in the file
        omas_UINT64 first_stack_pos;
        //! Length of following UTF8 description (bytes).
        omas_UINT32 descr_len;
   } OBF_FILE_HEADER;

The header is immediately followed by :cppcode:`descr_len` bytes of a UTF-8 string containing
the file description which is preferably in xml format such that it can be parsed into a 
:cppcode:`OPropstruct` by the function :cppcode:`omas_xml2prop()` described in a later 
chapter.  

From format version 2 on the file description string is followed by the meta data position

.. code-block:: cpp

    omas_UINT64 meta_data_position_ ;

The header members are

magic_header
   The magic header identifies compatible OBF files and no read routine should go on if it 
   does not match. 

format_version
   The format version is used by newer routines to read older lacking features 
   but the file format is designed to be upwards and downwards compatible. That 
   is, newer features and additional information is to be added such that the old 
   routines should be able read as much information from files of a newer version 
   as possible. This document describes format version 1.

first_stack_pos
   Location of the first stack header in the file. Passing this to a :cppcode:`seek()`
   function should position the file pointer to the beginning of a stack header
   (see below)

descr_len
   Length of the file description string following this header immediately in bytes
   (not in characters). The string is defined to be in UTF-8 encoding.


OBF is an embeddable file format. i.e. a more feature-rich file format may choose to be
readable as OBF by having this file header at its beginning, writing any additional information
between the header and any stacks as long as the first stack header is found where 
specified by :cppcode:`first_stack_pos`. Each stack starts with a binary header of the following
structure:

.. code-block:: cpp

   typedef struct _OBF_STACK_HEADER
   {
      //! Magic header "OMAS_BF_STACK\n" then 0xff 0xff
      char magic_header[16]; 
      //! The version of the file format
      omas_UINT32 format_version;
      //! The rank of the stack.
      omas_UINT32 rank;
      //! The number of pixels along the axes
      omas_UINT32 res[OMAS_MAX_DIMENSIONS];
      //! The phyisical length of the stack axes
      double len[OMAS_MAX_DIMENSIONS];
      //! The physical offset of the stack
      double off[OMAS_MAX_DIMENSIONS];
      //! The data type of the stack on disk.
      omas_DT dt;
      //! The type of compression. 
      omas_UINT32 compression_type;
      //! The compression level 0-9
      omas_UINT32 compression_level;
      //! The length of the utf-8 name of the stack in bytes
      omas_UINT32 name_len;
      //! The length of the utf-8 description in bytes. 
      omas_UINT32 descr_len;
      //! Unused as of version 1
      omas_UINT64 reserved;
      //! The length of the data on the disk.   
      omas_UINT64 data_len_disk;
      //! The next stack position in the file
      omas_UINT64 next_stack_pos;
            
   } OBF_STACK_HEADER;

The header is immediately followed by :cppcode:`name_len` bytes of a UTF-8 string containing
the stack name and :cppcode:`descr_len` bytes containing the UTF-8 encoded stack description, 
which is, again, preferably in xml format such that it can be parsed into a 
:cppcode:`OPropstruct` by :cppcode:`omas_xml2prop()`.  The binary data is possibly compressed
and follows immediately after the description and takes up exactly :cppcode:`data_len_disk` bytes.
\newline
The header members are

magic_header
   The magic header identifies compatible OBF stacks and a read routine should stop
   reading the file when it is not found at the specified position. 
format_version
   The format version for backwards compatibility. This allows versions being set 
   per stack if necessary. E.g. the stack footer is present only in version 1, not in
   version 0 and a write routine may choose to write stacks as version 0 omitting
   the footer and other stacks (in the same file) as version 1 including the footer.
   IMPORTANT: A reader for version n is allowed to read the stack of higher version
   as long as it found the magic_header and as long as it seeks to the end of the 
   footer using its size member before reading the variably sized components. 
rank
   The number of used dimensions. The following members are valid only up to
   e.g. :cppcode:`res[rank-1]`.
res (*only the first* rank *members are valid*)
   The number :cppcode:`res[i]`. is the number of pixels the stack has along the i'th
   dimension.
len (*only the first* rank *members are valid*)
   The physical length along each used dimension. Units may be given as part of 
   the dimension labels in the footer. The physical center position of the k*th* along
   the i*th* axis is given by :cppcode:`off[i] + (.5 + k)*len[i]/res[i]` where k 
   runs from :cppcode:`0! to \lstinline!res[i] - 1`.
off (*only the first* rank *members are valid*)
   The physical offset. May be used to specify relative positions of stack volumes
   inside a larger measurement space.
dt (*see* OmasTypes.h *for the actual values*)
   The binary data type as stored on disk. The {\bf Omas} binary types are explained
   in detail later together with their helper routines. For the file format the constants
   are:

   .. code-block:: cpp

      #define OMAS_DT_AUTO    0x00000000 // Automatically determine the data type 
      #define OMAS_DT_UINT8   0x00000001 // An unsigned byte 
      #define OMAS_DT_SINT8   0x00000002 // A signed char 
      #define OMAS_DT_UINT16  0x00000004 // A 16 bit word value 
      #define OMAS_DT_SINT16  0x00000008 // A 16 bit signed integer 
      #define OMAS_DT_UINT32  0x00000010 // A 32 bit unsigned integer 
      #define OMAS_DT_SINT32  0x00000020 // A 32 bit signed integer 
      #define OMAS_DT_REAL32  0x00000040 // A 32 bit floating point value (float, ) 
      #define OMAS_DT_REAL64  0x00000080 // A 64 bit floating point value (double, ) 
      #define OMAS_DT_RGB     0x00000400 // Byte RGB, 3 samples per pixel 
      #define OMAS_DT_RGB4    0x00000800 // Byte RGB, 4 samples per pixel. 
      #define OMAS_DT_UINT64  0x00001000 // A 64 bit unsigned integer 
      #define OMAS_DT_SINT64  0x00002000 // A 64 bit signed integer 
      #define OMAS_DT_BOOL    0x00010000 // A c++ boolean 
   
   Each of the numeric types has a complex counterpart by setting the following bit in :cppcode:`dt`:

   .. code-block:: cpp

      #define OMAS_DT_COMPLEX 0x40000000 // Is set, if this is a complex array. 
   
   So a stack containing :cppcode:`std::complex<float>` values would have 
   
   .. code-block:: cpp
   
      dt = OMAS_DT_REAL32|OMAS_DT_COMPLEX 

compression_type
   The type of compression used. Currently only the values {bf 0} (no compression) and {\bf 1} (ZIP compression)
   are supported.
compression_level
   The compression level used. This is whatever the library allows. For ZIP  compression
   the levels are 0 to 9 from fastest to strongest.
name_len
   The length in tytes of the UTF-8 encoded stack name following this header immediately.
descr_len
   The length in tytes of the UTF-8 encoded stack description following the name. 
reserved
   Out of use.
next_stack_pos
   Pointer to the location of the next stack header. 

For stacks with :cppcode:`format_version >= 1` the binary data is immediately followed by the
stack footer

.. code-block:: cpp

   //! Stack footer
   typedef struct _OBF_STACK_FOOTER
   {
      //! The total size until the variable sized parts (col_positions) start
      omas_UINT32 size;
      //! Entries are != 0 for all aces that have a pixel position array
      //! following.
      omas_UINT32 has_col_positions[OMAS_BF_MAX_DIMENSIONS];
      //! Entries are != 0 for all aces that have a label following
      omas_UINT32 has_col_labels[OMAS_BF_MAX_DIMENSIONS];
      //! Length of the metadata following the footer
      omas_UINT32 metadata_length;

      // The following is starting with stack version 2

      //! Si units of the value carried
      OBF_SI_UNIT si_value;
      //! Si units of the axes
      OBF_SI_UNIT si_dimensions[OMAS_MAX_DIMENSIONS];

      // The following is starting with stack version 3
      
      //! The number of flush points
      omas_UINT64 num_flush_points;
      //! The flush block size
      omas_UINT64 flush_block_size;
      
   } OBF_STACK_FOOTER;

where the :cppcode:`OBF_SI_UNIT` structure is defined as follows:

.. code-block:: cpp

   //! A fraction, ideally should be reduced when writing to file
   typedef struct _OBF_SI_FRACTION
   {
      omas_SINT32 numerator;
      omas_SINT32 denominator;

   } OBF_SI_FRACTION;

   //! The dimensions and scaling factor of an SI unit. For each of th base and supplemental
   //! units the exponent is saved as a fraction.
   //! Ordering for the exponents array is as follows:
   //! exponents[0]: Meters (M)
   //! exponents[1]: Kilograms (KG)
   //! exponents[2]: Seconds (S)
   //! exponents[3]: Amperes (A)
   //! exponents[4]: Kelvin (K)
   //! exponents[5]: Moles (MOL)
   //! exponents[6]: Candela (CD)
   //! exponents[7]: Radian (R)
   //! exponents[8]: Steradian (SR)
   typedef struct _OBF_SI_UNIT
   {
      OBF_SI_FRACTION exponents[9];
      double scalefactor;   

   } OBF_SI_UNIT;
   
  
The footer contains additional meta-information that is too large to be saved as a string and/or
is to be made available without the need for xml parsing. Future versions of the footer may become
larger so a read routine should always read the known members and then seek to a position 
:cppcode:`footer.size` bytes after its beginning before starting to read the variable sized parts of
the meta information. In detail:
The header members are

size
   The size of this structure on disk. Read the known part of the structure and 
   discard the :cppcode:`footer.size - sizeof(OBF_STACK_FOOTER)` bytes. This allows a reader
   written for a lower version to read stacks of a higher version simply omitting meta-data
   that has been added to the new version. 
   In case breaking changes will be introduced, the magic header will be changed and the
   changes will be described in this document.
has_col_positions
   For those dimensions for which :cppcode:`has_col_positions[i] != 0` an array of 
   :cppcode:`res[i]` (64bit) double values is appended after the label strings (see below) 
   which signify the position of the column along its axis. If present the :cppcode:`len! and \lstinline!off` 
   should be ignored in favor of the position values. 
has_col_labels
   For those dimensions for which :cppcode:`has_col_labels[i] != 0` an array of 
   :cppcode:`res[i]` label strings is appended after the column position arrays. Each label
   string starts in the form :cppcode:`(omas_UINT32)n:char[n]` where *n* is the length of 
   the string. It is thus read out by reading a 32bit integer *n* and then reading *n* bytes
   forming an UTF-8 encoded string.
metadata_length
   Immediately after the label strings a block of memory is appended which is a string in 
   UTF-8 format which contains meta-data interpreted on a higher level in the OmasIo 
   xml format for properties described elsewhere. This entails e.g. the stack position
   and orientation in a global coordinate system etc. As it becomes important some of 
   it may find its way into the obf specification appended to the header in a binary
   format.
   While you can use this field for your own meta-data this is not encouraged. The field
   is intended to be filled in a standard way that OBF readers may or may not read. Custom
   meta-data should be saved in the file and stack description fields, preferrably also
   in UTF-8 xml(see below).
   Nevertheless, readers should not throw or report a fatal error when they do not 
   understand the data contained in this field - they should issue a warning. 
si_value
   For The SI units of the stack values.
si_dimensions
   The SI units of the stack axes. 
num_flush_points
   For zip compressed stacks this is the number of full flush points the zlib compression
   has created for fast seeking. The flush point positions relative to the beginning of
   the zlib compressed data follow immediately after the meta data as an array 
   :cppcode:`omas_UINT64 flush_positions[num_flush_points]`. 
   When uncompressing only a window of the stack
   starting at :cppcode:`pos` the inflator may start decompressing data at the disk position
   :cppcode:`flush_positions[n]` where :cppcode:`n` is the largest integer with 
   :cppcode:`flush_block_size*n <= pos`. Please note that there is no ZLIB header
   written at that position, so the inflator needs to be initialized in 'raw' format
   i.e. inflateInit2(h, -15) needs to be called in zlib.
flush_block_size
   The number of (uncompressed) bytes between full flush points. See above.
   
The footer is immediately followed by :cppcode:`rank` label strings (encoded in the same form as the 
column labels) which are in turn followed by the column positions, column labels, meta data and
flush positions as outlined above.

.. note:: Backwards and forward compatibility:
   As outlined above, OBF files are designed to be backwards and forward compatible. Any 
   breaking change would be accompanied by a change of the magic header. Versions after such
   a change may introduce a different versioning scheme indicating forward compatible versions
   but both, breaking of the forward compatibility and such a change in philosophy are currently
   not being considered.
   
   Also, please note that while this is unintended behaviour the footer is allowed to grow without 
   a version jump. i.e. more data may follow or the size member may indicate that the footer 
   structure written is larger than expected for this version. This is no problem as long as
   its size member is used to find the beginning of the label strings.
   
.. note:: SI units
   While simply writing SI units as a string in a certain format would have been simpler and
   would have allowed to display the units directly in a simple reader (and have them written
   more easily after user input) this format was chosen as it allows bindings to existing
   units implementations i.e. in C/C++, Python and MATLAB more easily. 
   
   For C/C++ OmasIo contains a simple formatter and parser for unit strings into this format.
   

The DBL File Format *(deprecated)*
-----------------------------------

The DBL format is a simple binary file containing a single up to four-dimensional data stack with some 
header information about physical dimensions of the sampled a volume. The header is exactly 
128 bytes long

.. code-block:: cpp

   unsigned char header[128];

For historical reasons it  has an mixed little endian and big endian format. 
The rank of the stack is not explicitly contained but the pixel number of 
higher dimensions are simply set to 1. 
The number of pixels along the four possible dimensions
are given by 

.. code-block:: cpp

   res[2] = header[0]*256 + header[1];
   res[1] = header[2]*256 + header[3];
   res[0] = header[4]*256 + header[5];
   res[3] = header[6]*256 + header[7];

The physical length is 

.. code-block:: cpp

   len[2] = *((float *) (header +  8);
   len[1] = *((float *) (header + 12);
   len[0] = *((float *) (header + 16);
   len[3] = *((float *) (header + 20);

where the floats are stored in little endian format. Reading on big endian machines involves
flipping bytes before casting to float. The header is followed by floating point data in little endian
byte order. If :cppcode:`header[24] == 1` it is 32bit floating point (float), otherwise it is 
64bit floating point data (double).


The OmasIo API, Bindings
------------------------
The **OmasIo** library implements the OBF and DBL file format providing both a C++ 
interface to OBF files. There are bindings using the C++ implementation for both MATLAB
and Python and in addition, a pure JAVA implementation of a reader is in the process
of becoming part of `BioFormats <http://loci.wisc.edu/software/bio-formats/>`_.

.. note:: 
   All .msr files written by Imspector conform to the OBF specification. Additional
   information is stored between the stacks and before the first stack but any .msr file
   (except for very, very old ones) should be readable by a correctly implemented OBF
   reader. 
   
   Vice versa, Imspector reads .obf files. Because OBF is forward and backwards compatible
   this comes in handy when opening .msr files from newer versions of Imspector (as .msr
   is not forward compatible). 

Meta information data model
-----------------------------

Strictly speaking, the OBF file format does not specify the way meta information is to be 
associated with the file or data stacks within and because it can be embedded into 
arbitrary, more complex formats it even encourages the use of methods suitable for 
the task at hand.

For meta information that is to be shared by several applications it is however strongly 
encouraged that meta-information is saved as UTF-8 text in the file or stack 
description, preferably formatted as xml in a way compatible to the output of the 
:cppcode:`omas_export_xml()` function in the *OmasIo* library, described in a seperate 
section. In C++, the easiest way to do this is to write the meta information into an 
:cppcode:`OProp` object and actually use the :cppcode:`omas_export_xml()` function 
to convert it to an xml string. For MATLAB and Python, toolboxes are provided that 
can convert a (complex) variable into a compatible xml string and back. In fact these 
toolboxes, too first map the data into an  :cppcode:`OProp` variable and then export 
it to xml and vice versa.

The  :cppcode:`OProp` data model is strongly based on the MATLAB data model. Data is
organized in arrays of arbitrary numeric complex or real data type and arbitrary rank 
(with the special case of a scalar, which is a 1x1 array in MATLAB), cell arrays (where 
each cell can contain data of a different type), structs (where each member is 
addressed by its name and can contain arbitrary data) and arrays of structs (with identical 
fields). In MATLAB strings are one-dimensional character arrays. MALAB string arrays  
therefore will always contain strings of equal length (with shorter strings simply padded
by NULL bytes). The toolbox will convert these to cell arrays of strings tagged with
a special flag. On the C++ side they will look like cell arrays of strings but as long
as the tag is untouched they will be converted back to string arrays on the MATLAB side.
Please note that usually it is preferrable to use cell arrays of strings on the MATLAB
side to start with. Also, :cppcode:`OProp` knows empty 'cells' (an :cppcode:`OProp` with 
no content) which is mapped to an empty 'double' array in MATLAB.
There are similar mapping issues with other bindings like Python. The general Ansatz is
that variables converted to xml by one language binding will produce the same variable
when read back directly but that there is no guarantee that this applies once a property
tree has been converted back and forth between different languages. 