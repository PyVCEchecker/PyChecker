=============
requests-mock
=============

.. _requests-mock_1.9.2:

1.9.2
=====

.. _requests-mock_1.9.2_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/Fix-urlquote-of-quoted-path-84cc1ff122dba279.yaml @ b'77f1a1fef7a6bb60b1ad4bafb85159782474178d'

- As part of 1.9.0 we started quoting unsafe URL characters. This was done incorrectly that meant we requoted existing quoted strings. Fixes


.. _requests-mock_1.9.1:

1.9.1
=====

.. _requests-mock_1.9.1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/Add-py.typed-file-5a5cae1041dd0859.yaml @ b'78ef2d0a377355d5e0a20e6eeb6c8333f3bdf17c'

- A py.typed file is required to enable type annotations for the package. Add to pack for re-release.


.. _requests-mock_1.9.0:

1.9.0
=====

.. _requests-mock_1.9.0_New Features:

New Features
------------

.. releasenotes/notes/Support-Type-Hints-0f7d2385bd808d84.yaml @ b'402fd627cc28f76f6938c17848c6c88ff58863c0'

- Add python type hints for python 3.


.. _requests-mock_1.9.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-zero-bytes-read-109628b72221cfe7.yaml @ b'91bb753d62c8788d0ed72292d5e1f37ed1a365e0'

- Issue 144 - When performing a read we handled an empty byte return as an indication to close the file pointer. This is not true when you actually ask for a zero byte read so we should allow it.

.. releasenotes/notes/url-quote-path-a593190dee974a7a.yaml @ b'f072845c0cb13c6c0fb18824160639a8bb3c7fe8'

- Fix [#148](https://github.com/jamielennox/requests-mock/issues/158). When you have a non url-safe character in your URL it is quoted by requests however requests-mock just treated it as a normal string.


.. _requests-mock_1.8.0:

1.8.0
=====

.. _requests-mock_1.8.0_Prelude:

Prelude
-------

.. releasenotes/notes/explicit-nesting-behaviour-4d28c310dc4c463a.yaml @ b'b99eef22c5603dae28e35018166d95b40731ec7c'

Makes explicit the behaviour of nested mocking.


.. _requests-mock_1.8.0_New Features:

New Features
------------

.. releasenotes/notes/add-reset-function-bcef01162cab0912.yaml @ b'aeca73aeb57752315a5b6cd123b00a24e81f8c39'

- Add a reset/reset_mock function to the mocker and components so that users
  can clear the calls and history from the Mocker without clearing all the
  matching that has been used.

.. releasenotes/notes/explicit-nesting-behaviour-4d28c310dc4c463a.yaml @ b'b99eef22c5603dae28e35018166d95b40731ec7c'

- Nested mocks now has a defined behaviour which is essentially a classic
  nesting behaviour. A mock works as normal, but in the same way that
  real_http=True will escalate to the outer send (typically the real send) if
  there is a mocker defined outside that will handle the calls.

.. releasenotes/notes/session-scoped-mock-7f1c98d9a91bffc8.yaml @ b'35bfe56591f188dd169bad64b612688e55ec552c'

- Allow mocking of only a single Session object. While there has always been
  the option of adding just the Adapter to an existing Session, this is more
  difficult to work with than the Mocker workflow that is typically used. You
  can now pass a Session object to a Mocker and it will provide the standard
  workflow but limited to just that object.

.. releasenotes/notes/set-default-response-reason-f24556261bc7e9e5.yaml @ b'c2d3d248798087c6cf44e60f69679276e7a797c0'

- When creating a response we now default the reason string to the appropriate string based on the status code. This can still be provided manually.

.. releasenotes/notes/set-real-http-on-mocker-01eb26b65697466d.yaml @ b'5788dcf191728e384a73f7dee100f482dfb79a7e'

- Make real_http variable on Mocker object public. This means you can change
  the value of the parameter after the object has been created. This will
  allow setting it in situations like pytest where you may not be able to set
  __init__ time options.


.. _requests-mock_1.8.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/explicit-nesting-behaviour-4d28c310dc4c463a.yaml @ b'b99eef22c5603dae28e35018166d95b40731ec7c'

- This fixes all known nesting bugs. They may not be perfect, however this is
  now the explicit defined behaviour and so all related bugs are closed in
  favour of this.

.. releasenotes/notes/fix-iter-content-none-1e29754a75273b8c.yaml @ b'7a5fc638b606507a9a1dd2dc88e95df87dd2baa7'

- 124 when using `response.iter_content(None)` the iterator would keep returning b'' and never finish. In most code paths the b'' would indicate that the stream is finished, but using None we have to close it ourselves.


.. _requests-mock_1.7.0:

1.7.0
=====

.. _requests-mock_1.7.0_New Features:

New Features
------------

.. releasenotes/notes/match-empty-query-string-e6d6976fe002da0b.yaml @ b'9210dfc1c831c4afdd698dcd9ac637ee36019439'

- You can now match on the empty query string value like `/path?a`.


.. _requests-mock_1.7.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/pin-requests-version-e0f090aa31dc86c3.yaml @ b'1e2d0904f85e7987fa4b33429a2f80f156e997cf'

- Pins version of requests to <3 to prepare for new release of requests in future.


.. _requests-mock_1.6.0:

1.6.0
=====

.. _requests-mock_1.6.0_Prelude:

Prelude
-------

.. releasenotes/notes/Bump-minimum-requests-2.3-70fd287f6ea1a12e.yaml @ b'3a7c98f63d625f675c36df27724148fbe75f50a6'

Increase the minimum required requests version to 2.3


.. _requests-mock_1.6.0_Critical Issues:

Critical Issues
---------------

.. releasenotes/notes/Bump-minimum-requests-2.3-70fd287f6ea1a12e.yaml @ b'3a7c98f63d625f675c36df27724148fbe75f50a6'

- The minimum version of requests has been increase to 2.3. This simply
  ensures that all documented features of requests-mock are actually
  available. This version of requests is still quite old and if this is an
  issue you should either pin requests-mock to <1.6 or preferably update
  requests.


.. _requests-mock_1.6.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/Allow-pickling-response-fe751b0a760a5001.yaml @ b'a0e8fb61e0bcadb85b0dcb1ea3b7a5d029821ee8'

- Remove weakref objects from the request/response that will allow the objects to be pickled with the regular python mechanisms.

.. releasenotes/notes/user-response-encoding-b2eea39404140164.yaml @ b'f4f3b0a631a76b73bc08757a6b78055e5a7d6835'

- If you specified a charset in the Content-Type of a response it would be
  ignored and overriden with either 'utf-8' or None depending on the type of
  response content passed in. If you pass this value we should honour it and
  perform the encoding correctly.


.. _requests-mock_1.5.2:

1.5.2
=====

.. _requests-mock_1.5.2_Prelude:

Prelude
-------

.. releasenotes/notes/py.test-2-4e7735793288ea2d.yaml @ b'acce6240de329869ef87efaf43560f4a6dfeafcd'

Fix py.test plugin with py.test < 3.0


.. _requests-mock_1.5.2_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-pytest-version-discovery-43f27e7e162ed055.yaml @ b'4909eac4a72a052b20eff76900f470fae1d328fd'

- Fixed a bug relating to how the pytest version was being discovered that meant new versions of pytest were being treated as old versions and would receive bad configuration.

.. releasenotes/notes/py.test-2-4e7735793288ea2d.yaml @ b'acce6240de329869ef87efaf43560f4a6dfeafcd'

- The py.test plugin was broken when using py.test < 3.0. The version of py.test that ships in EPEL is only 2.7 so we need to make sure we support at least that version.


.. _requests-mock_1.5.1:

1.5.1
=====

.. _requests-mock_1.5.1_New Features:

New Features
------------

.. releasenotes/notes/request-history-stream-f1d75b33adcd7e97.yaml @ b'7c82b5294f24989ef934dac8f4c58ab20b42103c'

- The stream parameter is recorded when the request is sent and available in request history in the same was as parameters like verify or timeout.


.. _requests-mock_1.5.0:

1.5.0
=====

.. _requests-mock_1.5.0_Prelude:

Prelude
-------

.. releasenotes/notes/repo-move-15e956e1d54c048b.yaml @ b'33d9cc8468f89063934a58c08eb9d04e09aae895'

The primary repository is now at https://github.com/jamielennox/requests-mock


.. _requests-mock_1.5.0_New Features:

New Features
------------

.. releasenotes/notes/pytest-7e35da8c5f2cd428.yaml @ b'a455a735d7edba5d064380eb054021a11d076f57'

- Added pytest fixture for native integration into pytest projects.


.. _requests-mock_1.5.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/repo-move-15e956e1d54c048b.yaml @ b'33d9cc8468f89063934a58c08eb9d04e09aae895'

- In this release the main repository was moved off of OpenStack provided
  infrastructure and onto github at
  https://github.com/jamielennox/requests-mock. OpenStack has been a great
  home for the project however requests-mock is a general python project with
  no specific relationship to OpenStack and the unfamiliar infrastructure was
  limiting contributes from the wider community.


.. _requests-mock_1.3.0:

1.3.0
=====

.. _requests-mock_1.3.0_New Features:

New Features
------------

.. releasenotes/notes/additional-matcher-5c5cd466a6d70080.yaml @ b'aa3e87c4ee8da57b0b71f0a9511af89002a7aa1e'

- Allow specifying an `additional_matcher` to the mocker that will call a function to allow a user to add their own custom request matching logic.


.. _requests-mock_1.1.0:

1.1.0
=====

.. _requests-mock_1.1.0_Prelude:

Prelude
-------

.. releasenotes/notes/Add-called_once-property-a69546448cbd5542.yaml @ b'0c6e567ec77681178e461c2994db16fa81aea4a8'

Add a called_once property to the mockers.


.. releasenotes/notes/case-insensitive-matching-a3143221359bbf2d.yaml @ b'1b08dcc70557b2d58c56a923e6d3176c2b64a14f'

It is now possible to make URL matching and request history not lowercase the provided URLs.


.. releasenotes/notes/fixture-extras-699a5b5fb5bd6aab.yaml @ b'6df03ed3d03d05f606bff28764e72bc0574333b7'

Installing the requirements for the 'fixture' contrib package can now be done via pip with `pip install requests-mock[fixture]`


.. _requests-mock_1.1.0_New Features:

New Features
------------

.. releasenotes/notes/Add-called_once-property-a69546448cbd5542.yaml @ b'0c6e567ec77681178e461c2994db16fa81aea4a8'

- A called_once property was added to the adapter and the mocker. This gives us an easy way to emulate mock's assert_called_once.

.. releasenotes/notes/case-insensitive-matching-a3143221359bbf2d.yaml @ b'1b08dcc70557b2d58c56a923e6d3176c2b64a14f'

- You can pass case_sensitive=True to an adapter or set `requests_mock.mock.case_sensitive = True` globally to enable case sensitive matching.

.. releasenotes/notes/fixture-extras-699a5b5fb5bd6aab.yaml @ b'6df03ed3d03d05f606bff28764e72bc0574333b7'

- Added 'fixture' to pip extras so you can install the fixture requirements with `pip install requests-mock[fixture]`


.. _requests-mock_1.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/case-insensitive-matching-a3143221359bbf2d.yaml @ b'1b08dcc70557b2d58c56a923e6d3176c2b64a14f'

- It is recommended you add `requests_mock.mock.case_sensitive = True` to your base test file to globally turn on case sensitive matching as this will become the default in a 2.X release.


.. _requests-mock_1.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/case-insensitive-matching-a3143221359bbf2d.yaml @ b'1b08dcc70557b2d58c56a923e6d3176c2b64a14f'

- Reported in bug \#1584008 all request matching is done in a case insensitive way, as a byproduct of this request history is handled in a case insensitive way. This can now be controlled by setting case_sensitive to True when creating an adapter or globally.

