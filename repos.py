import logging
import random
import string

from queries import CREATE_INVITE, DELETE_INVITE, \
                    GET_LIST, UPDATE_INVITE, GET_INVITE, SET_INVITE


class Utils:
    
    
    def log(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger('main')
            try:
                logger.info(f'\n{func.__name__}\n{args}')
                return func(*args, **kwargs)
            except Exception as e:
                raise e
        return wrapper
        
        
    def for_all_methods(decorator):
        def decorate(cls):
            for attr in cls.__dict__:
                if callable(getattr(cls, attr)) and not attr.startswith('_'):
                    setattr(cls, attr, decorator(getattr(cls, attr)))
            return cls
        return decorate        
    
    
@Utils.for_all_methods(Utils.log)
class InviteService:


    def __init__(self, storage):
        self.storage = storage
        
    
    def generate_url(self, n):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
        
    
    def get_list(self):
        res = self.storage.fetch(GET_LIST)
        return res

        
    def create(self, data):
        self.storage.execute(CREATE_INVITE.format(
            guest_name=data['guestname'],
            sex=data['sex'],
            place=data['place'],
            guest_time=data['guest-time'],
            invite_url=self.generate_url(50)
            )
        )
    
    
    def delete(self, invite_id):
        self.storage.execute(DELETE_INVITE.format(invite_id=invite_id))
    
    
    def get_invite(self, invite_id):
        return self.storage.fetch(GET_INVITE.format(invite_id=invite_id))
        
    
    def invite(self, invite_id):
        self.storage.execute(SET_INVITE.format(invite_id=invite_id))