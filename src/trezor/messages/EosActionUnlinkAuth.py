# Automatically generated by pb2py
# fmt: off
import protobuf as p


class EosActionUnlinkAuth(p.MessageType):

    def __init__(
        self,
        account: int = None,
        code: int = None,
        type: int = None,
    ) -> None:
        self.account = account
        self.code = code
        self.type = type

    @classmethod
    def get_fields(cls):
        return {
            1: ('account', p.UVarintType, 0),
            2: ('code', p.UVarintType, 0),
            3: ('type', p.UVarintType, 0),
        }