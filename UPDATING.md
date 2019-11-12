# Updating automatically generated pages

Some of the website pages are automatically generated using the
[document_sopel_plugins.py](document_sopel_plugins.py) and
[document_versions.py](document_versions.py) scripts in the root of this
repository, and the Sphinx Makefile included with Sopel's docs.

For website deploys, the [Netlify build script](netlify-build.sh) handles all
of that automatically. There's no need to manually update anything after
releasing a new version of Sopel; updating the commit that the `_sopel`
submodule points to is sufficient.

The plugin-doc script is very old. It has been updated to mostly-working
condition, but it cannot document plugin configuration options any more due to
changes in how the standard `configure()` method works. This function would be
nice to have back, of course, so any help fixing it for current plugin code is
much appreciated! (For the moment, we're embedding Markdown tables in
docstrings in the plugin code, which is… kludgy, but it works for now.)


## Manual guide

Preferably, the scripts should be run under a version of Python 3 that Sopel
supports. If your `python` points to an old version, substitute `python3` or
whatever name is appropriate for your system.

All example commands are run from the root of the local `sopel.chat` repo,
except where otherwise noted.

Changelog generation will "just work" using whatever entries exist in the
`_sopel` submodule:

    python document_versions.py

or you can manually point it to a NEWS file that lives elsewhere:

    python document_versions.py --news=/path/to/NEWS

Clean up the generated changelog files if needed with:

    python document_versions.py --clean

The plugin-doc script expects that `sopel` is at least installed globally,
even if the installed version is not the latest release, so that it can open
plugin files without import errors.

If Sopel is stored in (from this repo's perspective) `../sopel`, just run:

    python document_sopel_plugins.py

If Sopel's code is stored elsewhere, use the `--sopel` argument like so:

    python document_sopel_plugins.py --sopel=/path/to/sopel/repo

This script also supports cleaning up after itself:

    python document_sopel_plugins.py --clean

Finally, the `/docs/` folder is built with Sphinx from `_sopel/docs`:

    cd _sopel/docs
    make html
    mv build/html ../../_site/docs

Jekyll might wipe this depending on how you test locally, but you can probably
just trust that the site deployment will get the API docs right and not worry
about them too much when testing.
