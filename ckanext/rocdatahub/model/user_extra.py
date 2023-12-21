from ckan.model.meta import Base, Session

from ckan.model import User, meta
from ckan.model.domain_object import DomainObject
from sqlalchemy import Column, ForeignKey, Table, types
from sqlalchemy.orm import backref, relation, relationship, Mapped
from ckan.model.domain_object import DomainObject
from typing import Any, Collection, Optional
from sqlalchemy.ext.associationproxy import association_proxy

__all__ = ['UserExtra', 'user_extra_table']

user_extra_table = Table(
    'user_extra',
    meta.metadata,
    Column('id', types.UnicodeText, primary_key=True, default=types.make_uuid),
    Column(
        'user_id',
        types.UnicodeText,
        ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
        unique=True,
    ),
    Column('country', types.UnicodeText, nullable=True),
    Column('affiliation', types.UnicodeText, nullable=True),
    Column('agreement', types.Boolean, nullable=True),
    Column('advertisement', types.Boolean, nullable=True),
    Column('reviewer', types.Boolean, nullable=True),
)

class UserExtra(DomainObject):
    id: Mapped[str]
    user_id: Mapped[str]
    country: Mapped[Optional[str]]
    affiliation: Mapped[Optional[str]]
    agreement: Mapped[str]
    advertisement: Mapped[Optional[str]]
    reviewer: Mapped[Optional[str]]

    @classmethod
    def create(cls, id, user_id, country, affiliation, agreement, advertisement, reviewer):
        """
        Create a new record in the UserExtra table.

        :param id: a new UserExtra string
        :param user_id: the id of the user this UserExtra represents
        :param country: the country of residence of the user
        :param affiliation: the institutional affiliation of the user
        :param agreement: agreement to the terms of use
        :param advertisement: allow to receive advertisement
        :param reviewer: agree to be a reviewer
        :return: the newly created record object
        """
        new_record = UserExtra(
            id=id, user_id=user_id, country=country, affiliation=affiliation, agreement=agreement, advertisement=advertisement, reviewer=reviewer
        )
        Session.add(new_record)
        Session.commit()
        return new_record

    @classmethod
    def read_user_extra(cls, id):
        """
        Retrieve a record with a given UserExtra.

        :param id: the UserExtra string
        :return: the record object
        """
        return Session.query(UserExtra).get(id)

    @classmethod
    def read_user(cls, user_id):
        """
        Retrieve a record associated with a given user.

        :param user_id: the id of the user
        :param create_if_none: generate a new UserExtra and add a record if no record is found for the
                               given user
        :return: the record object
        """

        record = Session.query(UserExtra).filter(UserExtra.user_id == user_id).first()
        return record

    @classmethod
    def update_user_extra(cls, id, **kwargs):
        """
        Update the package_id and/or published fields of a record with a given UserExtra.

        :param id: the UserExtra string
        :param kwargs: the values to be updated
        :return: the updated record object
        """
        update_dict = {k: v for k, v in kwargs.items() if k in cls.cols}
        Session.query(UserExtra).filter(UserExtra.id == id).update(update_dict)
        Session.commit()
        return cls.read_user_extra(id)

    @classmethod
    def update_user(cls, user_id, **kwargs):
        """
        Update the user_id and/or published fields of a record associated with a
        given user.

        :param user_id: the id of the user
        :param kwargs: the values to be updated
        :return: the updated record object
        """
        update_dict = {k: v for k, v in kwargs.items() if k in cls.cols}
        Session.query(UserExtra).filter(UserExtra.user_id == user_id).update(update_dict)
        Session.commit()
        return cls.read_user(user_id)

    @classmethod
    def delete_user_extra(cls, id):
        """
        Delete the record with a given UserExtra.

        :param id: the UserExtra string
        :return: True if a record was deleted, False if not
        """
        to_delete = cls.read_user_extra(id)
        if to_delete is not None:
            Session.delete(to_delete)
            Session.commit()
            return True
        else:
            return False

    @classmethod
    def delete_user(cls, user_id):
        """
        Delete the record associated with a given user.

        :param user_id: the id of the user
        :return: True if a record was deleted, False if not
        """
        to_delete = cls.read_user(user_id)
        if to_delete is not None:
            Session.delete(to_delete)
            Session.commit()
            return True
        else:
            return False


meta.mapper(
    UserExtra,
    user_extra_table,
    properties={
        'user': relation(
            User,
            backref=backref('user_extra', cascade='all, delete-orphan'),
            primaryjoin=user_extra_table.c.user_id.__eq__(User.id),
        )
    },
)


def _create_extra(key: str, value: Any):
    return UserExtra(key=str(key), value=value)

User.extras = association_proxy(
    '_extras', 'value', creator=_create_extra)