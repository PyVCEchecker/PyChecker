Using :mod:`zope.i18nmessageid`
===============================

Rationale
---------

To translate any text, we must be able to discover the source domain
of the text.  A source domain is an identifier that identifies a
project that produces program source strings.  Source strings occur as
literals in python programs, text in templates, and some text in XML
data.  The project implies a source language and an application
context.

Messages and Domains
--------------------

We can think of a source domain as a collection of messages and
associated translation strings.  The domain helps to disambiguate messages
based on context:  for instance, the message whose source string is ``draw``
means one thing in a first-person shooter game, and quite another in a
graphics package:  in the first case, the domain for the message might
be ``ok_corral``, while in the second it might be ``gimp``.

We often need to create unicode strings that will be displayed by
separate views.  The view cannot translate the string without knowing
its source domain.  A string or unicode literal carries no domain
information, therefore we use instances of the
:class:`~zope.i18nmessageid.message.Message` class.  Messages are unicode
strings which carry a translation source domain and possibly a default
translation.

Message Factories
-----------------

Messages are created by a message factory belonging to a given translation
domain. Each message factory is created by instantiating a
:class:`~zope.i18nmessageid.message.MessageFactory`, passing the domain
corresponding to the project which manages the corrresponding translations.

.. doctest::

  >>> from zope.i18nmessageid import MessageFactory
  >>> factory = MessageFactory('myproject')
  >>> foo = factory('foo')
  >>> foo.domain
  'myproject'

The Zope project uses the ``zope`` domain for its messages.  This package
exports an already-created factory for that domain:

.. doctest::

  >>> from zope.i18nmessageid import ZopeMessageFactory as _z_
  >>> foo = _z_('foo')
  >>> foo.domain
  'zope'


Example Usage
-------------

In this example, we create a message factory and assign it to _.  By
convention, we use _ as the name of our factory to be compatible with
translatable string extraction tools such as xgettext.  We then call _
with a string that needs to be translatable:

.. doctest::

  >>> from zope.i18nmessageid import MessageFactory, Message
  >>> _ = MessageFactory("futurama")
  >>> robot = _(u"robot-message", u"${name} is a robot.")

Messages at first seem like they are unicode strings:

.. doctest::

  >>> robot == u'robot-message'
  True
  >>> isinstance(robot, unicode)
  True

The additional domain, default and mapping information is available
through attributes:

.. doctest::

  >>> robot.default == u'${name} is a robot.'
  True
  >>> robot.mapping
  >>> robot.domain
  'futurama'

The message's attributes are considered part of the immutable message
object.  They cannot be changed once the message id is created:

.. doctest::

  >>> robot.domain = "planetexpress"
  Traceback (most recent call last):
  ...
  TypeError: readonly attribute

  >>> robot.default = u"${name} is not a robot."
  Traceback (most recent call last):
  ...
  TypeError: readonly attribute

  >>> robot.mapping = {u'name': u'Bender'}
  Traceback (most recent call last):
  ...
  TypeError: readonly attribute

If you need to change their information, you'll have to make a new
message id object:

.. doctest::

  >>> new_robot = Message(robot, mapping={u'name': u'Bender'})
  >>> new_robot == u'robot-message'
  True
  >>> new_robot.domain
  'futurama'
  >>> new_robot.default == u'${name} is a robot.'
  True
  >>> new_robot.mapping == {u'name': u'Bender'}
  True

Last but not least, messages are reduceable for pickling:

.. doctest::

  >>> callable, args = new_robot.__reduce__()
  >>> callable is Message
  True
  >>> args == (u'robot-message',
  ...          'futurama',
  ...          u'${name} is a robot.',
  ...          {u'name': u'Bender'},
  ...          None,
  ...          None,
  ...          None)
  True

  >>> fembot = Message(u'fembot')
  >>> callable, args = fembot.__reduce__()
  >>> callable is Message
  True
  >>> args == (u'fembot', None, None, None, None, None, None)
  True

Pickling and unpickling works, which means we can store message IDs in
a database:

.. doctest::

   >>> from pickle import dumps, loads
   >>> pystate = dumps(new_robot)
   >>> pickle_bot = loads(pystate)
   >>> (pickle_bot,
   ...  pickle_bot.domain,
   ...  pickle_bot.default,
   ...  pickle_bot.mapping) == (u'robot-message',
   ...                          'futurama',
   ...                          u'${name} is a robot.',
   ...                          {u'name': u'Bender'})
   True
   >>> pickle_bot.__reduce__()[0] is Message
   True
