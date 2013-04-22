from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Unicode, String, Text, DateTime, ForeignKey, Column, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

_Base = declarative_base()
DBSession = scoped_session(sessionmaker())

class Note(_Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime())
    text = Column(Text())

    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
        )

    @classmethod
    def from_dict(cls, new):
        n = Note()
        n.created_at = datetime.now()
        n.text = new.get('text', '')
        return n

    def __repr__(self):
        return "Note id: %s snippet: %s" % (self.id, self.text[:20])

def initialize_db(engine):
    DBSession.configure(bind=engine)
    _Base.metadata.bind = engine
    _Base.metadata.drop_all()
    _Base.metadata.create_all(engine, checkfirst=False)
    DBSession.add(Note.from_dict({'text': 'check out tmux, it is a terminal multiplexer'}))
    DBSession.commit()

