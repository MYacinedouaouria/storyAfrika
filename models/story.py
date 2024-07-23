#!/usr/bin/python3

"""
    story: represent a model for creating a story

"""
from models.imports import *
from models.base_model import BaseModel, Base
from models.image_upload import ImageUpload


class Story(BaseModel, ImageUpload, Base):
    """ Represents a story

         Attributes:
            - title: short text representing the title
            - text: the actual text content of the story
            - user_id: id of the user that made the post
            - category_id: id of the category the post is under

    """

    if os.getenv('STORAGE') in ['db', 'DB']:
        __tablename__ = 'stories'
        title = Column(String(200), nullable=False)
        text = Column(Text, nullable=False)
        user_id = Column('User', ForeignKey('users.id'), nullable=False)

        comments = relationship('Comment', backref='story', lazy=True)
        likes = relationship('Like', backref='story', lazy=True)
        bookmarks = relationship('Bookmark', backref='story', lazy=True)
        image = Column(String(100), nullable=True) # path to image

    else:
        title = ''
        text = ''
        user_id = ''

    @property
    def read_time(self):
        num_of_words = len(self.text.split())
        read_time_in_minutes = int(num_of_words / 225)

        return read_time_in_minutes

    def __init__(self, title, text, user_id, **kwargs):
        super().__init__(**kwargs)

        arguments = {
            'title': title,
            'text': text,
            'user_id': user_id,
        }
        for argument, value in arguments.items():
            if not isinstance(value, str):
                raise ValueError(f"{argument} must ba a string")

            setattr(self, argument, value)
