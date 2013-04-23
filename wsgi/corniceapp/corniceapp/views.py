""" Cornice services.
"""
from cornice import Service
from datetime import datetime

from corniceapp.models import DBSession, Note


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}


samnotes = Service(name='samnotes', path='/sam/notes',
                   description="stuff sam should remember")


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

onotes = Service(name='onotes', path='/notes',
                 description="stuff sam should remember")


@onotes.get()
def get_note(request):
    return {
        'notes': [
            n.to_dict() for n in DBSession.query(Note).all()
        ]
    }


@onotes.put()
def put_note(request):
    work = Note.from_dict(request.json)
    DBSession.add(work)
    DBSession.commit()
    return work.to_dict()


specnotes = Service(name='specnotes', path='/notes/{nid}',
                    description="stuff sam should remember")


@specnotes.post()
def post_note(request):
    work = DBSession.query(Note).filter(Note.id == request.matchdict['nid']).first()
    if request.json.get('text', None):
        work.text = request.json['text']
    work.modified_at = datetime.now()
    DBSession.add(work)
    DBSession.commit()

    return work.to_dict()

@specnotes.delete()
def del_note(request):
    work = DBSession.query(Note).filter(Note.id == request.matchdict['nid']).first()
    DBSession.delete(work)
    DBSession.commit()
    return "Success"
