CREATE_INVITE = '''insert into 
    InviteList (GuestName, Sex, Place, GuestTime, CreatedOn, InviteURL, IsInvited)
    values ('{guest_name}', '{sex}', '{place}', '{guest_time}', date('now'), '{invite_url}', 0)
'''

GET_INVITE = '''select * from InviteList where InviteURL = "{invite_id}"'''

DELETE_INVITE = '''
    delete from InviteList where InviteID = {invite_id}
'''

GET_LIST = '''
    select * from InviteList
'''

UPDATE_INVITE = '''
    update InviteList
    set GuestName = '{guest_name}',
        Sex = '{sex}',
        Place = '{place}',
        GuestTime = '{guest_time}'
'''

SET_INVITE = '''
    update InviteList
    set IsInvited = 1
    where InviteURL = "{invite_id}"
'''