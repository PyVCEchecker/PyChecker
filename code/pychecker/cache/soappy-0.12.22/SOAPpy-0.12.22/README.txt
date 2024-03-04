==============================================
SOAPpy - Simple to use SOAP library for Python
==============================================

.. contents::

Disclaimer
==========
Please use `suds <https://pypi.python.org/pypi/suds>`_ rather than SOAPpy.
SOAPpy is old and clamsy.

Credits
========

Companies
---------
|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

Authors
------------

- Cayce Ullman <c_ullman@yahoo.com>
- Brian Matthews <blm@blmatthews.com>
- Gregory R. Warnes <Gregory.R.Warnes@Pfizer.com>
- Makina Corpus <python@makina-corpus.com>
- Mathieu Le Marec - Pasquet <kiorky@cryptelium.net>

Contributors
----------------
- Christopher Blunck <blunck2@gst.com>
- Brad Knotwell <b.knotwell@f5.com>
- Mark Bucciarelli <mark@hubcapconsulting.com> (ported WSDL client from ZSI)
- Ivan R. Judson     <judson@mcs.anl.gov> (Globus support)
- Kirk Strauser <kirk@daycos.com>
- Antonio Beamud Montero <antonio.beamud@linkend.com> (patches for integrating SOAPpy into Zope)
- And others.

Copyright (c) 20011 Makina Corpus
Copyright (c) 2002-2005, Pfizer, Inc.
Copyright (c) 2001, Cayce Ullman.
Copyright (c) 2001, Brian Matthews.
All rights reserved, see the file LICENSE for conditions of use.

INTRODUCTION
==============

The goal of the SOAPpy team is to provide a full-featured SOAP library
for Python that is very simple to use and that fully supports dynamic
interaction between clients and servers.


INCLUDED
--------
- General SOAP Parser based on sax.xml
- General SOAP Builder
- SOAP Proxy for RPC client code
- SOAP Server framework for RPC server code

FEATURES
--------
- Handles all SOAP 1.0 types
- Handles faults
- Allows namespace specification
- Allows SOAPAction specification
- Homogeneous typed arrays
- Supports multiple schemas
- Header support (mustUnderstand and actor)
- XML attribute support
- Multi-referencing support (Parser/Builder)
- Understands SOAP-ENC:root attribute
- Good interop, passes all client tests for Frontier, SOAP::LITE, SOAPRMI
- Encodings
- SSL clients (with Python compiled with OpenSSL support)
- SSL servers (with Python compiled with OpenSSL support and M2Crypto installed)
- Encodes XML tags per SOAP 1.2 name mangling specification (Gregory Warnes)
- Automatic stateful SOAP server support (Apache v2.x) (blunck2)
- WSDL client support
- WSDL server support

TODO (See RELEASE_INFO and CHANGELOG for recent changes)
----------------------------------------------------------
- Timeout on method calls
- Advanced arrays (sparse, multidimensional and partial)
- Attachments
- mod_python example
- medusa example
- Improved documentation

MANIFEST
--------
::

    Files

        README              This file
        RELEASE_NOTES       General information about each release
        ChangeLog           Detailed list of changes
        TODO                List of tasks that need to be done
        setup.py            Python installation control files
        SOAPpy.spec         RPM package control file

    Directories

        SOAPpy/            Source code for the package
        SOAPpy/wstools/    Source code for WSDL tools
        tests/             unit tests and examples
        validate/          interop client and servers
        bid/               N+I interop client and server
        contrib/           Contributed examples (also see test/)
        docs/              Documentation
        tools/             Misc tools useful for the SOAPpy developers
        zope/              Patches to Zope allowing it to provide SOAP services


INSTALLATION
============

USING GITHUB
------------

    You can install SOAPpy and its dependencies directly from GitHub using PIP:

        pip install -e "git+http://github.com/kiroky/SOAPpy.git@develop#egg=SOAPpy"

REQUIRED PACKAGES
------------------

    - wstools


OPTIONAL PACKAGES
-----------------

    - pyGlobus, optional support for Globus,
      <http://www-itg.lbl.gov/gtg/projects/pyGlobus/>

    - M2Crypto.SSL, optional support for server-side SSL
      <http://sandbox.rulemaker.net/ngps/m2/>

    - If Python is compiled with SSL support (Python 2.3 does so by
      default), client-side use of SSL is supported

INSTALLATION STEPS
------------------

    As of version 0.9.8 SOAPpy can be installed using the standard python
    package installation tools.

    To install:

      1) Unpack the distribution package:

         On Windows, use your favorite zip file uncompression tool.

         On Unix::

             $ tar -xvzf SOAPpy-$VERSION$.tar.gz

         If you have gnu tar, otherwise
            ::

             $ gzcat SOAPpy-$VERSION$.tar.gz | tar -xvf -

      2) Change into the source directory
         ::

                 cd SOAPpy-$VERSION$

      3) Compile the package::

                $ python setup.py build

      4) Install the package

         On Windows::

                $ python setup.py install

         On Unix install as the owner of the python directories
         (usally root)::

                $ su root
                Password: XXXXXX
                $ python setup.py install


DOCUMENTATION
=============
QUICK START
-----------

A simple "Hello World" http SOAP server::

        import SOAPpy
        def hello():
            return "Hello World"
        server = SOAPpy.SOAPServer(("localhost", 8080))
        server.registerFunction(hello)
        server.serve_forever()

And the corresponding client::

        import SOAPpy
        server = SOAPpy.SOAPProxy("http://localhost:8080/")
        print server.hello()

BASIC TUTORIAL
--------------
Mark Pilgrims _Dive Into Python, published in printed form by
Apress and online at at http://diveintopython.org provides a
nice tutorial for SOAPpy in Chapter 12, "SOAP Web Services".
See http://diveintopython.org/soap_web_services .

OTHER DOCUMENTATION
-------------------

For further information see the files in the docs/ directory.

Note that documentation is one of SOAPpy's current weak points.
Please help us out!


Support
============
Github: https://github.com/kiorky/SOAPpy
Issues: https://github.com/kiorky/SOAPpy/issues

