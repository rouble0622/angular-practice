import click
from flask.cli import with_appcontext
from app import db
from app.models.role import Role

@click.command('init-roles')
@with_appcontext
def init_roles_command():
    """Initialize default roles."""
    # Create default roles
    roles = [
        {'name': 'admin', 'description': 'Administrator with full access'},
        {'name': 'user', 'description': 'Regular user with limited access'}
    ]
    
    for role_data in roles:
        role = Role.query.filter_by(name=role_data['name']).first()
        if not role:
            role = Role(**role_data)
            db.session.add(role)
            click.echo(f"Created role: {role.name}")
        else:
            click.echo(f"Role already exists: {role.name}")
    
    db.session.commit()
    click.echo('Roles initialized successfully.') 