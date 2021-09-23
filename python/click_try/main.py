#!/usr/bin/env python3

import functools

import click

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


@f1
@click.command()
@click.pass_context
@click.argument("n", help="n help")
@click.option("-p", help="oPtion")
def cmd1(ctx, n, p):
    click.echo(n)
    click.echo(p)
    click.echo(ctx.obj)
    return

@click.group()
@click.pass_context
@click.argument("m", help="m help")
@click.option("-o", help="Option")
def cli(ctx, m, o):
    click.echo(m)
    click.echo(o)
    ctx.ensure_object(dict)
    ctx.obj["m"] = m
    ctx.obj["o"] = o
    return

cli.add_command(cmd1)

if __name__ == "__main__":
    # cli(["--help"])
    cli(["-o", "fue", "hoe", "cmd1", "abc"])
