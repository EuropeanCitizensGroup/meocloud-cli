#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,slots
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class NotificationLevel(object):
  INFO = 0
  WARNING = 1
  ERROR = 2

  _VALUES_TO_NAMES = {
    0: "INFO",
    1: "WARNING",
    2: "ERROR",
  }

  _NAMES_TO_VALUES = {
    "INFO": 0,
    "WARNING": 1,
    "ERROR": 2,
  }

class State(object):
  INITIALIZING = 0
  AUTHORIZING = 1
  WAITING = 2
  SYNCING = 3
  READY = 4
  PAUSED = 5
  ERROR = 6
  SELECTIVE_SYNC = 7
  RESTARTING = 8
  OFFLINE = 9

  _VALUES_TO_NAMES = {
    0: "INITIALIZING",
    1: "AUTHORIZING",
    2: "WAITING",
    3: "SYNCING",
    4: "READY",
    5: "PAUSED",
    6: "ERROR",
    7: "SELECTIVE_SYNC",
    8: "RESTARTING",
    9: "OFFLINE",
  }

  _NAMES_TO_VALUES = {
    "INITIALIZING": 0,
    "AUTHORIZING": 1,
    "WAITING": 2,
    "SYNCING": 3,
    "READY": 4,
    "PAUSED": 5,
    "ERROR": 6,
    "SELECTIVE_SYNC": 7,
    "RESTARTING": 8,
    "OFFLINE": 9,
  }


class UserNotification(object):
  """
  Attributes:
   - code
   - type
   - level
   - parameters
  """

  __slots__ = [ 
    'code',
    'type',
    'level',
    'parameters',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'code', None, None, ), # 1
    (2, TType.I32, 'type', None, None, ), # 2
    (3, TType.I32, 'level', None,     0, ), # 3
    (4, TType.LIST, 'parameters', (TType.STRING,None), None, ), # 4
  )

  def __init__(self, code=None, type=None, level=thrift_spec[3][4], parameters=None,):
    self.code = code
    self.type = type
    self.level = level
    self.parameters = parameters

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.level = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.parameters = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.parameters.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('UserNotification')
    if self.code is not None:
      oprot.writeFieldBegin('code', TType.I32, 1)
      oprot.writeI32(self.code)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.level is not None:
      oprot.writeFieldBegin('level', TType.I32, 3)
      oprot.writeI32(self.level)
      oprot.writeFieldEnd()
    if self.parameters is not None:
      oprot.writeFieldBegin('parameters', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.parameters))
      for iter6 in self.parameters:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class SystemNotification(object):
  """
  Attributes:
   - code
   - parameters
  """

  __slots__ = [ 
    'code',
    'parameters',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'code', None, None, ), # 1
    (2, TType.LIST, 'parameters', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, code=None, parameters=None,):
    self.code = code
    self.parameters = parameters

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.parameters = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString();
            self.parameters.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SystemNotification')
    if self.code is not None:
      oprot.writeFieldBegin('code', TType.I32, 1)
      oprot.writeI32(self.code)
      oprot.writeFieldEnd()
    if self.parameters is not None:
      oprot.writeFieldBegin('parameters', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.parameters))
      for iter13 in self.parameters:
        oprot.writeString(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class SyncStatus(object):
  """
  Attributes:
   - uploadRate
   - downloadRate
   - pendingUploads
   - pendingDownloads
   - uploadETASecs
   - downloadETASecs
   - pendingIndexes
   - downloadingPath
   - uploadingPath
   - indexingPath
  """

  __slots__ = [ 
    'uploadRate',
    'downloadRate',
    'pendingUploads',
    'pendingDownloads',
    'uploadETASecs',
    'downloadETASecs',
    'pendingIndexes',
    'downloadingPath',
    'uploadingPath',
    'indexingPath',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'uploadRate', None, None, ), # 1
    (2, TType.I32, 'downloadRate', None, None, ), # 2
    (3, TType.I32, 'pendingUploads', None, None, ), # 3
    (4, TType.I32, 'pendingDownloads', None, None, ), # 4
    (5, TType.I32, 'uploadETASecs', None, None, ), # 5
    (6, TType.I32, 'downloadETASecs', None, None, ), # 6
    (7, TType.I32, 'pendingIndexes', None, None, ), # 7
    (8, TType.STRING, 'downloadingPath', None, None, ), # 8
    (9, TType.STRING, 'uploadingPath', None, None, ), # 9
    (10, TType.STRING, 'indexingPath', None, None, ), # 10
  )

  def __init__(self, uploadRate=None, downloadRate=None, pendingUploads=None, pendingDownloads=None, uploadETASecs=None, downloadETASecs=None, pendingIndexes=None, downloadingPath=None, uploadingPath=None, indexingPath=None,):
    self.uploadRate = uploadRate
    self.downloadRate = downloadRate
    self.pendingUploads = pendingUploads
    self.pendingDownloads = pendingDownloads
    self.uploadETASecs = uploadETASecs
    self.downloadETASecs = downloadETASecs
    self.pendingIndexes = pendingIndexes
    self.downloadingPath = downloadingPath
    self.uploadingPath = uploadingPath
    self.indexingPath = indexingPath

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.uploadRate = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.downloadRate = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.pendingUploads = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.pendingDownloads = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.uploadETASecs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.downloadETASecs = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.pendingIndexes = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.downloadingPath = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.uploadingPath = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.indexingPath = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SyncStatus')
    if self.uploadRate is not None:
      oprot.writeFieldBegin('uploadRate', TType.I32, 1)
      oprot.writeI32(self.uploadRate)
      oprot.writeFieldEnd()
    if self.downloadRate is not None:
      oprot.writeFieldBegin('downloadRate', TType.I32, 2)
      oprot.writeI32(self.downloadRate)
      oprot.writeFieldEnd()
    if self.pendingUploads is not None:
      oprot.writeFieldBegin('pendingUploads', TType.I32, 3)
      oprot.writeI32(self.pendingUploads)
      oprot.writeFieldEnd()
    if self.pendingDownloads is not None:
      oprot.writeFieldBegin('pendingDownloads', TType.I32, 4)
      oprot.writeI32(self.pendingDownloads)
      oprot.writeFieldEnd()
    if self.uploadETASecs is not None:
      oprot.writeFieldBegin('uploadETASecs', TType.I32, 5)
      oprot.writeI32(self.uploadETASecs)
      oprot.writeFieldEnd()
    if self.downloadETASecs is not None:
      oprot.writeFieldBegin('downloadETASecs', TType.I32, 6)
      oprot.writeI32(self.downloadETASecs)
      oprot.writeFieldEnd()
    if self.pendingIndexes is not None:
      oprot.writeFieldBegin('pendingIndexes', TType.I32, 7)
      oprot.writeI32(self.pendingIndexes)
      oprot.writeFieldEnd()
    if self.downloadingPath is not None:
      oprot.writeFieldBegin('downloadingPath', TType.STRING, 8)
      oprot.writeString(self.downloadingPath)
      oprot.writeFieldEnd()
    if self.uploadingPath is not None:
      oprot.writeFieldBegin('uploadingPath', TType.STRING, 9)
      oprot.writeString(self.uploadingPath)
      oprot.writeFieldEnd()
    if self.indexingPath is not None:
      oprot.writeFieldBegin('indexingPath', TType.STRING, 10)
      oprot.writeString(self.indexingPath)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class Status(object):
  """
  Attributes:
   - state
   - statusCode
   - usedQuota
   - totalQuota
  """

  __slots__ = [ 
    'state',
    'statusCode',
    'usedQuota',
    'totalQuota',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'state', None, None, ), # 1
    (2, TType.I32, 'statusCode', None, None, ), # 2
    (3, TType.I64, 'usedQuota', None, None, ), # 3
    (4, TType.I64, 'totalQuota', None, None, ), # 4
  )

  def __init__(self, state=None, statusCode=None, usedQuota=None, totalQuota=None,):
    self.state = state
    self.statusCode = statusCode
    self.usedQuota = usedQuota
    self.totalQuota = totalQuota

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.state = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.statusCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.usedQuota = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.totalQuota = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Status')
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 1)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    if self.statusCode is not None:
      oprot.writeFieldBegin('statusCode', TType.I32, 2)
      oprot.writeI32(self.statusCode)
      oprot.writeFieldEnd()
    if self.usedQuota is not None:
      oprot.writeFieldBegin('usedQuota', TType.I64, 3)
      oprot.writeI64(self.usedQuota)
      oprot.writeFieldEnd()
    if self.totalQuota is not None:
      oprot.writeFieldBegin('totalQuota', TType.I64, 4)
      oprot.writeI64(self.totalQuota)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class NetworkSettings(object):
  """
  Attributes:
   - proxyAddress
   - proxyType
   - proxyPort
   - proxyUser
   - proxyPassword
   - uploadBandwidth
   - downloadBandwidth
  """

  __slots__ = [ 
    'proxyAddress',
    'proxyType',
    'proxyPort',
    'proxyUser',
    'proxyPassword',
    'uploadBandwidth',
    'downloadBandwidth',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'proxyAddress', None, None, ), # 1
    (2, TType.STRING, 'proxyType', None, None, ), # 2
    (3, TType.I32, 'proxyPort', None, None, ), # 3
    (4, TType.STRING, 'proxyUser', None, None, ), # 4
    (5, TType.STRING, 'proxyPassword', None, None, ), # 5
    (6, TType.I32, 'uploadBandwidth', None, None, ), # 6
    (7, TType.I32, 'downloadBandwidth', None, None, ), # 7
  )

  def __init__(self, proxyAddress=None, proxyType=None, proxyPort=None, proxyUser=None, proxyPassword=None, uploadBandwidth=None, downloadBandwidth=None,):
    self.proxyAddress = proxyAddress
    self.proxyType = proxyType
    self.proxyPort = proxyPort
    self.proxyUser = proxyUser
    self.proxyPassword = proxyPassword
    self.uploadBandwidth = uploadBandwidth
    self.downloadBandwidth = downloadBandwidth

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.proxyAddress = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.proxyType = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.proxyPort = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.proxyUser = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.proxyPassword = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.uploadBandwidth = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.downloadBandwidth = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NetworkSettings')
    if self.proxyAddress is not None:
      oprot.writeFieldBegin('proxyAddress', TType.STRING, 1)
      oprot.writeString(self.proxyAddress)
      oprot.writeFieldEnd()
    if self.proxyType is not None:
      oprot.writeFieldBegin('proxyType', TType.STRING, 2)
      oprot.writeString(self.proxyType)
      oprot.writeFieldEnd()
    if self.proxyPort is not None:
      oprot.writeFieldBegin('proxyPort', TType.I32, 3)
      oprot.writeI32(self.proxyPort)
      oprot.writeFieldEnd()
    if self.proxyUser is not None:
      oprot.writeFieldBegin('proxyUser', TType.STRING, 4)
      oprot.writeString(self.proxyUser)
      oprot.writeFieldEnd()
    if self.proxyPassword is not None:
      oprot.writeFieldBegin('proxyPassword', TType.STRING, 5)
      oprot.writeString(self.proxyPassword)
      oprot.writeFieldEnd()
    if self.uploadBandwidth is not None:
      oprot.writeFieldBegin('uploadBandwidth', TType.I32, 6)
      oprot.writeI32(self.uploadBandwidth)
      oprot.writeFieldEnd()
    if self.downloadBandwidth is not None:
      oprot.writeFieldBegin('downloadBandwidth', TType.I32, 7)
      oprot.writeI32(self.downloadBandwidth)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class DesktopSettings(object):
  """
  Attributes:
   - autostart
   - notifications
   - blackIcons
  """

  __slots__ = [ 
    'autostart',
    'notifications',
    'blackIcons',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'autostart', None, None, ), # 1
    (2, TType.BOOL, 'notifications', None, None, ), # 2
    (3, TType.BOOL, 'blackIcons', None, None, ), # 3
  )

  def __init__(self, autostart=None, notifications=None, blackIcons=None,):
    self.autostart = autostart
    self.notifications = notifications
    self.blackIcons = blackIcons

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.autostart = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.notifications = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.blackIcons = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DesktopSettings')
    if self.autostart is not None:
      oprot.writeFieldBegin('autostart', TType.BOOL, 1)
      oprot.writeBool(self.autostart)
      oprot.writeFieldEnd()
    if self.notifications is not None:
      oprot.writeFieldBegin('notifications', TType.BOOL, 2)
      oprot.writeBool(self.notifications)
      oprot.writeFieldEnd()
    if self.blackIcons is not None:
      oprot.writeFieldBegin('blackIcons', TType.BOOL, 3)
      oprot.writeBool(self.blackIcons)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class UserSettings(object):
  """
  Attributes:
   - network
   - desktop
   - rootFolder
  """

  __slots__ = [ 
    'network',
    'desktop',
    'rootFolder',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'network', (NetworkSettings, NetworkSettings.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'desktop', (DesktopSettings, DesktopSettings.thrift_spec), None, ), # 2
    (3, TType.STRING, 'rootFolder', None, None, ), # 3
  )

  def __init__(self, network=None, desktop=None, rootFolder=None,):
    self.network = network
    self.desktop = desktop
    self.rootFolder = rootFolder

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.network = NetworkSettings()
          self.network.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.desktop = DesktopSettings()
          self.desktop.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.rootFolder = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('UserSettings')
    if self.network is not None:
      oprot.writeFieldBegin('network', TType.STRUCT, 1)
      self.network.write(oprot)
      oprot.writeFieldEnd()
    if self.desktop is not None:
      oprot.writeFieldBegin('desktop', TType.STRUCT, 2)
      self.desktop.write(oprot)
      oprot.writeFieldEnd()
    if self.rootFolder is not None:
      oprot.writeFieldBegin('rootFolder', TType.STRING, 3)
      oprot.writeString(self.rootFolder)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)


class Account(object):
  """
  Attributes:
   - clientID
   - authKey
   - email
   - name
   - deviceName
  """

  __slots__ = [ 
    'clientID',
    'authKey',
    'email',
    'name',
    'deviceName',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'clientID', None, None, ), # 1
    (2, TType.STRING, 'authKey', None, None, ), # 2
    (3, TType.STRING, 'email', None, None, ), # 3
    (4, TType.STRING, 'name', None, None, ), # 4
    (5, TType.STRING, 'deviceName', None, None, ), # 5
  )

  def __init__(self, clientID=None, authKey=None, email=None, name=None, deviceName=None,):
    self.clientID = clientID
    self.authKey = authKey
    self.email = email
    self.name = name
    self.deviceName = deviceName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.clientID = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.authKey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.email = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.deviceName = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Account')
    if self.clientID is not None:
      oprot.writeFieldBegin('clientID', TType.STRING, 1)
      oprot.writeString(self.clientID)
      oprot.writeFieldEnd()
    if self.authKey is not None:
      oprot.writeFieldBegin('authKey', TType.STRING, 2)
      oprot.writeString(self.authKey)
      oprot.writeFieldEnd()
    if self.email is not None:
      oprot.writeFieldBegin('email', TType.STRING, 3)
      oprot.writeString(self.email)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 4)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.deviceName is not None:
      oprot.writeFieldBegin('deviceName', TType.STRING, 5)
      oprot.writeString(self.deviceName)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, getattr(self, key))
      for key in self.__slots__]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    for attr in self.__slots__:
      my_val = getattr(self, attr)
      other_val = getattr(other, attr)
      if my_val != other_val:
        return False
    return True

  def __ne__(self, other):
    return not (self == other)

