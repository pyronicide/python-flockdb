#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class SelectOperationType:
  SimpleQuery = 1
  Intersection = 2
  Union = 3
  Difference = 4

  _VALUES_TO_NAMES = {
    1: "SimpleQuery",
    2: "Intersection",
    3: "Union",
    4: "Difference",
  }

  _NAMES_TO_VALUES = {
    "SimpleQuery": 1,
    "Intersection": 2,
    "Union": 3,
    "Difference": 4,
  }

class ExecuteOperationType:
  Add = 1
  Remove = 2
  Archive = 3
  Negate = 4

  _VALUES_TO_NAMES = {
    1: "Add",
    2: "Remove",
    3: "Archive",
    4: "Negate",
  }

  _NAMES_TO_VALUES = {
    "Add": 1,
    "Remove": 2,
    "Archive": 3,
    "Negate": 4,
  }

class EdgeState:
  Positive = 0
  Negative = 3
  Removed = 1
  Archived = 2

  _VALUES_TO_NAMES = {
    0: "Positive",
    3: "Negative",
    1: "Removed",
    2: "Archived",
  }

  _NAMES_TO_VALUES = {
    "Positive": 0,
    "Negative": 3,
    "Removed": 1,
    "Archived": 2,
  }

class Priority:
  Low = 1
  Medium = 2
  High = 3

  _VALUES_TO_NAMES = {
    1: "Low",
    2: "Medium",
    3: "High",
  }

  _NAMES_TO_VALUES = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
  }


class FlockException(Exception):
  """
  Attributes:
   - description
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'description', None, None, ), # 1
  )

  def __init__(self, description=None,):
    self.description = description

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
          self.description = iprot.readString();
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
    oprot.writeStructBegin('FlockException')
    if self.description != None:
      oprot.writeFieldBegin('description', TType.STRING, 1)
      oprot.writeString(self.description)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Results:
  """
  Attributes:
   - ids
   - next_cursor
   - prev_cursor
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'ids', None, None, ), # 1
    (2, TType.I64, 'next_cursor', None, None, ), # 2
    (3, TType.I64, 'prev_cursor', None, None, ), # 3
  )

  def __init__(self, ids=None, next_cursor=None, prev_cursor=None,):
    self.ids = ids
    self.next_cursor = next_cursor
    self.prev_cursor = prev_cursor

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
          self.ids = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.next_cursor = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.prev_cursor = iprot.readI64();
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
    oprot.writeStructBegin('Results')
    if self.ids != None:
      oprot.writeFieldBegin('ids', TType.STRING, 1)
      oprot.writeString(self.ids)
      oprot.writeFieldEnd()
    if self.next_cursor != None:
      oprot.writeFieldBegin('next_cursor', TType.I64, 2)
      oprot.writeI64(self.next_cursor)
      oprot.writeFieldEnd()
    if self.prev_cursor != None:
      oprot.writeFieldBegin('prev_cursor', TType.I64, 3)
      oprot.writeI64(self.prev_cursor)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Page:
  """
  Attributes:
   - count
   - cursor
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'count', None, None, ), # 1
    (2, TType.I64, 'cursor', None, None, ), # 2
  )

  def __init__(self, count=None, cursor=None,):
    self.count = count
    self.cursor = cursor

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
          self.count = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.cursor = iprot.readI64();
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
    oprot.writeStructBegin('Page')
    if self.count != None:
      oprot.writeFieldBegin('count', TType.I32, 1)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    if self.cursor != None:
      oprot.writeFieldBegin('cursor', TType.I64, 2)
      oprot.writeI64(self.cursor)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Metadata:
  """
  Attributes:
   - source_id
   - state_id
   - count
   - updated_at
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'source_id', None, None, ), # 1
    (2, TType.I32, 'state_id', None, None, ), # 2
    (3, TType.I32, 'count', None, None, ), # 3
    (4, TType.I32, 'updated_at', None, None, ), # 4
  )

  def __init__(self, source_id=None, state_id=None, count=None, updated_at=None,):
    self.source_id = source_id
    self.state_id = state_id
    self.count = count
    self.updated_at = updated_at

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
        if ftype == TType.I64:
          self.source_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.state_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.count = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.updated_at = iprot.readI32();
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
    oprot.writeStructBegin('Metadata')
    if self.source_id != None:
      oprot.writeFieldBegin('source_id', TType.I64, 1)
      oprot.writeI64(self.source_id)
      oprot.writeFieldEnd()
    if self.state_id != None:
      oprot.writeFieldBegin('state_id', TType.I32, 2)
      oprot.writeI32(self.state_id)
      oprot.writeFieldEnd()
    if self.count != None:
      oprot.writeFieldBegin('count', TType.I32, 3)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    if self.updated_at != None:
      oprot.writeFieldBegin('updated_at', TType.I32, 4)
      oprot.writeI32(self.updated_at)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Edge:
  """
  Attributes:
   - source_id
   - destination_id
   - position
   - updated_at
   - count
   - state_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'source_id', None, None, ), # 1
    (2, TType.I64, 'destination_id', None, None, ), # 2
    (3, TType.I64, 'position', None, None, ), # 3
    (4, TType.I32, 'updated_at', None, None, ), # 4
    (5, TType.I32, 'count', None, None, ), # 5
    (6, TType.I32, 'state_id', None, None, ), # 6
  )

  def __init__(self, source_id=None, destination_id=None, position=None, updated_at=None, count=None, state_id=None,):
    self.source_id = source_id
    self.destination_id = destination_id
    self.position = position
    self.updated_at = updated_at
    self.count = count
    self.state_id = state_id

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
        if ftype == TType.I64:
          self.source_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.destination_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.position = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.updated_at = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.count = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.state_id = iprot.readI32();
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
    oprot.writeStructBegin('Edge')
    if self.source_id != None:
      oprot.writeFieldBegin('source_id', TType.I64, 1)
      oprot.writeI64(self.source_id)
      oprot.writeFieldEnd()
    if self.destination_id != None:
      oprot.writeFieldBegin('destination_id', TType.I64, 2)
      oprot.writeI64(self.destination_id)
      oprot.writeFieldEnd()
    if self.position != None:
      oprot.writeFieldBegin('position', TType.I64, 3)
      oprot.writeI64(self.position)
      oprot.writeFieldEnd()
    if self.updated_at != None:
      oprot.writeFieldBegin('updated_at', TType.I32, 4)
      oprot.writeI32(self.updated_at)
      oprot.writeFieldEnd()
    if self.count != None:
      oprot.writeFieldBegin('count', TType.I32, 5)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    if self.state_id != None:
      oprot.writeFieldBegin('state_id', TType.I32, 6)
      oprot.writeI32(self.state_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryTerm:
  """
  Attributes:
   - source_id
   - graph_id
   - is_forward
   - destination_ids
   - state_ids
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'source_id', None, None, ), # 1
    (2, TType.I32, 'graph_id', None, None, ), # 2
    (3, TType.BOOL, 'is_forward', None, None, ), # 3
    (4, TType.STRING, 'destination_ids', None, None, ), # 4
    (5, TType.LIST, 'state_ids', (TType.I32,None), None, ), # 5
  )

  def __init__(self, source_id=None, graph_id=None, is_forward=None, destination_ids=None, state_ids=None,):
    self.source_id = source_id
    self.graph_id = graph_id
    self.is_forward = is_forward
    self.destination_ids = destination_ids
    self.state_ids = state_ids

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
        if ftype == TType.I64:
          self.source_id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.graph_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.is_forward = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.destination_ids = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.state_ids = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32();
            self.state_ids.append(_elem5)
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
    oprot.writeStructBegin('QueryTerm')
    if self.source_id != None:
      oprot.writeFieldBegin('source_id', TType.I64, 1)
      oprot.writeI64(self.source_id)
      oprot.writeFieldEnd()
    if self.graph_id != None:
      oprot.writeFieldBegin('graph_id', TType.I32, 2)
      oprot.writeI32(self.graph_id)
      oprot.writeFieldEnd()
    if self.is_forward != None:
      oprot.writeFieldBegin('is_forward', TType.BOOL, 3)
      oprot.writeBool(self.is_forward)
      oprot.writeFieldEnd()
    if self.destination_ids != None:
      oprot.writeFieldBegin('destination_ids', TType.STRING, 4)
      oprot.writeString(self.destination_ids)
      oprot.writeFieldEnd()
    if self.state_ids != None:
      oprot.writeFieldBegin('state_ids', TType.LIST, 5)
      oprot.writeListBegin(TType.I32, len(self.state_ids))
      for iter6 in self.state_ids:
        oprot.writeI32(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SelectOperation:
  """
  Attributes:
   - operation_type
   - term
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'operation_type', None, None, ), # 1
    (2, TType.STRUCT, 'term', (QueryTerm, QueryTerm.thrift_spec), None, ), # 2
  )

  def __init__(self, operation_type=None, term=None,):
    self.operation_type = operation_type
    self.term = term

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
          self.operation_type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.term = QueryTerm()
          self.term.read(iprot)
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
    oprot.writeStructBegin('SelectOperation')
    if self.operation_type != None:
      oprot.writeFieldBegin('operation_type', TType.I32, 1)
      oprot.writeI32(self.operation_type)
      oprot.writeFieldEnd()
    if self.term != None:
      oprot.writeFieldBegin('term', TType.STRUCT, 2)
      self.term.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExecuteOperation:
  """
  Attributes:
   - operation_type
   - term
   - position
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'operation_type', None, None, ), # 1
    (2, TType.STRUCT, 'term', (QueryTerm, QueryTerm.thrift_spec), None, ), # 2
    (3, TType.I64, 'position', None, None, ), # 3
  )

  def __init__(self, operation_type=None, term=None, position=None,):
    self.operation_type = operation_type
    self.term = term
    self.position = position

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
          self.operation_type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.term = QueryTerm()
          self.term.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.position = iprot.readI64();
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
    oprot.writeStructBegin('ExecuteOperation')
    if self.operation_type != None:
      oprot.writeFieldBegin('operation_type', TType.I32, 1)
      oprot.writeI32(self.operation_type)
      oprot.writeFieldEnd()
    if self.term != None:
      oprot.writeFieldBegin('term', TType.STRUCT, 2)
      self.term.write(oprot)
      oprot.writeFieldEnd()
    if self.position != None:
      oprot.writeFieldBegin('position', TType.I64, 3)
      oprot.writeI64(self.position)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ExecuteOperations:
  """
  Attributes:
   - operations
   - execute_at
   - priority
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'operations', (TType.STRUCT,(ExecuteOperation, ExecuteOperation.thrift_spec)), None, ), # 1
    (2, TType.I32, 'execute_at', None, None, ), # 2
    (3, TType.I32, 'priority', None, None, ), # 3
  )

  def __init__(self, operations=None, execute_at=None, priority=None,):
    self.operations = operations
    self.execute_at = execute_at
    self.priority = priority

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
        if ftype == TType.LIST:
          self.operations = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = ExecuteOperation()
            _elem12.read(iprot)
            self.operations.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.execute_at = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.priority = iprot.readI32();
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
    oprot.writeStructBegin('ExecuteOperations')
    if self.operations != None:
      oprot.writeFieldBegin('operations', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.operations))
      for iter13 in self.operations:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.execute_at != None:
      oprot.writeFieldBegin('execute_at', TType.I32, 2)
      oprot.writeI32(self.execute_at)
      oprot.writeFieldEnd()
    if self.priority != None:
      oprot.writeFieldBegin('priority', TType.I32, 3)
      oprot.writeI32(self.priority)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SelectQuery:
  """
  Attributes:
   - operations
   - page
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'operations', (TType.STRUCT,(SelectOperation, SelectOperation.thrift_spec)), None, ), # 1
    (2, TType.STRUCT, 'page', (Page, Page.thrift_spec), None, ), # 2
  )

  def __init__(self, operations=None, page=None,):
    self.operations = operations
    self.page = page

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
        if ftype == TType.LIST:
          self.operations = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = SelectOperation()
            _elem19.read(iprot)
            self.operations.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.page = Page()
          self.page.read(iprot)
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
    oprot.writeStructBegin('SelectQuery')
    if self.operations != None:
      oprot.writeFieldBegin('operations', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.operations))
      for iter20 in self.operations:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.page != None:
      oprot.writeFieldBegin('page', TType.STRUCT, 2)
      self.page.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EdgeQuery:
  """
  Attributes:
   - term
   - page
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'term', (QueryTerm, QueryTerm.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'page', (Page, Page.thrift_spec), None, ), # 2
  )

  def __init__(self, term=None, page=None,):
    self.term = term
    self.page = page

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
          self.term = QueryTerm()
          self.term.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.page = Page()
          self.page.read(iprot)
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
    oprot.writeStructBegin('EdgeQuery')
    if self.term != None:
      oprot.writeFieldBegin('term', TType.STRUCT, 1)
      self.term.write(oprot)
      oprot.writeFieldEnd()
    if self.page != None:
      oprot.writeFieldBegin('page', TType.STRUCT, 2)
      self.page.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EdgeResults:
  """
  Attributes:
   - edges
   - next_cursor
   - prev_cursor
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'edges', (TType.STRUCT,(Edge, Edge.thrift_spec)), None, ), # 1
    (2, TType.I64, 'next_cursor', None, None, ), # 2
    (3, TType.I64, 'prev_cursor', None, None, ), # 3
  )

  def __init__(self, edges=None, next_cursor=None, prev_cursor=None,):
    self.edges = edges
    self.next_cursor = next_cursor
    self.prev_cursor = prev_cursor

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
        if ftype == TType.LIST:
          self.edges = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = Edge()
            _elem26.read(iprot)
            self.edges.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.next_cursor = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.prev_cursor = iprot.readI64();
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
    oprot.writeStructBegin('EdgeResults')
    if self.edges != None:
      oprot.writeFieldBegin('edges', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.edges))
      for iter27 in self.edges:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.next_cursor != None:
      oprot.writeFieldBegin('next_cursor', TType.I64, 2)
      oprot.writeI64(self.next_cursor)
      oprot.writeFieldEnd()
    if self.prev_cursor != None:
      oprot.writeFieldBegin('prev_cursor', TType.I64, 3)
      oprot.writeI64(self.prev_cursor)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
