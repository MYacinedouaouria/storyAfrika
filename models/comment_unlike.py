"""
    comment_unlike: represent the number of unlikes for a comment

"""

from models.imports import *
from models.base_model import BaseModel, Base


class CommentUnLike(BaseModel, Base):
    """ Represent a like

        - Attributes:
            - comment_id: the comment that was unliked
            - user_id: the user that unliked the comment

    """

    if os.getenv('STORAGE') in ['db', 'DB']:
        __tablename__ = 'comment_unlikes'
        comment_id = Column(String(60), ForeignKey('comments.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        comment_id = ''
        user_id = ''

    def __init__(self, comment_id, user_id):
        super().__init__()
        if isinstance(comment_id, str) and isinstance(user_id, str):
            self.comment_id = comment_id
            self.user_id = user_id
        else:
            raise ValueError("arguments must be a string")