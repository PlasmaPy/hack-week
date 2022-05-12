.. currentmodule:: hack

.. _glossary:

********
Glossary
********

.. glossary::
   :sorted:

   args
      An abbreviation for `positional arguments`_.

   keyword-only
      An |argument| or |parameter| is *keyword-only* when the |argument|
      must be provided with the name of the corresponding |parameter|.

      If ``z`` is a keyword-only |parameter| to ``f(z)``, then the
      |argument| ``2`` can be provided as ``f(z=2)`` but not ``f(2)``.

   kwargs
      An abbreviation for `keyword arguments`_.

.. |argument| replace:: :term:`argument`
.. |parameter| replace:: :term:`parameter`

.. _`keyword arguments`: https://docs.python.org/3/glossary.html#term-argument
.. _`positional arguments`: https://docs.python.org/3/glossary.html#term-argument
