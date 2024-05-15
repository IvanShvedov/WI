CREATE table if not exists User (
  UserID integer not NULL PRIMARY key,
  UserName text NOT NULL,
  PasswordHash text NOT NULL
);

create table if not exists InviteList (
  InviteID integer NOT NULL PRIMARY KEY,
  GuestName text not NULL,
  Sex integer not null,
  Place text not null,
  GuestTime text not null,
  CreatedOn text NOT NULL,
  InviteURL text not null,
  IsInvited integer not null
);
