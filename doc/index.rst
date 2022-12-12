.. image:: wsy-web-15/wsy_web_customize_title/static/description/assets/image/logo_long.png
   :target: https://weasydoo.com/en_US/
   :alt: WEASYDOO
   :scale: 100 %
   :align: center

==========================
 WSY CUSTOMIZE TITLE
==========================
Set up REST API and export OpenAPI (Swagger) specification file for integration
with whatever system you need. All can be configured in Odoo UI, no extra module
is needed.

This module implements a ``/api/v1/`` route tree.

Authentication
==============

* Database inference: Database name encoded and appended to the token
* User authentication through the actual token

As a workaround for multi-db Odoo instances, system uses `Basic Authentication <https://swagger.io/docs/specification/2-0/authentication/basic-authentication/>`__ with
``db_name:token`` credentials, where ``token`` is a new field in ``res.users``
model. That is, whenever you see Username / Password to setup OpenAPI
connection, use Database Name / OpenAPI toekn accordingly.

Roadmap
=======

* TODO: Rewrite tests to replace dependency ``mail`` to ``web`` module.
* TODO: Add a button to developer menu to grant access to current model

    * `Activate Developer Mode <https://odoo-development.readthedocs.io/en/latest/odoo/usage/debug-mode.html>`__
    * Open the developer tools drop down
    * Click menu ``Configure REST API`` located within the dropdown
    * On the form that opens, activate and configure this module for REST API accessability.
    * Click ``[Apply]``

* TODO: when user is not authenticated api returns 200 with the message below, instead of designed 401

  ::

    File "/opt/odoo/vendor/it-projects-llc/sync-addons/openapi/controllers/pinguin.py", line 152, in authenticate_token_for_user
        raise werkzeug.exceptions.HTTPException(response=error_response(*CODE__no_user_auth))
    HTTPException: ??? Unknown Error: None

* TODO: ``wrap__resource__create_one`` method makes ``cr.commit()``. We need to avoid that.
* TODO: add code examples for other programming languages in index.html. The examples can be based on generated swagger clients. The idea of the scripts must be the same as for python (search for partner, create if it doesn't exist, send message)
* TODO: use sudo for log creating and disable write access rights
* TODO: finish unitttests (see ``test_api.py``)
* TODO: ``.../swagger.json`` url doesn't work in multi-db mode in odoo 12.0 at least: it make strange redirection to from ``/api/v1/demo/swagger.json?token=demo_token&db=source`` to ``/api/v1/demo/swagger.json?token%3Ddemo_token%26db%3Dsource``
* TODO: remove access to create logs and use sudo (SUPERUSER_ID)  instead. It prevents making fake logs by malicous user
* TODO: Check that swagger specification and module documentaiton covers how to pass context to method calls

Questions?
==========

To get an assistance on this module contact us by email wehearyou@weasydoo.com

Contributors
============
* `Abdelhak LARBI CHERIF <abdelhak.larbi@weasydoo.com>`__

===================

Website: `WEASYDOO <https://weasydoo.com/en_US/>`_


Notifications on updates: `by Email <https://blogtrottr.com/?subscribe=https://github.com/itpp-labs/sync-addons/commits/15.0/openapi.atom>`_

Tested on `Odoo 15.0 `
