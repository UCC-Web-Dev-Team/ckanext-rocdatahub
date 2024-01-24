from ckan.model.meta import Base, Session

from ckan.model import User, meta
from ckan.model.domain_object import DomainObject
from sqlalchemy import Column, ForeignKey, Table, types
from sqlalchemy.orm import backref, relation, relationship, Mapped
from ckan.model.domain_object import DomainObject
from typing import Any, Collection, Optional
from sqlalchemy.ext.associationproxy import association_proxy

__all__ = ['DataRequest', 'data_request_table']

data_request_table = Table(
    'data_request',
    meta.metadata,
    Column('id', types.UnicodeText, primary_key=True, default=types.make_uuid),
    Column(
        'user_id',
        types.UnicodeText,
        ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
    ),
    Column(
        'dataset', 
        types.UnicodeText, 
        ForeignKey('package.name', onupdate='CASCADE', ondelete='CASCADE'), 
        nullable=False
    ),
    Column('status', types.String, nullable=False),
    Column('requested_at', types.DateTime, nullable=False),
    Column('approved_at', types.DateTime, nullable=True),
)

class DataRequest(DomainObject):
    id: Mapped[str]
    user_id: Mapped[str]
    dataset: Mapped[str]
    status: Mapped[str]
    requested_at: Mapped[str]
    approved_at: Mapped[Optional[str]]

    @classmethod
    def create(cls, id, user_id, country, affiliation, agreement, advertisement, reviewer):
        """
        Create a new record in the DataRequest table.

        :param id: a new DataRequest string
        :param user_id: the id of the user this DataRequest represents
        :param dataset: the requested dataset
        :param status: the status of the request
        :param requested_at: request timestamp
        :param approved_at: approval timestamp
        :return: the newly created record object
        """
        new_record = DataRequest(
            id=id, user_id=user_id, country=country, affiliation=affiliation, agreement=agreement, advertisement=advertisement, reviewer=reviewer
        )
        Session.add(new_record)
        Session.commit()
        return new_record

    @classmethod
    def read_data_request(cls, id):
        """
        Retrieve a record with a given DataRequest.

        :param id: the DataRequest string
        :return: the record object
        """
        return Session.query(DataRequest).get(id)

    @classmethod
    def read_user_data_request(cls, user_id):
        """
        Retrieve a record associated with a given user.

        :param user_id: the id of the user
        :param create_if_none: generate a new DataRequest and add a record if no record is found for the
                               given user
        :return: the record object
        """

        record = Session.query(DataRequest).filter(DataRequest.user_id == user_id).first()
        return record

    @classmethod
    def update_data_request(cls, id, **kwargs):
        """
        Update the package_id and/or published fields of a record with a given DataRequest.

        :param id: the DataRequest string
        :param kwargs: the values to be updated
        :return: the updated record object
        """
        update_dict = {k: v for k, v in kwargs.items() if k in cls.cols}
        Session.query(DataRequest).filter(DataRequest.id == id).update(update_dict)
        Session.commit()
        return cls.read_data_request(id)

    @classmethod
    def update_user_data_request(cls, user_id, **kwargs):
        """
        Update the user_id and/or published fields of a record associated with a
        given user.

        :param user_id: the id of the user
        :param kwargs: the values to be updated
        :return: the updated record object
        """
        update_dict = {k: v for k, v in kwargs.items() if k in cls.cols}
        Session.query(DataRequest).filter(DataRequest.user_id == user_id).update(update_dict)
        Session.commit()
        return cls.read_user(user_id)

    @classmethod
    def delete_data_request(cls, id):
        """
        Delete the record with a given DataRequest.

        :param id: the DataRequest string
        :return: True if a record was deleted, False if not
        """
        to_delete = cls.read_data_request(id)
        if to_delete is not None:
            Session.delete(to_delete)
            Session.commit()
            return True
        else:
            return False

    @classmethod
    def delete_user_data_request(cls, user_id):
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
    DataRequest,
    data_request_table,
    properties={
        'user': relation(
            User,
            backref=backref('data_request', cascade='all, delete-orphan'),
            primaryjoin=data_request_table.c.user_id.__eq__(User.id),
        )
    },
)


def _create_extra(key: str, value: Any):
    return DataRequest(key=str(key), value=value)

User.extras = association_proxy(
    '_extras', 'value', creator=_create_extra)