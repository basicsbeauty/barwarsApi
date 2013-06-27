# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bwdo.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bwdo.proto',
  package='BarWars',
  serialized_pb='\n\nbwdo.proto\x12\x07\x42\x61rWars\"A\n\x0b\x43hallengeDO\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x10\n\x08\x62\x61r_code\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x83\x01\n\x06UserDO\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x19\n\x11profile_image_uri\x18\x03 \x01(\t\x12\x0e\n\x06points\x18\x04 \x01(\r\x12\x14\n\x0csolved_count\x18\x05 \x01(\r\x12\x14\n\x0csubmit_count\x18\x06 \x01(\r\"_\n\x15GetDescriptionRequest\x12\'\n\tchallenge\x18\x01 \x02(\x0b\x32\x14.BarWars.ChallengeDO\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.BarWars.UserDO\"A\n\x16GetDescriptionResponse\x12\'\n\tchallenge\x18\x01 \x02(\x0b\x32\x14.BarWars.ChallengeDO\"2\n\x11GetProfileRequest\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\"3\n\x12GetProfileResponse\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\"I\n\x18GetChallengesListRequest\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"I\n\x19GetChallengesListResponse\x12,\n\x0e\x63hallenge_list\x18\x01 \x03(\x0b\x32\x14.BarWars.ChallengeDO\"7\n\x16\x43reateProfileDORequest\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\"8\n\x17\x43reateProfileDOResponse\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\"b\n\x18SubmitChallengeDORequest\x12\'\n\tchallenge\x18\x01 \x02(\x0b\x32\x14.BarWars.ChallengeDO\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.BarWars.UserDO\":\n\x19SubmitChallengeDOResponse\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\"a\n\x17SolveChallengeDORequest\x12\'\n\tchallenge\x18\x01 \x02(\x0b\x32\x14.BarWars.ChallengeDO\x12\x1d\n\x04user\x18\x02 \x01(\x0b\x32\x0f.BarWars.UserDO\"9\n\x18SolveChallengeDOResponse\x12\x1d\n\x04user\x18\x01 \x02(\x0b\x32\x0f.BarWars.UserDO\"%\n\x0eMessagePayload\x12\x13\n\x0braw_payload\x18\x01 \x01(\x0c\"\xbf\x01\n\x07Message\x12\x12\n\x07version\x18\x01 \x02(\r:\x01\x31\x12\r\n\x02id\x18\x02 \x02(\r:\x01\x30\x12$\n\x04type\x18\x03 \x02(\x0e\x32\x16.BarWars.OperationType\x12\x14\n\ttimestamp\x18\x04 \x01(\x04:\x01\x30\x12\x13\n\x0bstatus_code\x18\x05 \x01(\x05\x12\x16\n\x0estatus_message\x18\x06 \x01(\t\x12(\n\x07payload\x18\x07 \x01(\x0b\x32\x17.BarWars.MessagePayload*\x95\x01\n\rOperationType\x12\x13\n\x0fGET_DESCRIPTION\x10\x01\x12\x0f\n\x0bGET_PROFILE\x10\x02\x12\x17\n\x13GET_CHALLENGES_LIST\x10\x03\x12\x10\n\x0cPOST_PROFILE\x10\x04\x12\x19\n\x15POST_SUBMIT_CHALLENGE\x10\x05\x12\x18\n\x14POST_SOLVE_CHALLENGE\x10\x06')

_OPERATIONTYPE = _descriptor.EnumDescriptor(
  name='OperationType',
  full_name='BarWars.OperationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET_DESCRIPTION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PROFILE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CHALLENGES_LIST', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_PROFILE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_SUBMIT_CHALLENGE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_SOLVE_CHALLENGE', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1310,
  serialized_end=1459,
)

OperationType = enum_type_wrapper.EnumTypeWrapper(_OPERATIONTYPE)
GET_DESCRIPTION = 1
GET_PROFILE = 2
GET_CHALLENGES_LIST = 3
POST_PROFILE = 4
POST_SUBMIT_CHALLENGE = 5
POST_SOLVE_CHALLENGE = 6



_CHALLENGEDO = _descriptor.Descriptor(
  name='ChallengeDO',
  full_name='BarWars.ChallengeDO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='BarWars.ChallengeDO.cid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bar_code', full_name='BarWars.ChallengeDO.bar_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='BarWars.ChallengeDO.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=88,
)


_USERDO = _descriptor.Descriptor(
  name='UserDO',
  full_name='BarWars.UserDO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='BarWars.UserDO.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='BarWars.UserDO.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profile_image_uri', full_name='BarWars.UserDO.profile_image_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='points', full_name='BarWars.UserDO.points', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='solved_count', full_name='BarWars.UserDO.solved_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submit_count', full_name='BarWars.UserDO.submit_count', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=91,
  serialized_end=222,
)


_GETDESCRIPTIONREQUEST = _descriptor.Descriptor(
  name='GetDescriptionRequest',
  full_name='BarWars.GetDescriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='BarWars.GetDescriptionRequest.challenge', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.GetDescriptionRequest.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=224,
  serialized_end=319,
)


_GETDESCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='GetDescriptionResponse',
  full_name='BarWars.GetDescriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='BarWars.GetDescriptionResponse.challenge', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=321,
  serialized_end=386,
)


_GETPROFILEREQUEST = _descriptor.Descriptor(
  name='GetProfileRequest',
  full_name='BarWars.GetProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.GetProfileRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=388,
  serialized_end=438,
)


_GETPROFILERESPONSE = _descriptor.Descriptor(
  name='GetProfileResponse',
  full_name='BarWars.GetProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.GetProfileResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=440,
  serialized_end=491,
)


_GETCHALLENGESLISTREQUEST = _descriptor.Descriptor(
  name='GetChallengesListRequest',
  full_name='BarWars.GetChallengesListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.GetChallengesListRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='BarWars.GetChallengesListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=493,
  serialized_end=566,
)


_GETCHALLENGESLISTRESPONSE = _descriptor.Descriptor(
  name='GetChallengesListResponse',
  full_name='BarWars.GetChallengesListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_list', full_name='BarWars.GetChallengesListResponse.challenge_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=568,
  serialized_end=641,
)


_CREATEPROFILEDOREQUEST = _descriptor.Descriptor(
  name='CreateProfileDORequest',
  full_name='BarWars.CreateProfileDORequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.CreateProfileDORequest.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=643,
  serialized_end=698,
)


_CREATEPROFILEDORESPONSE = _descriptor.Descriptor(
  name='CreateProfileDOResponse',
  full_name='BarWars.CreateProfileDOResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.CreateProfileDOResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=700,
  serialized_end=756,
)


_SUBMITCHALLENGEDOREQUEST = _descriptor.Descriptor(
  name='SubmitChallengeDORequest',
  full_name='BarWars.SubmitChallengeDORequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='BarWars.SubmitChallengeDORequest.challenge', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.SubmitChallengeDORequest.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=758,
  serialized_end=856,
)


_SUBMITCHALLENGEDORESPONSE = _descriptor.Descriptor(
  name='SubmitChallengeDOResponse',
  full_name='BarWars.SubmitChallengeDOResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.SubmitChallengeDOResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=858,
  serialized_end=916,
)


_SOLVECHALLENGEDOREQUEST = _descriptor.Descriptor(
  name='SolveChallengeDORequest',
  full_name='BarWars.SolveChallengeDORequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='BarWars.SolveChallengeDORequest.challenge', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.SolveChallengeDORequest.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=918,
  serialized_end=1015,
)


_SOLVECHALLENGEDORESPONSE = _descriptor.Descriptor(
  name='SolveChallengeDOResponse',
  full_name='BarWars.SolveChallengeDOResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='BarWars.SolveChallengeDOResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1017,
  serialized_end=1074,
)


_MESSAGEPAYLOAD = _descriptor.Descriptor(
  name='MessagePayload',
  full_name='BarWars.MessagePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_payload', full_name='BarWars.MessagePayload.raw_payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1076,
  serialized_end=1113,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='BarWars.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='BarWars.Message.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='BarWars.Message.id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='BarWars.Message.type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='BarWars.Message.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='BarWars.Message.status_code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='BarWars.Message.status_message', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='BarWars.Message.payload', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1116,
  serialized_end=1307,
)

_GETDESCRIPTIONREQUEST.fields_by_name['challenge'].message_type = _CHALLENGEDO
_GETDESCRIPTIONREQUEST.fields_by_name['user'].message_type = _USERDO
_GETDESCRIPTIONRESPONSE.fields_by_name['challenge'].message_type = _CHALLENGEDO
_GETPROFILEREQUEST.fields_by_name['user'].message_type = _USERDO
_GETPROFILERESPONSE.fields_by_name['user'].message_type = _USERDO
_GETCHALLENGESLISTREQUEST.fields_by_name['user'].message_type = _USERDO
_GETCHALLENGESLISTRESPONSE.fields_by_name['challenge_list'].message_type = _CHALLENGEDO
_CREATEPROFILEDOREQUEST.fields_by_name['user'].message_type = _USERDO
_CREATEPROFILEDORESPONSE.fields_by_name['user'].message_type = _USERDO
_SUBMITCHALLENGEDOREQUEST.fields_by_name['challenge'].message_type = _CHALLENGEDO
_SUBMITCHALLENGEDOREQUEST.fields_by_name['user'].message_type = _USERDO
_SUBMITCHALLENGEDORESPONSE.fields_by_name['user'].message_type = _USERDO
_SOLVECHALLENGEDOREQUEST.fields_by_name['challenge'].message_type = _CHALLENGEDO
_SOLVECHALLENGEDOREQUEST.fields_by_name['user'].message_type = _USERDO
_SOLVECHALLENGEDORESPONSE.fields_by_name['user'].message_type = _USERDO
_MESSAGE.fields_by_name['type'].enum_type = _OPERATIONTYPE
_MESSAGE.fields_by_name['payload'].message_type = _MESSAGEPAYLOAD
DESCRIPTOR.message_types_by_name['ChallengeDO'] = _CHALLENGEDO
DESCRIPTOR.message_types_by_name['UserDO'] = _USERDO
DESCRIPTOR.message_types_by_name['GetDescriptionRequest'] = _GETDESCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['GetDescriptionResponse'] = _GETDESCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetProfileRequest'] = _GETPROFILEREQUEST
DESCRIPTOR.message_types_by_name['GetProfileResponse'] = _GETPROFILERESPONSE
DESCRIPTOR.message_types_by_name['GetChallengesListRequest'] = _GETCHALLENGESLISTREQUEST
DESCRIPTOR.message_types_by_name['GetChallengesListResponse'] = _GETCHALLENGESLISTRESPONSE
DESCRIPTOR.message_types_by_name['CreateProfileDORequest'] = _CREATEPROFILEDOREQUEST
DESCRIPTOR.message_types_by_name['CreateProfileDOResponse'] = _CREATEPROFILEDORESPONSE
DESCRIPTOR.message_types_by_name['SubmitChallengeDORequest'] = _SUBMITCHALLENGEDOREQUEST
DESCRIPTOR.message_types_by_name['SubmitChallengeDOResponse'] = _SUBMITCHALLENGEDORESPONSE
DESCRIPTOR.message_types_by_name['SolveChallengeDORequest'] = _SOLVECHALLENGEDOREQUEST
DESCRIPTOR.message_types_by_name['SolveChallengeDOResponse'] = _SOLVECHALLENGEDORESPONSE
DESCRIPTOR.message_types_by_name['MessagePayload'] = _MESSAGEPAYLOAD
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

class ChallengeDO(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHALLENGEDO

  # @@protoc_insertion_point(class_scope:BarWars.ChallengeDO)

class UserDO(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERDO

  # @@protoc_insertion_point(class_scope:BarWars.UserDO)

class GetDescriptionRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDESCRIPTIONREQUEST

  # @@protoc_insertion_point(class_scope:BarWars.GetDescriptionRequest)

class GetDescriptionResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDESCRIPTIONRESPONSE

  # @@protoc_insertion_point(class_scope:BarWars.GetDescriptionResponse)

class GetProfileRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPROFILEREQUEST

  # @@protoc_insertion_point(class_scope:BarWars.GetProfileRequest)

class GetProfileResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPROFILERESPONSE

  # @@protoc_insertion_point(class_scope:BarWars.GetProfileResponse)

class GetChallengesListRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCHALLENGESLISTREQUEST

  # @@protoc_insertion_point(class_scope:BarWars.GetChallengesListRequest)

class GetChallengesListResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCHALLENGESLISTRESPONSE

  # @@protoc_insertion_point(class_scope:BarWars.GetChallengesListResponse)

class CreateProfileDORequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEPROFILEDOREQUEST

  # @@protoc_insertion_point(class_scope:BarWars.CreateProfileDORequest)

class CreateProfileDOResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEPROFILEDORESPONSE

  # @@protoc_insertion_point(class_scope:BarWars.CreateProfileDOResponse)

class SubmitChallengeDORequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBMITCHALLENGEDOREQUEST

  # @@protoc_insertion_point(class_scope:BarWars.SubmitChallengeDORequest)

class SubmitChallengeDOResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBMITCHALLENGEDORESPONSE

  # @@protoc_insertion_point(class_scope:BarWars.SubmitChallengeDOResponse)

class SolveChallengeDORequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOLVECHALLENGEDOREQUEST

  # @@protoc_insertion_point(class_scope:BarWars.SolveChallengeDORequest)

class SolveChallengeDOResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOLVECHALLENGEDORESPONSE

  # @@protoc_insertion_point(class_scope:BarWars.SolveChallengeDOResponse)

class MessagePayload(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGEPAYLOAD

  # @@protoc_insertion_point(class_scope:BarWars.MessagePayload)

class Message(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGE

  # @@protoc_insertion_point(class_scope:BarWars.Message)


# @@protoc_insertion_point(module_scope)
