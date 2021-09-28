#!/usr/bin/env python3

import functools

import click
import docstring_parser as docparser


def f1(f):
    print(f"{f.__doc__=}")

    @functools.wraps(f)
    def wrapper(*args, **kargs):
        print(f"{args=}")
        print(f"{kargs=}")
        print(f"{f.__doc__=}")
        # print(f"{f.__code__=}")
        print(f"{dir(f)=}")
        # print(f"{dir(args[0])=}")
        res = f(*args, **kargs)
        return res
    # print(f"{f.__dict__=}")
    # print(f"{wrapper.__dict__=}")
    print(f"{f.params=}")
    print(f"{dir(f.params[0])=}")
    print(f"{f.params[0].help=}")
    f.params[0].help = "HOEHOEHOE"
    print(f"{f.params[0].help=}")
    attrs_f = set(dir(f))
    attrs_wrapper = set(dir(wrapper))
    for attr in (attrs_f - attrs_wrapper):
        setattr(wrapper, attr, (getattr(f, attr)))
    return wrapper


def dochelp(style=docparser.DocstringStyle.AUTO):
    def decorator(f):
        # print(f"{f.__doc__=}")
        parsed = docparser.parse(f.__doc__, style=style)
        # print(f"{parsed.short_description=}")
        # print(f"{parsed.long_description=}")
        param_dict = dict()
        for param in parsed.params:
            # print(f"{param=}")
            # print(f"{param.arg_name=}")
            # print(f"{param.description=}")
            param_dict[param.arg_name] = param.description

        # print(f"{dir(f)=}")
        # print(f"{f.help=}")
        if parsed.long_description:
            f.help = parsed.short_description + "\n\n" + parsed.long_description
        else:
            f.help = parsed.short_description
        for param in f.params:
            # print(f"{param=}")
            # print(f"{param.name=}")
            # print(f"{hasattr(param, 'help')=}")
            if hasattr(param, 'help') and param.name in param_dict:
                param.help = param_dict[param.name]
        return f
    return decorator


@dochelp()
@click.command()
@click.pass_context
@click.argument("n")
@click.option("-p", help="oPtion")
def cmd1(ctx, n, p):
    """Run CMD1.

    CMD1 description body.
    Hoehoehoe.

    SEcond paragraph.

    :param ctx: Click context
    :param n: N parameter
    :param p: P parameter
    """
    click.echo(n)
    click.echo(p)
    click.echo(ctx.obj)
    return

@dochelp()
@click.group()
@click.pass_context
@click.argument("m")
@click.option("-o", help="Option")
@click.option("--long-param")
def cli(ctx, m, o, long_param):
    """CLI root.

    Root descrption body.

    :param ctx: Click context
    :param m: M parameter
    :param o: O parameter
    :param long_param: LOOng parameter
    """
    click.echo(m)
    click.echo(o)
    ctx.ensure_object(dict)
    ctx.obj["m"] = m
    ctx.obj["o"] = o
    return

cli.add_command(cmd1)

if __name__ == "__main__":
    # cli(["--help"])
    cli(["mvalue", "cmd1", "--help"])
    # cli(["-o", "fue", "hoe", "cmd1", "abc"])
