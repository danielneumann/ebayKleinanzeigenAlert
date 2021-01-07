from contextlib import contextmanager
import os
import enum
from . import createLogger

log = createLogger(__name__)

try:
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
except ImportError:
    log.error("SQLAlchemy should be installed\npip install sqlalchemy")

FILELOCATION = os.path.join(os.path.expanduser("~"), "postwatch.db")
engine = create_engine('sqlite:///{!s}'.format(FILELOCATION), echo=False)
Base = declarative_base()

## ENUM Classes ##
class MessageTypes(enum.IntEnum):
    ebaykleinanzeigen = 1
    immoscout = 2
    immonet = 3

class IntEnum(Base.TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = Base.Integer

    def __init__(self, enumtype, *args, **kwargs):
        super(IntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value

        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)
## End ENUM Classes ##

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)

    platform_type = Base.Column(IntEnum(MessageTypes), default=MessageTypes.ebaykleinanzeigen)
    title = Column(String)
    price = Column(String)
    post_id = Column(Integer)
    link = Column(String)


class Link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)

    platform_type = Base.Column(IntEnum(MessageTypes), default=MessageTypes.ebaykleinanzeigen)
    link = Column(String)




Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@contextmanager
def getSession():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        log.error(e)
    finally:
        session.close()



def postExist(post_id):
    with getSession() as db:
        result = db.query(Post).filter(Post.post_id == post_id).first()
        return bool(result)



def addPost(post_list=None):
    with getSession() as db:
        if post_list is not None:
            for post in post_list:
                newPost = Post()
                newPost.post_id = post.id
                newPost.link = post.link
                newPost.price = post.price
                newPost.title = post.title
                db.add(newPost)



def addLink(link):
    with getSession() as db:
        newLink = Link()
        newLink.link = link
        db.add(newLink)


#def getLinks():
#    with getSession() as db:
#        result = db.query(Link).all()
#        links = []
#        for row in result:
#            links.append(row.__dict__)
#        return links

def getLinks():
    with getSession() as db:
        result = db.query(Link).all()
        links = []
        for row in result:
            links.append((row.id, row.link))
        return links


def removeLink(linkId):
    with getSession() as db:
        result = db.query(Link).filter(Link.id == linkId).first()
        db.delete(result)

def clearPostDatabase():
    with getSession() as db:
        result = db.query(Post)
        result.delete()

