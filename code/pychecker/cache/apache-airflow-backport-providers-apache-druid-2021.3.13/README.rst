
.. Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at

..   http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.


Package ``apache-airflow-providers-microsoft-azure``

Release: ``1.2.0``


`Microsoft Azure <https://azure.microsoft.com/>`__


Provider package
================

This is a provider package for ``microsoft.azure`` provider. All classes for this provider package
are in ``airflow.providers.microsoft.azure`` python package.

You can find package information and changelog for the provider
in the `documentation <https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/1.2.0/>`_.


Installation
============

NOTE!

On November 2020, new version of PIP (20.3) has been released with a new, 2020 resolver. This resolver
does not yet work with Apache Airflow and might lead to errors in installation - depends on your choice
of extras. In order to install Airflow you need to either downgrade pip to version 20.2.4
``pip install --upgrade pip==20.2.4`` or, in case you use Pip 20.3, you need to add option
``--use-deprecated legacy-resolver`` to your pip install command.

You can install this package on top of an existing airflow 2.* installation via
``pip install apache-airflow-providers-microsoft-azure``

PIP requirements
================

================================  ==================
PIP package                       Version required
================================  ==================
``azure-batch``                   ``>=8.0.0``
``azure-cosmos``                  ``>=3.0.1,<4``
``azure-datalake-store``          ``>=0.0.45``
``azure-identity``                ``>=1.3.1``
``azure-keyvault``                ``>=4.1.0``
``azure-kusto-data``              ``>=0.0.43,<0.1``
``azure-mgmt-containerinstance``  ``>=1.5.0,<2.0``
``azure-mgmt-datafactory``        ``>=1.0.0,<2.0``
``azure-mgmt-datalake-store``     ``>=0.5.0``
``azure-mgmt-resource``           ``>=2.2.0``
``azure-storage-blob``            ``>=12.7.0``
``azure-storage-common``          ``>=2.1.0``
``azure-storage-file``            ``>=2.1.0``
================================  ==================

Cross provider package dependencies
===================================

Those are dependencies that might be needed in order to use all the features of the package.
You need to install the specified backport providers package in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

.. code-block:: bash

    pip install apache-airflow-providers-microsoft-azure[google]


====================================================================================================  ==========
Dependent package                                                                                     Extra
====================================================================================================  ==========
`apache-airflow-providers-google <https://airflow.apache.org/docs/apache-airflow-providers-google>`_  ``google``
`apache-airflow-providers-oracle <https://airflow.apache.org/docs/apache-airflow-providers-oracle>`_  ``oracle``
====================================================================================================  ==========