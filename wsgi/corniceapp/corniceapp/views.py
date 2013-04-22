""" Cornice services.
"""
from cornice import Service


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
