#!/usr/bin/env python3
"""
Sopel plugin documentation utility
This script creates (either Markdown or reST) files, documenting the commands
and plugin configuration options in a Sopel instance.

Copyright 2012 Edward Powell, embolalia.net
Copyright 2019 dgw, technobabbl.es
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
import argparse
import inspect
import operator
import os
import imp
import sys
try:
    import sopel
except:
    print ("Sopel isn't installed globally. You may have problems.")


def main(argv=None):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    config_vals_file = os.path.join(this_dir, '_usage/plugin-configuration.md')
    commands_file = os.path.join(this_dir, '_usage/commands.md')

    parser = argparse.ArgumentParser(
        description="Sopel plugin documentation utility",
        usage='%(prog)s [options]'
        )
    parser.add_argument(
        '--sopel',
        dest='sopel_root',
        nargs='?',
        help="Specify the location of Sopel's code.",
        default=os.path.join(os.path.dirname(this_dir), 'sopel')
        )
    parser.add_argument(
        '--clean',
        action='store_true',
        help="Clean up the generated page files."
        )

    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    if args.clean:
        print("Cleaning up generated plugin documentation...")
        os.remove(config_vals_file)
        os.remove(commands_file)
        return

    print("Generating plugin docs using Sopel from " + args.sopel_root)
    print("...")
    os.sys.path.insert(0, args.sopel_root)

    filenames = []
    plugins_dir = os.path.join(args.sopel_root, 'sopel', 'modules')

    for fn in os.listdir(plugins_dir):
        if fn.endswith('.py') and not fn.startswith('_'):
            filenames.append(os.path.join(plugins_dir, fn))

    filenames.sort()

    filenames.append(os.path.join(args.sopel_root, 'sopel', 'coretasks.py'))

    commands = []

    with open(config_vals_file, 'w', encoding='utf8') as f:
        f.write(inspect.cleandoc("""\
        ---
        title: Plugin configuration
        order: 5
        previously:
          - /usage/module-configuration/
        ---

        This page contains documentation for all plugins within Sopel's main
        plugins directory. If you have added plugins without rebuilding the
        documentation, or are using a secondary plugins directory, those
        plugins will not be shown here.

        ## Plugins
        """))
        for filename in filenames:
            c = document_plugin(filename, f)
            if c:
                commands.extend(c)

    with open(commands_file, 'w', encoding='utf8') as f:
        f.write(inspect.cleandoc("""\
        ---
        title: Plugin commands
        order: 10
        ---

        This page contains a list of all commands from plugins within Sopel's
        main plugins directory. If you have added plugins without rebuilding
        the documentation, or are using a secondary plugins directory, those
        plugins will not be shown here.
        """))
        f.write("\n\n| Command(s) | Purpose | Example | Plugin |\n")
        f.write("| ---------- | ------- | ------- | ------ |\n")
        for c in commands:
            process_command(f, c)

    print("Done!")

def document_plugin(plugin_file, f):
    try: plugin = imp.load_source(os.path.basename(plugin_file)[:-3], plugin_file)
    except Exception as e:
        print ("Error loading %s: %s\nThis plugin will not be documented."
               % (plugin_file, e))
    else:
        commands = []
        if hasattr(plugin, 'configure'):
            f.write('\n\n### %s\n\n'%(plugin.__name__))
            if not plugin.configure.__doc__:
                plugin.configure.__doc__ = 'This plugin has configuration options that are not documented. Go bludgeon the author.'
            f.write(inspect.cleandoc(plugin.configure.__doc__))
        for obj in dir(plugin):
            func = getattr(plugin, obj)
            if not callable(func):
                # guard against plugins that use `from sopel import module`
                continue
            if (hasattr(func, 'commands')):
                if not hasattr(func, 'name'):
                    name = func.__name__
                else:
                    name = func.name
                setattr(func, 'plugin_name', plugin.__name__)
                commands.append((name, func))

        # return the commands from each plugin in (roughly) alphabetical order
        commands.sort()
        return commands

def process_command(f, func):
    name = func[0]
    func = func[1]

    purpose = (func.__doc__ or '*No documentation found.*')
    purpose = inspect.cleandoc(purpose).replace('\n', '<br>').replace('|', '\\|')
    # Remove when upstream docstrings in the meetbot file have been updated
    purpose = purpose.replace('_usage/meetbot-module.md', '_usage/meetbot-plugin.md')
    if hasattr(func, 'example'):
        example = '`%s`' % func.example[0]["example"].replace('$nickname', 'Sopel')
    else:
        example = ''

    commands = '.'+'<br>.'.join(func.commands) #TODO rules
    plugin = func.plugin_name
    line = "| %s | %s | %s | %s |\n" % (commands, purpose, example, plugin)
    f.write(line)

if __name__ == '__main__':
    main()
