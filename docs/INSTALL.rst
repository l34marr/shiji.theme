Installation
------------

To install shiji.theme using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``shiji.theme`` to the list of eggs to install::

    [buildout]
    ...
    eggs =
        ...
        shiji.theme

* Re-run buildout::

    $ ./bin/buildout

* Restart the Zope server::

    $ ./bin/instance restart

Then activate 'ShiJi Theme' in Plone (Site Setup -> Add-ons).

