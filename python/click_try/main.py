#!/usr/bin/env python3

import click


@click.command()
@click.pass_context
@click.argument("n")
@click.option("-p", help="oPtion")
def cmd1(ctx, n, p):
    click.echo(n)
    click.echo(p)
    click.echo(ctx.obj)
    return

@click.group()
@click.pass_context
@click.argument("m")
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
