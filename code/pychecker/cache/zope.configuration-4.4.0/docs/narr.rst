===========================
 Zope configuration system
===========================

The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some
language that express configuration choices. The intent is that the
language be pluggable.  An XML language is provided by default.

Configuration is performed in three stages. In the first stage,
directives are processed to compute configuration actions.
Configuration actions consist of:

- A discriminator

- A callable

- Positional arguments

- Keyword arguments

The actions are essentially delayed function calls.  Two or more
actions conflict if they have the same discriminator.  The
configuration system has rules for resolving conflicts. If conflicts
cannot be resolved, an error will result.  Conflict resolution
typically discards all but one of the conflicting actions, so that
the remaining action of the originally-conflicting actions no longer
conflicts.  Non-conflicting actions are executed in the order that
they were created by passing the positional and non-positional
arguments to the action callable.

The system is extensible. There is a meta-configuration language for
defining configuration directives. A directive is defined by
providing meta data about the directive and handler code to process
the directive.  There are four kinds of directives:

- Simple directives compute configuration actions.  Their handlers
  are typically functions that take a context and zero or more
  keyword arguments and return a sequence of configuration actions.

  To learn how to create simple directives, see ``tests/simple.py``.


- Grouping directives collect information to be used by nested
  directives. They are called with a context object which they adapt
  to some interface that extends IConfigurationContext.

  To learn how to create grouping directives, look at the
  documentation for :mod:`zope.configuration.zopeconfigure`, which
  provides the implementation of the zope ``configure`` directive.

  Other directives can be nested in grouping directives.

  To learn how to implement nested directives, look at the
  documentation in the "Creating Nested Directives" section below.

- Complex directives are directives that have subdirectives.
  Subdirectives have handlers that are simply methods of complex
  directives. Complex diretives are handled by factories, typically
  classes, that create objects that have methods for handling
  subdirectives. These objects also have __call__ methods that are
  called when processing of subdirectives is finished.

  Complex directives only exist to support old directive
  handlers. They will probably be deprecated in the future.

- Subdirectives are nested in complex directives. They are like
  simple directives except that they hane handlers that are complex
  directive methods.

  Subdirectives, like complex directives only exist to support old
  directive handlers. They will probably be deprecated in the future.

.. todo::
   Flesh out narrative docs.

Using the configuration machinery programatically
=================================================

An extended example:

.. doctest::

   >>> from zope.configuration.config import ConfigurationMachine
   >>> from zope.configuration.config import metans
   >>> machine = ConfigurationMachine()
   >>> ns = "http://www.zope.org/testing"

Register some test directives:

Start with a grouping directive that sets a package:

.. doctest::

   >>> machine((metans, "groupingDirective"),
   ...         name="package", namespace=ns,
   ...         schema="zope.configuration.tests.directives.IPackaged",
   ...         handler="zope.configuration.tests.directives.Packaged",
   ...         )

Now we can set the package:

.. doctest::

   >>> machine.begin((ns, "package"),
   ...               package="zope.configuration.tests.directives",
   ...               )

Which makes it easier to define the other directives:

First, define some simple directives:

.. doctest::

   >>> machine((metans, "directive"),
   ...         namespace=ns, name="simple",
   ...         schema=".ISimple", handler=".simple")

   >>> machine((metans, "directive"),
   ...         namespace=ns, name="newsimple",
   ...         schema=".ISimple", handler=".newsimple")


and try them out:

.. doctest::

   >>> machine((ns, "simple"), "first", a=u"aa", c=u"cc")
   >>> machine((ns, "newsimple"), "second", a=u"naa", c=u"ncc", b=u"nbb")

   >>> from pprint import PrettyPrinter
   >>> pprint = PrettyPrinter(width=48).pprint

   >>> pprint(machine.actions)
   [{'args': ('aa', 'xxx', 'cc'),
     'callable': f,
     'discriminator': ('simple',
                       'aa',
                       'xxx',
                       'cc'),
     'includepath': (),
     'info': 'first',
     'kw': {},
     'order': 0},
    {'args': ('naa', 'nbb', 'ncc'),
     'callable': f,
     'discriminator': ('newsimple',
                       'naa',
                       'nbb',
                       'ncc'),
     'includepath': (),
     'info': 'second',
     'kw': {},
     'order': 0}]

Define and try a simple directive that uses a component:

.. doctest::

   >>> machine((metans, "directive"),
   ...         namespace=ns, name="factory",
   ...         schema=".IFactory", handler=".factory")


   >>> machine((ns, "factory"), factory=u".f")
   >>> pprint(machine.actions[-1:])
   [{'args': (),
     'callable': f,
     'discriminator': ('factory', 1, 2),
     'includepath': (),
     'info': None,
     'kw': {},
     'order': 0}]

Define and try a complex directive:

.. doctest::

   >>> machine.begin((metans, "complexDirective"),
   ...               namespace=ns, name="testc",
   ...               schema=".ISimple", handler=".Complex")

   >>> machine((metans, "subdirective"),
   ...         name="factory", schema=".IFactory")

   >>> machine.end()

   >>> machine.begin((ns, "testc"), None, "third", a=u'ca', c='cc')
   >>> machine((ns, "factory"), "fourth", factory=".f")

Note that we can't call a complex method unless there is a directive for
it:

.. doctest::

   >>> machine((ns, "factory2"), factory=".f")
   Traceback (most recent call last):
   ...
   ConfigurationError: ('Invalid directive', 'factory2')


   >>> machine.end()
   >>> pprint(machine.actions)
   [{'args': ('aa', 'xxx', 'cc'),
     'callable': f,
     'discriminator': ('simple',
                       'aa',
                       'xxx',
                       'cc'),
     'includepath': (),
     'info': 'first',
     'kw': {},
     'order': 0},
    {'args': ('naa', 'nbb', 'ncc'),
     'callable': f,
     'discriminator': ('newsimple',
                       'naa',
                       'nbb',
                       'ncc'),
     'includepath': (),
     'info': 'second',
     'kw': {},
     'order': 0},
    {'args': (),
     'callable': f,
     'discriminator': ('factory', 1, 2),
     'includepath': (),
     'info': None,
     'kw': {},
     'order': 0},
    {'args': (),
     'callable': None,
     'discriminator': 'Complex.__init__',
     'includepath': (),
     'info': 'third',
     'kw': {},
     'order': 0},
    {'args': ('ca',),
     'callable': f,
     'discriminator': ('Complex.factory', 1, 2),
     'includepath': (),
     'info': 'fourth',
     'kw': {},
     'order': 0},
    {'args': ('xxx', 'cc'),
     'callable': f,
     'discriminator': ('Complex', 1, 2),
     'includepath': (),
     'info': 'third',
     'kw': {},
     'order': 0}]

Done with the package

.. doctest::

   >>> machine.end()


Verify that we can use a simple directive outside of the package:

.. doctest::

   >>> machine((ns, "simple"), a=u"oaa", c=u"occ", b=u"obb")

But we can't use the factory directive, because it's only valid
inside a package directive:

.. doctest::

   >>> machine((ns, "factory"), factory=u".F")
   Traceback (most recent call last):
   ...
   ConfigurationError: ('Invalid value for', 'factory',""" \
      """ "Can't use leading dots in dotted names, no package has been set.")

   >>> pprint(machine.actions)
   [{'args': ('aa', 'xxx', 'cc'),
     'callable': f,
     'discriminator': ('simple',
                       'aa',
                       'xxx',
                       'cc'),
     'includepath': (),
     'info': 'first',
     'kw': {},
     'order': 0},
    {'args': ('naa', 'nbb', 'ncc'),
     'callable': f,
     'discriminator': ('newsimple',
                       'naa',
                       'nbb',
                       'ncc'),
     'includepath': (),
     'info': 'second',
     'kw': {},
     'order': 0},
    {'args': (),
     'callable': f,
     'discriminator': ('factory', 1, 2),
     'includepath': (),
     'info': None,
     'kw': {},
     'order': 0},
    {'args': (),
     'callable': None,
     'discriminator': 'Complex.__init__',
     'includepath': (),
     'info': 'third',
     'kw': {},
     'order': 0},
    {'args': ('ca',),
     'callable': f,
     'discriminator': ('Complex.factory', 1, 2),
     'includepath': (),
     'info': 'fourth',
     'kw': {},
     'order': 0},
    {'args': ('xxx', 'cc'),
     'callable': f,
     'discriminator': ('Complex', 1, 2),
     'includepath': (),
     'info': 'third',
     'kw': {},
     'order': 0},
    {'args': ('oaa', 'obb', 'occ'),
     'callable': f,
     'discriminator': ('simple',
                       'oaa',
                       'obb',
                       'occ'),
     'includepath': (),
     'info': None,
     'kw': {},
     'order': 0}]


Overriding Included Configuration
=================================

When we have conflicting directives, we can resolve them if one of
the conflicting directives was from a file that included all of
the others.  The problem with this is that this requires that all
of the overriding directives be in one file, typically the
top-most including file. This isn't very convenient.  Fortunately,
we can overcome this with the includeOverrides directive. Let's
look at an example to see how this works.

Look at the file ``bar.zcml`` (in ``zope/configuration/tests/samplepackage``):

- It includes ``bar1.zcml`` and ``bar2.zcml``.

- ``bar1.zcml`` includes ``configure.zcml`` and has a ``foo``
  directive.

- ``bar2.zcml`` includes ``bar21.zcml``, and has a ``foo``
  directive that conflicts with one in ``bar1.zcml``.

- ``bar2.zcml`` also overrides a foo directive in ``bar21.zcml``.

- ``bar21.zcml`` has a ``foo`` directive that conflicts with one in in
  ``configure.zcml``. Whew!

Let's see what happens when we try to process ``bar.zcml``.

.. doctest::

   >>> import os
   >>> from zope.configuration.config import ConfigurationMachine
   >>> from zope.configuration.xmlconfig import include
   >>> from zope.configuration.xmlconfig import registerCommonDirectives
   >>> context = ConfigurationMachine()
   >>> registerCommonDirectives(context)

   >>> from zope.configuration.tests import __file__
   >>> here = os.path.dirname(__file__)
   >>> path = os.path.join(here, "samplepackage", "bar.zcml")
   >>> include(context, path)

So far so good, let's look at the configuration actions:

.. doctest::

   >>> from zope.configuration.tests.test_xmlconfig import clean_actions
   >>> pprint = PrettyPrinter(width=73).pprint
   >>> pprint(clean_actions(context.actions))
   [{'discriminator': (('x', b'blah'), ('y', 0)),
     'includepath': ['tests/samplepackage/bar.zcml',
                     'tests/samplepackage/bar1.zcml',
                     'tests/samplepackage/configure.zcml'],
     'info': 'File "tests/samplepackage/configure.zcml", line 12.2-12.29'},
    {'discriminator': (('x', b'blah'), ('y', 1)),
     'includepath': ['tests/samplepackage/bar.zcml',
                     'tests/samplepackage/bar1.zcml'],
     'info': 'File "tests/samplepackage/bar1.zcml", line 5.2-5.24'},
    {'discriminator': (('x', b'blah'), ('y', 0)),
     'includepath': ['tests/samplepackage/bar.zcml',
                     'tests/samplepackage/bar2.zcml',
                     'tests/samplepackage/bar21.zcml'],
     'info': 'File "tests/samplepackage/bar21.zcml", line 3.2-3.24'},
    {'discriminator': (('x', b'blah'), ('y', 2)),
     'includepath': ['tests/samplepackage/bar.zcml',
                     'tests/samplepackage/bar2.zcml',
                     'tests/samplepackage/bar21.zcml'],
     'info': 'File "tests/samplepackage/bar21.zcml", line 4.2-4.24'},
    {'discriminator': (('x', b'blah'), ('y', 2)),
     'includepath': ['tests/samplepackage/bar.zcml',
                     'tests/samplepackage/bar2.zcml'],
     'info': 'File "tests/samplepackage/bar2.zcml", line 5.2-5.24'},
    {'discriminator': (('x', b'blah'), ('y', 1)),
     'includepath': ['tests/samplepackage/bar.zcml',
                     'tests/samplepackage/bar2.zcml'],
     'info': 'File "tests/samplepackage/bar2.zcml", line 6.2-6.24'}]

As you can see, there are a number of conflicts (actions with the same
discriminator).  Some of these can be resolved, but many can't, as
we'll find if we try to execuse the actions:

.. doctest::

   >>> from zope.configuration.config import ConfigurationConflictError
   >>> from zope.configuration.tests.test_xmlconfig import clean_text_w_paths
   >>> try:
   ...    v = context.execute_actions()
   ... except ConfigurationConflictError as e:
   ...    v = e
   >>> print(clean_text_w_paths(str(v)))
   Conflicting configuration actions
     For: (('x', b'blah'), ('y', 0))
       File "tests/samplepackage/configure.zcml", line 12.2-12.29
           <test:foo x="blah" y="0" />
       File "tests/samplepackage/bar21.zcml", line 3.2-3.24
           <foo x="blah" y="0" />
     For: (('x', b'blah'), ('y', 1))
       File "tests/samplepackage/bar1.zcml", line 5.2-5.24
           <foo x="blah" y="1" />
       File "tests/samplepackage/bar2.zcml", line 6.2-6.24
           <foo x="blah" y="1" />

Note that the conflicts for (('x', 'blah'), ('y', 2)) aren't
included in the error because they could be resolved.

Let's try this again using includeOverrides.  We'll include
baro.zcml which includes bar2.zcml as overrides.

.. doctest::

   >>> context = ConfigurationMachine()
   >>> registerCommonDirectives(context)
   >>> path = os.path.join(here, "samplepackage", "baro.zcml")
   >>> include(context, path)

Now, if we look at the actions:

.. doctest::

   >>> pprint(clean_actions(context.actions))
   [{'discriminator': (('x', b'blah'), ('y', 0)),
     'includepath': ['tests/samplepackage/baro.zcml',
                     'tests/samplepackage/bar1.zcml',
                     'tests/samplepackage/configure.zcml'],
     'info': 'File "tests/samplepackage/configure.zcml", line 12.2-12.29'},
    {'discriminator': (('x', b'blah'), ('y', 1)),
     'includepath': ['tests/samplepackage/baro.zcml',
                     'tests/samplepackage/bar1.zcml'],
     'info': 'File "tests/samplepackage/bar1.zcml", line 5.2-5.24'},
    {'discriminator': (('x', b'blah'), ('y', 0)),
     'includepath': ['tests/samplepackage/baro.zcml'],
     'info': 'File "tests/samplepackage/bar21.zcml", line 3.2-3.24'},
    {'discriminator': (('x', b'blah'), ('y', 2)),
     'includepath': ['tests/samplepackage/baro.zcml'],
     'info': 'File "tests/samplepackage/bar2.zcml", line 5.2-5.24'},
    {'discriminator': (('x', b'blah'), ('y', 1)),
     'includepath': ['tests/samplepackage/baro.zcml'],
     'info': 'File "tests/samplepackage/bar2.zcml", line 6.2-6.24'}]

We see that:

- The conflicting actions between bar2.zcml and bar21.zcml have
  been resolved, and

- The remaining (after conflict resolution) actions from bar2.zcml
  and bar21.zcml have the includepath that they would have if they
  were defined in baro.zcml and this override the actions from
  bar1.zcml and configure.zcml.

We can now execute the actions without problem, since the
remaining conflicts are resolvable:

.. doctest::

   >>> context.execute_actions()

We should now have three entries in foo.data:

.. doctest::

   >>> from zope.configuration.tests.samplepackage import foo
   >>> from zope.configuration.tests.test_xmlconfig import clean_info_path
   >>> len(foo.data)
   3

   >>> data = foo.data.pop(0)
   >>> data.args
   (('x', b'blah'), ('y', 0))
   >>> print(clean_info_path(repr(data.info)))
   File "tests/samplepackage/bar21.zcml", line 3.2-3.24

   >>> data = foo.data.pop(0)
   >>> data.args
   (('x', b'blah'), ('y', 2))
   >>> print(clean_info_path(repr(data.info)))
   File "tests/samplepackage/bar2.zcml", line 5.2-5.24

   >>> data = foo.data.pop(0)
   >>> data.args
   (('x', b'blah'), ('y', 1))
   >>> print(clean_info_path(repr(data.info)))
   File "tests/samplepackage/bar2.zcml", line 6.2-6.24


We expect the exact same results when using includeOverrides with
the ``files`` argument instead of the ``file`` argument.  The
baro2.zcml file uses the former:

.. doctest::

   >>> context = ConfigurationMachine()
   >>> registerCommonDirectives(context)
   >>> path = os.path.join(here, "samplepackage", "baro2.zcml")
   >>> include(context, path)

Actions look like above:

.. doctest::

   >>> pprint(clean_actions(context.actions))
   [{'discriminator': (('x', b'blah'), ('y', 0)),
     'includepath': ['tests/samplepackage/baro2.zcml',
                     'tests/samplepackage/bar1.zcml',
                     'tests/samplepackage/configure.zcml'],
     'info': 'File "tests/samplepackage/configure.zcml", line 12.2-12.29'},
    {'discriminator': (('x', b'blah'), ('y', 1)),
     'includepath': ['tests/samplepackage/baro2.zcml',
                     'tests/samplepackage/bar1.zcml'],
     'info': 'File "tests/samplepackage/bar1.zcml", line 5.2-5.24'},
    {'discriminator': (('x', b'blah'), ('y', 0)),
     'includepath': ['tests/samplepackage/baro2.zcml'],
     'info': 'File "tests/samplepackage/bar21.zcml", line 3.2-3.24'},
    {'discriminator': (('x', b'blah'), ('y', 2)),
     'includepath': ['tests/samplepackage/baro2.zcml'],
     'info': 'File "tests/samplepackage/bar2.zcml", line 5.2-5.24'},
    {'discriminator': (('x', b'blah'), ('y', 1)),
     'includepath': ['tests/samplepackage/baro2.zcml'],
     'info': 'File "tests/samplepackage/bar2.zcml", line 6.2-6.24'}]

   >>> context.execute_actions()
   >>> len(foo.data)
   3
   >>> del foo.data[:]



Making specific directives conditional
======================================

There is a ``condition`` attribute in the
"http://namespaces.zope.org/zcml" namespace which is honored on all
elements in ZCML.  The value of the attribute is an expression
which is used to determine if that element and its descendents are
used.  If the condition evaluates to true, processing continues normally;
otherwise that element and its descendents are ignored.

The expression is always of the form "*verb* *arguments*". There are
four verbs that are supported:

- have
- not-have
- installed
- not-installed

Note that logical "if/else" conditions can be achieved by using both the
positive verb and its not-prefixed counterpart on sibling elements
with the same arguments. Logical "and" conditions can be achieved by
nesting elements. To group arbitrary directives under a condition,
nest them under a new ``<configure>`` element.

.. seealso:: :meth:`zope.configuration.xmlconfig.ConfigurationHandler.evaluateCondition`

   For documentation and examples of the XML implementation of conditions.

Features
--------

The verbs ``have`` and ``not-have`` test for the presence or absence
of features in the configuration context. The argument is a single
feature name. Features can be established in Python code using
:meth:`~zope.configuration.config.ConfigurationContext.provideFeature`,
or they can be set during ZCML processing with the ``meta:provides``
directive (e.g., ``<meta:provides feature="featurename" />``.)

A popular use of features is to enable certain configuration only
during development with a feature called ``devmode``. (This also
demonstrates applying a condition to a single directive.)

.. code-block:: xml

   <configure
      xmlns="http://namespaces.zope.org/zope"
      xmlns:zcml="http://namespaces.zope.org/zcml" >
      <include package="." file="devconfig.zcml" zcml:condition="have devmode" />
   </configure>

Module Availability
-------------------

The verbs ``installed`` and ``not-installed`` test whether a Python
module can be imported successfully or not. They can be used to enable
optional configuration if a package is present, or enable fallback
functionality if it isn't. (This also demonstrates grouping directives
under a new ``<configure>`` element, and establishing a logical "if/else".)

.. code-block:: xml

   <configure
      xmlns="http://namespaces.zope.org/zope"
      xmlns:zcml="http://namespaces.zope.org/zcml" >

      <configure zcml:condition="installed some.package">
          <!-- Use it -->
          <include package="some.package" />
      </configure>
      <configure zcml:condition="not-installed some-package">
          <!-- Enable our fallback code -->
          <adapter for=".ISomeInterface"
                   provides=".ISomeFunction"
                   factory=".MockFunction" />
      </configure>
   </configure>


Example
-------

Our demonstration uses a trivial registry; each registration consists
of a simple id inserted in the global ``registry`` in this module.  We
can checked that a registration was made by checking whether the id is
present in ``registry``.

.. doctest::

   >>> from zope.configuration.tests.conditions import registry
   >>> registry
   []

We start by loading the example ZCML file, *conditions.zcml*:

.. literalinclude:: ../src/zope/configuration/tests/conditions.zcml
   :language: xml

.. doctest::

  >>> import zope.configuration.tests
  >>> from zope.configuration.xmlconfig import file
  >>> context = file("conditions.zcml", zope.configuration.tests)

To show that our sample directive works, we see that the unqualified
registration was successful:

.. doctest::

  >>> "unqualified.registration" in registry
  True

When the expression specified with ``zcml:condition`` evaluates to
true, the element it is attached to and all contained elements (not
otherwise conditioned) should be processed normally:

.. doctest::

  >>> "direct.true.condition" in registry
  True
  >>> "nested.true.condition" in registry
  True

However, when the expression evaluates to false, the conditioned
element and all contained elements should be ignored:

.. doctest::

  >>> "direct.false.condition" in registry
  False
  >>> "nested.false.condition" in registry
  False

Conditions on container elements affect the conditions in nested
elements in a reasonable way.  If an "outer" condition is true, nested
conditions are processed normally:

.. doctest::

  >>> "true.condition.nested.in.true" in registry
  True
  >>> "false.condition.nested.in.true" in registry
  False

If the outer condition is false, inner conditions are not even
evaluated, and the nested elements are ignored:

.. doctest::

  >>> "true.condition.nested.in.false" in registry
  False
  >>> "false.condition.nested.in.false" in registry
  False

.. testcleanup::

  del registry[:]


Filtering and Inhibiting Configuration
======================================

The ``exclude`` standard directive is provided for inhibiting unwanted
configuration. It is used to exclude processing of configuration files.
It is useful when including a configuration that includes some other
configuration that you don't want.

It must be used BEFORE including the files to be excluded.

First, let's look at an example.  The zope.configuration.tests.excludedemo
package has a ZCML configuration that includes some other configuration files.

We'll set a log handler so we can see what's going on:

.. doctest::

   >>> import logging
   >>> import logging.handlers
   >>> import sys
   >>> logger = logging.getLogger('config')
   >>> oldlevel = logger.level
   >>> logger.setLevel(logging.DEBUG)
   >>> handler = logging.handlers.MemoryHandler(10)
   >>> logger.addHandler(handler)

Now, we'll include the zope.configuration.tests.excludedemo config:

.. doctest::

   >>> from zope.configuration.xmlconfig import string
   >>> _ = string('<include package="zope.configuration.tests.excludedemo" />')
   >>> len(handler.buffer)
   3
   >>> logged = [x.getMessage() for x in handler.buffer]
   >>> logged[0].startswith('include ')
   True
   >>> logged[0].endswith('zope/configuration/tests/excludedemo/configure.zcml')
   True
   >>> logged[1].startswith('include ')
   True
   >>> logged[1].endswith('zope/configuration/tests/excludedemo/sub/configure.zcml')
   True
   >>> logged[2].startswith('include ')
   True
   >>> logged[2].endswith('zope/configuration/tests/excludedemo/spam.zcml')
   True
   >>> del handler.buffer[:]

Each run of the configuration machinery runs with fresh state, so
rerunning gives the same thing:

.. doctest::

   >>> _ = string('<include package="zope.configuration.tests.excludedemo" />')
   >>> len(handler.buffer)
   3
   >>> logged = [x.getMessage() for x in handler.buffer]
   >>> logged[0].startswith('include ')
   True
   >>> logged[0].endswith('zope/configuration/tests/excludedemo/configure.zcml')
   True
   >>> logged[1].startswith('include ')
   True
   >>> logged[1].endswith('zope/configuration/tests/excludedemo/sub/configure.zcml')
   True
   >>> logged[2].startswith('include ')
   True
   >>> logged[2].endswith('zope/configuration/tests/excludedemo/spam.zcml')
   True
   >>> del handler.buffer[:]

Now, we'll use the exclude directive to exclude the two files included
by the configuration file in zope.configuration.tests.excludedemo:

.. doctest::

   >>> _ = string(
   ... '''
   ... <configure  xmlns="http://namespaces.zope.org/zope">
   ...   <exclude package="zope.configuration.tests.excludedemo.sub" />
   ...   <exclude package="zope.configuration.tests.excludedemo" file="spam.zcml" />
   ...   <include package="zope.configuration.tests.excludedemo" />
   ... </configure>
   ... ''')
   >>> len(handler.buffer)
   1
   >>> logged = [x.getMessage() for x in handler.buffer]
   >>> logged[0].startswith('include ')
   True
   >>> logged[0].endswith('zope/configuration/tests/excludedemo/configure.zcml')
   True


.. testcleanup::

   logger.setLevel(oldlevel)
   logger.removeHandler(handler)


Creating simple directives
==========================

A simple directive is a directive that doesn't contain other
directives. It can be implemented via a fairly simple function.
To implement a simple directive, you need to do 3 things:

- You need to create a schema to describe the directive parameters,

- You need to write a directive handler, and

- You need to register the directive.

In this example, we'll implement a contrived example that records
information about files in a file registry. The file registry is just
the list, ``file_registry``.

.. doctest::

   >>> from zope.configuration.tests.simple import file_registry

Our registry will contain tuples with:

  - file path

  - file title

  - description

  - Information about where the file was defined

Our schema is defined in ``zope.configuration.tests.simple.IRegisterFile``
(q.v).

.. doctest::

   >>> from zope.configuration.tests.simple import IRegisterFile

Our schema lists the ``path`` and ``title`` attributes.  We'll get the
description and other information for free, as we'll see later.  The
title is not required, and may be omitted.

The job of a configuration handler is to compute one or more
configuration actions.  Configuration actions are defered function
calls. The handler doesn't perform the actions. It just computes
actions, which may be performed later if they are not overridden by
other directives.

Our handler is given in the function,
``zope.configuration.tests.simple.registerFile``.

.. doctest::

   >>> from zope.configuration.tests.simple import registerFile


It takes a context, a path and a title. All directive handlers take the
directive context as the first argument.  A directive context, at a minimim,
implements, ``zope.configuration.IConfigurationContext``.
(Specialized contexts can implement more specific interfaces. We'll say more
about that when we talk about grouping directives.)  The title argument
must have a default value, because we indicated that the title was not
required in the schema. (Alternatively, we could have made the title
required, but provided a default value in the schema.

In the first line of function ``registerFile``, we get the context information
object. This object contains information about the configuration
directive, such as the file and location within the file of the
directive.

The context information object also has a text attribute that contains
the textual data contained by the configuration directive. (This is
the concatenation of all of the xml text nodes directly contained by
the directive.)  We use this for our description in the second line
of the handler.

The last thing the handler does is to compute an action by calling the
action method of the context.  It passes the action method 3 keyword
arguments:

- discriminator

  The discriminator is used to identify the action to be performed so
  that duplicate actions can be detected.  Two actions are duplicated,
  and this conflict, if they have the same discriminator values and
  the values are not ``None``.  Conflicting actions can be resolved if
  one of the conflicting actions is from a configuration file that
  directly or indirectly includes the files containing the other
  conflicting actions.

  In function ``registerFile``, we a tuple with the string
  ``'RegisterFile'`` and the path to be registered.

- callable

  The callable is the object to be called to perform the action.

- args

  The args argument contains positinal arguments to be passed to the
  callable. In function ``registerFile``, we pass a tuple containing a
  ``FileInfo`` object.

  (Note that there's nothing special about the FileInfo class. It has
   nothing to do with creating simple directives. It's just used in
   this example to organize the application data.)


The final step in implementing the simple directive is to register
it. We do that with the zcml ``meta:directive`` directive.  This is
given in the file simple.zcml.  Here we specify the name, namespace,
schema, and handler for the directive.  We also provide a
documentation for the directive as text between the start and end
tags.

The file simple.zcml also includes some directives that use the new
directive to register some files.

Now let's try it all out:

.. doctest::

   >>> from zope.configuration import tests
   >>> from zope.configuration.xmlconfig import file
   >>> context = file("simple.zcml", tests)

Now we should see some file information in the registry:

.. doctest::

   >>> from zope.configuration.tests.test_xmlconfig import clean_text_w_paths
   >>> from zope.configuration.tests.test_xmlconfig import clean_path
   >>> print(clean_path(file_registry[0].path))
   tests/simple.py
   >>> print(file_registry[0].title)
   How to create a simple directive
   >>> print(file_registry[0].description)
   Describes how to implement a simple directive
   >>> print(clean_text_w_paths(file_registry[0].info))
   File "tests/simple.zcml", line 19.2-24.2
       <files:register
           path="simple.py"
           title="How to create a simple directive"
           >
         Describes how to implement a simple directive
       </files:register>
   >>> print(clean_path(file_registry[1].path))
   tests/simple.zcml
   >>> print(file_registry[1].title)
   <BLANKLINE>
   >>> desc = file_registry[1].description
   >>> print('\n'.join([l.rstrip()
   ...                  for l in desc.strip().splitlines()
   ...                    if l.rstrip()]))
   Shows the ZCML directives needed to register a simple directive.
       Also show some usage examples,
   >>> print(clean_text_w_paths(file_registry[1].info))
   File "tests/simple.zcml", line 26.2-30.2
       <files:register path="simple.zcml">
         Shows the ZCML directives needed to register a simple directive.
         Also show some usage examples,
       </files:register>
   >>> print(clean_path(file_registry[2].path))
   tests/__init__.py
   >>> print(file_registry[2].title)
   Make this a package
   >>> print(file_registry[2].description)
   <BLANKLINE>
   >>> print(clean_text_w_paths(file_registry[2].info))
   File "tests/simple.zcml", line 32.2-32.67
       <files:register path="__init__.py" title="Make this a package" />

Clean up after ourselves:

.. doctest::

   >>> del file_registry[:]



Creating nested directives
==========================

When using ZCML, you sometimes nest ZCML directives. This is typically
done either to:

- Avoid repetative input.  Information shared among multiple
  directives is provided in a surrounding directive.

- Put together information that is too complex or structured to express
  with a single set of directive parameters.

Grouping directives are used to handle both of these cases.  See the
documentation in :mod:`zope.configuration.zopeconfigure`. This file describes the
implementation of the zope ``configure`` directive, which groups
directives that use a common package or internationalization domain.
You should also have read the section on "Creating simple directives."

This file shows you how to handle the second case above. In this case,
we have grouping directives that are meant to collaborate with
specific contained directives.  To do this, you have the grouping
directives declare a more specific (or alternate) interface to
``IConfigurationContext``. Directives designed to work with those
grouping directives are registered for the new interface.

Let's look at example. Suppose we wanted to be able to define schema
using ZCML.  We'd use a grouping directive to specify schemas and
contained directives to specify fields within the schema.  We'll use a
schema registry to hold the defined schemas::

.. doctest::

   >>> from zope.configuration.tests.nested import schema_registry

A schema has a name, an id, some documentation, and some fields.
We'll provide the name and the id as parameters. We'll define fields
as subdirectives and documentation as text contained in the schema
directive.  The schema directive uses the schema, ``ISchemaInfo`` for
it's parameters.

.. doctest::

   >>> from zope.configuration.tests.nested import ISchemaInfo

We also define the schema, ISchema, that specifies an attribute that
nested field directives will use to store the fields they define.

.. doctest::

   >>> from zope.configuration.tests.nested import ISchema

The class, ``Schema``, provides the handler for the schema directive. (If
you haven't read the documentation in ``zopeconfigure.py``, you need
to do so now.)  The constructor saves its arguments as attributes
and initializes its ``fields`` attribute:

.. doctest::

   >>> from zope.configuration.tests.nested import Schema

The ``after`` method of the ``Schema`` class creates a schema and
computes an action to register the schema in the schema registry.  The
discriminator prevents two schema directives from registering the same
schema.

It's important to note that when we call the ``action`` method on
``self``, rather than on ``self.context``.  This is because, in a
grouping directive handler, the handler instance is itself a context.
When we call the ``action`` method, the method stores additional meta
data associated with the context it was called on. This meta data
includes an include path, used when resolving conflicting actions,
and an object that contains information about the XML source used
to invole the directive. If we called the action method on
``self.context``, the wrong meta data would be associated with the
configuration action.

The file ``schema.zcml`` contains the meta-configuration directive
that defines the schema directive.

To define fields, we'll create directives to define the fields.
Let's start with a ``text`` field.  ``ITextField`` defines the schema for
text field parameters. It extends ``IFieldInfo``, which defines data
common to all fields.  We also define a simple handler method,
textField, that takes a context and keyword arguments. (For
information on writing simple directives, see ``test_simple.py``.)
We've abstracted most of the logic into the function ``field``.

The ``field`` function computes a field instance using the
constructor, and the keyword arguments passed to it.  It also uses the
context information object to get the text content of the directive,
which it uses for the field description.

After computing the field instance, it gets the ``Schema`` instance,
which is the context of the context passed to the function. The
function checks to see if there is already a field with that name. If
there is, it raises an error. Otherwise, it saves the field.

We also define an ``IIntInfo`` schema and ``intField`` handler
function to support defining integer fields.

We register the ``text`` and ``int`` directives in ``schema.zcml``.
These are like the simple directive definition we saw in
``test_simple.py`` with an important exception.  We provide a
``usedIn`` parameter to say that these directives can *only* ne used
in a ``ISchema`` context. In other words, these can only be used
inside of ``schema`` directives.

The ``schema.zcml`` file also contains some sample ``schema``
directives.  We can execute the file:

.. doctest::

   >>> from zope.configuration import tests
   >>> from zope.configuration.xmlconfig import file
   >>> context = file("schema.zcml", tests)

And verify that the schema registery has the schemas we expect:

.. doctest::

   >>> pprint(sorted(schema_registry))
   ['zope.configuration.tests.nested.I1',
    'zope.configuration.tests.nested.I2']

   >>> def sorted(x):
   ...     r = list(x)
   ...     r.sort()
   ...     return r

   >>> i1 = schema_registry['zope.configuration.tests.nested.I1']
   >>> sorted(i1)
   ['a', 'b']
   >>> i1['a'].__class__.__name__
   'Text'
   >>> i1['a'].description.strip()
   'A\n\n          Blah blah'
   >>> i1['a'].min_length
   1
   >>> i1['b'].__class__.__name__
   'Int'
   >>> i1['b'].description.strip()
   'B\n\n          Not feeling very creative'
   >>> i1['b'].min
   1
   >>> i1['b'].max
   10

   >>> i2 = schema_registry['zope.configuration.tests.nested.I2']
   >>> sorted(i2)
   ['x', 'y']


Now let's look at some error situations. For example, let's see what
happens if we use a field directive outside of a schema dorective.
(Note that we used the context we created above, so we don't have to
redefine our directives:

.. doctest::

   >>> from zope.configuration.xmlconfig import string
   >>> from zope.configuration.exceptions import ConfigurationError
   >>> v = string(
   ...      '<text xmlns="http://sample.namespaces.zope.org/schema" name="x" />',
   ...      context)
   Traceback (most recent call last):
   ...
   zope.configuration.exceptions.ConfigurationError: The directive ('http://sample.namespaces.zope.org/schema', 'text') cannot be used in this context
     File "<string>", line 1.0


Let's see what happens if we declare duplicate fields:

.. doctest::

   >>> try:
   ...    v = string(
   ...      '''
   ...      <schema name="I3" id="zope.configuration.tests.nested.I3"
   ...              xmlns="http://sample.namespaces.zope.org/schema">
   ...        <text name="x" />
   ...        <text name="x" />
   ...      </schema>
   ...      ''',
   ...      context)
   ... except ConfigurationError as e:
   ...   v = e
   >>> print(v)
   File "<string>", line 5.7-5.24
       ValueError: ('Duplicate field', 'x')
