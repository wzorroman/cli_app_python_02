import os
import requests
import click

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("Welcome to the contacts app 🥳")
        click.echo("Run contacts --help for options.")


@cli.command()
@click.argument('name')
@click.option('--mobile', '-m', required=True)
def add(name, mobile):
    """
    Add a new contact
    """
    response = requests.put('{}/contacts/{}.json'
                            .format(os.getenv('URL'), name),
                            json={'mobile': '{}'.format(mobile)})
    click.echo('Contact {} added!'.format(name))
    click.echo(response.json())


@cli.command()
def list():
    """
    View all contacts
    """
    response = requests.get('{}/contacts.json'
                            .format(os.getenv('URL')))
    click.echo('Here\'s a list of all your contacts:')
    click.echo(response.json())


@cli.command()
@click.argument('name')
def view(name):
    """
    View single contact
    """
    response = requests.get('{}/contacts/{}.json'
                            .format(os.getenv('URL'), name))
    if not response.json():
        click.echo("The contact you searched for does'nt exist")
    else:
        click.echo(response.json())


@cli.command()
@click.argument('name')
@click.option('--mobile', '-m', required=True)
def update(name, mobile):
    """
    Update contact
    """
    response = requests.patch('{}/contacts/{}.json'
                              .format(os.getenv('URL'), name),
                              json={'mobile': '{}'.format(mobile)})
    click.echo('Contact updated!')
    click.echo(response.json())


@cli.command()
@click.argument('name')
def delete(name):
    """
    Delete contact
    """
    requests.delete('{}/contacts/{}.json'
                    .format(os.getenv('URL'), name))
    click.echo('Contact deleted!')
