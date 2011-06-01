Django Git Revision
###################

**Django Git Revision** is django application that allows use git last head commit hexstring in views and templates.

.. contents::

Requirements
============

- python >= 2.5
- django >= 1.2
- gitpython


Installation
============

**Django Git Revision** should be installed using pip_: ::

    pip install django-gitrevision


Setup and use
=============

#. Add `gitrevision` to INSTALLED_APPS: ::

        INSTALLED_APPS += 'gitrevision',

#. If you want use git revision **only in templates** add gitrevision context processor in settings: ::

        TEMPLATE_CONTEXT_PROCESSORS += 'gitrevision.context_processors.gitrevision',

   And use `GIT_REVISION` var in templates: ::

        ...
        <script src="/test.js?{{ GIT_REVISION }}"></script>
        ...

#. Or if you want use git revision in **views and templates**, add gitrevision middleware in settings: ::

        MIDDLEWARE_CLASSES += 'gitrevision.middleware.GitRevision',

   Using in views: ::

        def superview( request ):
            git_revision = request.git_revision
            ...

   Using in templates (with requestcontext): ::

        ...
        <script src="/test.js?{{ request.git_revision }}"></script>
        ...

#. Maybe you be needed append **GIT_PATH** in django settings: ::

    GIT_PATH = <path_to_your_git_repository>


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/django-gitrevision/issues


Contributing
============

Development of django-gitrevision happens at github: https://github.com/klen/django-gitrevision


Contributors
=============

* klen_ (Kirill Klenov)


License
=======

Licensed under a `GNU lesser general public license`_.


Copyright
=========

Copyright (c) 2011 Kirill Klenov (horneds@gmail.com)


.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _pip: http://www.pip-installer.org/en/latest/
.. _klen: https://github.com/klen
