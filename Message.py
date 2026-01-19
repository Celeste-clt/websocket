from Message import Message, MessageType

class Message: 
       def __init__(self, type:MessageType, emitter, content, receiver=None):
           self.emitter = emitter
           self.content = content
           self.receiver = receiver
           self.type = type

@staticmethod
def default_message():
    return Message("System", "This is a defalut message", "All")

# @staticmethod
# def from_json(json_data):
#     import json
#     ""
#     {
#     "message_type": "MESSAGE_TYPE",
#     "data": {
#       "emitter": "EMITTER",
#       "recept": "RECEPT",
#       "value": "VALUE"
#     }
# }

# ""

@staticmethod
def from_json(json_data):
      import json
      data = json.loads(json_data)
      type = data['message_type']
      emitter = data['data']['emitter']
      content = data['data']['value']
      receiver = data['data']['emitter']
      return Message(type, emitter, content, receiver)


def to_json(message):
    import json
    data = {
        'message_type' : message.type,
        'data': {
            'emitteur': message.emitter,
            'value': message.content,
            'recept': message.receiver
        }}
    

message = Message(MessageType.DECLARATION,
                  emitter="System", 
                  content="This is a default message", 
                  dest="All")

messagerebuild = Message.from_json(message.tojson())
assert message.to_json() == messagerebuild.to_json()