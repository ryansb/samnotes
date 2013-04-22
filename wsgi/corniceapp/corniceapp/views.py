""" Cornice services.
"""
from cornice import Service

from corniceapp.models import DBSession, Note


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

samnotes = Service(name='samnotes', path='/sam/notes', description="stuff sam should remember")

@samnotes.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {
        "programs": [
            "tmux",
            "nload",
            "iftop"
        ]
    }

onotes = Service(name='onotes', path='/notes', description="stuff sam should remember")

@onotes.get()
def get_info(request):
    return {
        'notes': [
            n.to_dict() for n in DBSession.query(Note).all()
        ]
    }
