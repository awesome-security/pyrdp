from enum import IntEnum


class ClientInfoFlags:
    """
    Flags for the RDPClientInfoPDU flags field
    """
    INFO_MOUSE = 0x00000001
    INFO_DISABLECTRLALTDEL = 0x00000002
    INFO_AUTOLOGON = 0x00000008
    INFO_UNICODE = 0x00000010
    INFO_MAXIMIZESHELL = 0x00000020
    INFO_LOGONNOTIFY = 0x00000040
    INFO_COMPRESSION = 0x00000080
    INFO_ENABLEWINDOWSKEY = 0x00000100
    INFO_REMOTECONSOLEAUDIO = 0x00002000
    INFO_FORCE_ENCRYPTED_CS_PDU = 0x00004000
    INFO_RAIL = 0x00008000
    INFO_LOGONERRORS = 0x00010000
    INFO_MOUSE_HAS_WHEEL = 0x00020000
    INFO_PASSWORD_IS_SC_PIN = 0x00040000
    INFO_NOAUDIOPLAYBACK = 0x00080000
    INFO_USING_SAVED_CREDS = 0x00100000
    INFO_AUDIOCAPTURE = 0x00200000
    INFO_VIDEO_DISABLE = 0x00400000
    INFO_CompressionTypeMask = 0x00001E00


class RDPSecurityFlags:
    SEC_EXCHANGE_PKT = 0x0001
    SEC_TRANSPORT_REQ = 0x0002
    SEC_TRANSPORT_RSP = 0x0004
    SEC_ENCRYPT = 0x0008
    SEC_RESET_SEQNO = 0x0010
    SEC_IGNORE_SEQNO = 0x0020
    SEC_INFO_PKT = 0x0040
    SEC_LICENSE_PKT = 0x0080
    SEC_LICENSE_ENCRYPT_CS = 0x0100
    SEC_LICENSE_ENCRYPT_SC = 0x0200
    SEC_REDIRECTION_PKT = 0x0400
    SEC_SECURE_CHECKSUM = 0x0800
    SEC_AUTODETECT_REQ = 0x1000
    SEC_AUTODETECT_RSP = 0x2000
    SEC_HEARTBEAT = 0x4000
    SEC_FLAGSHI_VALID = 0x8000


class RDPFastPathSecurityFlags:
    FASTPATH_OUTPUT_SECURE_CHECKSUM = 0x40
    FASTPATH_OUTPUT_ENCRYPTED = 0x80

class RDPFastPathInputEventType(IntEnum):
    FASTPATH_INPUT_EVENT_SCANCODE = 0
    FASTPATH_INPUT_EVENT_MOUSE = 1
    FASTPATH_INPUT_EVENT_MOUSEX = 2
    FASTPATH_INPUT_EVENT_SYNC = 3
    FASTPATH_INPUT_EVENT_UNICODE = 4
    FASTPATH_INPUT_EVENT_QOE_TIMESTAMP = 6


class RDPFastPathOutputEventType(IntEnum):
    FASTPATH_UPDATETYPE_ORDERS = 0
    FASTPATH_UPDATETYPE_BITMAP = 1
    FASTPATH_UPDATETYPE_PALETTE = 2
    FASTPATH_UPDATETYPE_SYNCHRONIZE = 3
    FASTPATH_UPDATETYPE_SURFCMDS = 4
    FASTPATH_UPDATETYPE_PTR_NULL = 5
    FASTPATH_UPDATETYPE_PTR_DEFAULT = 6
    FASTPATH_UPDATETYPE_PTR_POSITION = 8
    FASTPATH_UPDATETYPE_COLOR = 9
    FASTPATH_UPDATETYPE_CACHED = 10
    FASTPATH_UPDATETYPE_POINTER = 11

class FastPathOutputCompressionType(IntEnum):
    FASTPATH_OUTPUT_COMPRESSION_USED = 0x2

class SlowPathUpdateType(IntEnum):
    FASTPATH_UPDATETYPE_ORDERS = 0
    FASTPATH_UPDATETYPE_BITMAP = 1
    FASTPATH_UPDATETYPE_PALETTE = 2
    FASTPATH_UPDATETYPE_SYNCHRONIZE = 3

class RDPSecurityHeaderType(IntEnum):
    NONE = 0
    BASIC = 1
    SIGNED = 2
    FIPS = 3

    # Header type used for Client Info and Licensing PDUs if no encryption is used
    DEFAULT = 1


class FIPSVersion(IntEnum):
    TSFIPS_VERSION1 = 1


class RDPLicensingPDUType(IntEnum):
    LICENSE_REQUEST = 0x01
    PLATFORM_CHALLENGE = 0x02
    NEW_LICENSE = 0x03
    UPGRADE_LICENSE = 0x04
    LICENSE_INFO = 0x12
    NEW_LICENSE_REQUEST = 0x13
    PLATFORM_CHALLENGE_RESPONSE = 0x15
    ERROR_ALERT = 0xFF


class RDPLicenseBinaryBlobType(IntEnum):
    """
    License blob data type
    See http://msdn.microsoft.com/en-us/library/cc240481.aspx
    """
    BB_ANY_BLOB = 0x0000
    BB_DATA_BLOB = 0x0001
    BB_RANDOM_BLOB = 0x0002
    BB_CERTIFICATE_BLOB = 0x0003
    BB_ERROR_BLOB = 0x0004
    BB_ENCRYPTED_DATA_BLOB = 0x0009
    BB_KEY_EXCHG_ALG_BLOB = 0x000D
    BB_SCOPE_BLOB = 0x000E
    BB_CLIENT_USER_NAME_BLOB = 0x000F
    BB_CLIENT_MACHINE_NAME_BLOB = 0x0010


class RDPLicenseErrorCode(IntEnum):
    """
    @summary: License error message code
    @see: http://msdn.microsoft.com/en-us/library/cc240482.aspx
    """
    ERR_INVALID_SERVER_CERTIFICATE = 0x00000001
    ERR_NO_LICENSE = 0x00000002
    ERR_INVALID_SCOPE = 0x00000004
    ERR_NO_LICENSE_SERVER = 0x00000006
    STATUS_VALID_CLIENT = 0x00000007
    ERR_INVALID_CLIENT = 0x00000008
    ERR_INVALID_PRODUCTID = 0x0000000B
    ERR_INVALID_MESSAGE_LEN = 0x0000000C
    ERR_INVALID_MAC = 0x00000003


class RDPStateTransition(IntEnum):
    """
    Automata state transition
    See http://msdn.microsoft.com/en-us/library/cc240482.aspx
    """
    ST_TOTAL_ABORT = 0x00000001
    ST_NO_TRANSITION = 0x00000002
    ST_RESET_PHASE_TO_START = 0x00000003
    ST_RESEND_LAST_MESSAGE = 0x00000004


class RDPDataPDUType(IntEnum):
    """
    RDP Data PDU types
    @see: http://msdn.microsoft.com/en-us/library/cc240576.aspx
    """
    DEMAND_ACTIVE_PDU = 0x1
    CONFIRM_ACTIVE_PDU = 0x3
    DEACTIVATE_ALL_PDU = 0x6
    DATA_PDU = 0x7
    SERVER_REDIR_PKT_PDU = 0xA


class RDPDataPDUSubtype(IntEnum):
    """
    @summary: Data PDU type secondary index
    @see: http://msdn.microsoft.com/en-us/library/cc240577.aspx
    """
    PDUTYPE2_UPDATE = 0x02
    PDUTYPE2_CONTROL = 0x14
    PDUTYPE2_POINTER = 0x1B
    PDUTYPE2_INPUT = 0x1C
    PDUTYPE2_SYNCHRONIZE = 0x1F
    PDUTYPE2_REFRESH_RECT = 0x21
    PDUTYPE2_PLAY_SOUND = 0x22
    PDUTYPE2_SUPPRESS_OUTPUT = 0x23
    PDUTYPE2_SHUTDOWN_REQUEST = 0x24
    PDUTYPE2_SHUTDOWN_DENIED = 0x25
    PDUTYPE2_SAVE_SESSION_INFO = 0x26
    PDUTYPE2_FONTLIST = 0x27
    PDUTYPE2_FONTMAP = 0x28
    PDUTYPE2_SET_KEYBOARD_INDICATORS = 0x29
    PDUTYPE2_BITMAPCACHE_PERSISTENT_LIST = 0x2B
    PDUTYPE2_BITMAPCACHE_ERROR_PDU = 0x2C
    PDUTYPE2_SET_KEYBOARD_IME_STATUS = 0x2D
    PDUTYPE2_OFFSCRCACHE_ERROR_PDU = 0x2E
    PDUTYPE2_SET_ERROR_INFO_PDU = 0x2F
    PDUTYPE2_DRAWNINEGRID_ERROR_PDU = 0x30
    PDUTYPE2_DRAWGDIPLUS_ERROR_PDU = 0x31
    PDUTYPE2_ARC_STATUS_PDU = 0x32
    PDUTYPE2_STATUS_INFO_PDU = 0x36
    PDUTYPE2_MONITOR_LAYOUT_PDU = 0x37


class RDPConnectionDataType(IntEnum):
    SERVER_CORE = 0x0C01
    SERVER_SECURITY = 0x0C02
    SERVER_NETWORK = 0x0C03
    CLIENT_CORE = 0xC001
    CLIENT_SECURITY = 0xC002
    CLIENT_NETWORK = 0xC003
    CLIENT_CLUSTER = 0xC004
    CLIENT_MONITOR = 0xC005


class RDPVersion(IntEnum):
    RDP4 = 0x80001
    RDP5 = 0x80004
    RDP10 = 0x80005
    RDP10_1 = 0x80006
    RDP10_2 = 0x80007
    RDP10_3 = 0x80008
    RDP10_4 = 0x80009
    RDP10_5 = 0x8000A
    RDP10_6 = 0x8000B


class ColorDepth(IntEnum):
    RNS_UD_COLOR_4BPP = 0xCA00
    RNS_UD_COLOR_8BPP = 0xCA01
    RNS_UD_COLOR_16BPP_555 = 0xCA02
    RNS_UD_COLOR_16BPP_565 = 0xCA03
    RNS_UD_COLOR_24BPP = 0xCA04


class HighColorDepth(IntEnum):
    HIGH_COLOR_4BPP = 4
    HIGH_COLOR_8BPP = 8
    HIGH_COLOR_15BPP = 15
    HIGH_COLOR_16BPP = 16
    HIGH_COLOR_24BPP = 24


class KeyboardType(IntEnum):
    IBM_PC_XT = 1
    OLIVETTI = 2
    IBM_PC_AT = 3
    IBM_ENHANCED = 4
    NOKIA_1050 = 5
    NOKIA_9140 = 6
    JAPANESE = 7


class SupportedColorDepth:
    RNS_UD_24BPP_SUPPORT = 0x0001
    RNS_UD_16BPP_SUPPORT = 0x0002
    RNS_UD_15BPP_SUPPORT = 0x0004
    RNS_UD_32BPP_SUPPORT = 0x0008


class ClientCapabilityFlag:
    RNS_UD_CS_SUPPORT_ERRINFO_PDU = 0x0001
    RNS_UD_CS_WANT_32BPP_SESSION = 0x0002
    RNS_UD_CS_SUPPORT_STATUSINFO_PDU = 0x0004
    RNS_UD_CS_STRONG_ASYMMETRIC_KEYS = 0x0008
    RNS_UD_CS_UNUSED = 0x0010
    RNS_UD_CS_VALID_CONNECTION_TYPE = 0x0020
    RNS_UD_CS_SUPPORT_MONITOR_LAYOUT_PDU = 0x0040
    RNS_UD_CS_SUPPORT_NETCHAR_AUTODETECT = 0x0080
    RNS_UD_CS_SUPPORT_DYNVC_GFX_PROTOCOL = 0x0100
    RNS_UD_CS_SUPPORT_DYNAMIC_TIME_ZONE = 0x0200
    RNS_UD_CS_SUPPORT_HEARTBEAT_PDU = 0x0400


class ServerCapabilityFlag:
    RNS_UD_SC_EDGE_ACTIONS_SUPPORTED_V1 = 1
    RNS_UD_SC_DYNAMIC_DST_SUPPORTED = 2
    RNS_UD_SC_EDGE_ACTIONS_SUPPORTED_V2 = 4


class ConnectionType(IntEnum):
    CONNECTION_TYPE_UNKNOWN = 0x00
    CONNECTION_TYPE_MODEM = 0x01
    CONNECTION_TYPE_BROADBAND_LOW = 0x02
    CONNECTION_TYPE_SATELLITE = 0x03
    CONNECTION_TYPE_BROADBAND_HIGH = 0x04
    CONNECTION_TYPE_WAN = 0x05
    CONNECTION_TYPE_LAN = 0x06
    CONNECTION_TYPE_AUTODETECT = 0x07


class DesktopOrientation(IntEnum):
    ORIENTATION_LANDSCAPE = 0
    ORIENTATION_PORTRAIT = 90
    ORIENTATION_LANDSCAPE_FLIPPED = 180
    ORIENTATION_PORTRAIT_FLIPPED = 270


class EncryptionMethod(IntEnum):
    ENCRYPTION_NONE = 0x00
    ENCRYPTION_40BIT = 0x01
    ENCRYPTION_128BIT = 0x02
    ENCRYPTION_56BIT = 0x08
    ENCRYPTION_FIPS = 0x10


class EncryptionLevel(IntEnum):
    ENCRYPTION_LEVEL_NONE = 0
    ENCRYPTION_LEVEL_LOW = 1
    ENCRYPTION_LEVEL_CLIENT_COMPATIBLE = 2
    ENCRYPTION_LEVEL_HIGH = 3
    ENCRYPTION_LEVEL_FIPS = 4


class ClusterFlags(IntEnum):
    REDIRECTION_SUPPORTED = 0x01
    REDIRECTED_SESSIONID_FIELD_VALID = 0x02
    SERVER_SESSION_REDIRECTION_VERSION_MASK = 0x3C
    REDIRECTED_SMARTCARD = 0x40


class RedirectionVersion(IntEnum):
    REDIRECTION_VERSION1 = 0
    REDIRECTION_VERSION2 = 1
    REDIRECTION_VERSION3 = 2
    REDIRECTION_VERSION4 = 3
    REDIRECTION_VERSION5 = 4
    REDIRECTION_VERSION6 = 5


class ServerCertificateType(IntEnum):
    PROPRIETARY = 1
    X509 = 2


class NegotiationProtocols(IntEnum):
    NONE = 0
    SSL = 0b00000001
    CRED_SSP = 0b00000010
    EARLY_USER_AUTHORIZATION_RESULT = 0b00001000


class CapabilityType(IntEnum):
    CAPSTYPE_GENERAL = 0x0001
    CAPSTYPE_BITMAP = 0x0002
    CAPSTYPE_ORDER = 0x0003
    CAPSTYPE_BITMAPCACHE = 0x0004
    CAPSTYPE_CONTROL = 0x0005
    CAPSTYPE_ACTIVATION = 0x0007
    CAPSTYPE_POINTER = 0x0008
    CAPSTYPE_SHARE = 0x0009
    CAPSTYPE_COLORCACHE = 0x000A
    CAPSTYPE_SOUND = 0x000C
    CAPSTYPE_INPUT = 0x000D
    CAPSTYPE_FONT = 0x000E
    CAPSTYPE_BRUSH = 0x000F
    CAPSTYPE_GLYPHCACHE = 0x0010
    CAPSTYPE_OFFSCREENCACHE = 0x0011
    CAPSTYPE_BITMAPCACHE_HOSTSUPPORT = 0x0012
    CAPSTYPE_BITMAPCACHE_REV2 = 0x0013
    CAPSTYPE_VIRTUALCHANNEL = 0x0014
    CAPSTYPE_DRAWNINEGRIDCACHE = 0x0015
    CAPSTYPE_DRAWGDIPLUS = 0x0016
    CAPSTYPE_RAIL = 0x0017
    CAPSTYPE_WINDOW = 0x0018
    CAPSETTYPE_COMPDESK = 0x0019
    CAPSETTYPE_MULTIFRAGMENTUPDATE = 0x001A
    CAPSETTYPE_LARGE_POINTER = 0x001B
    CAPSETTYPE_SURFACE_COMMANDS = 0x001C
    CAPSETTYPE_BITMAP_CODECS = 0x001D
    CAPSSETTYPE_FRAME_ACKNOWLEDGE = 0x001E


class MajorType(IntEnum):
    OSMAJORTYPE_UNSPECIFIED = 0x0000
    OSMAJORTYPE_WINDOWS = 0x0001
    OSMAJORTYPE_OS2 = 0x0002
    OSMAJORTYPE_MACINTOSH = 0x0003
    OSMAJORTYPE_UNIX = 0x0004
    OSMAJORTYPE_IOS = 0x0005
    OSMAJORTYPE_OSX = 0x0006
    OSMAJORTYPE_ANDROID = 0x0007


class MinorType(IntEnum):
    OSMINORTYPE_UNSPECIFIED = 0x0000
    OSMINORTYPE_WINDOWS_31X = 0x0001
    OSMINORTYPE_WINDOWS_95 = 0x0002
    OSMINORTYPE_WINDOWS_NT = 0x0003
    OSMINORTYPE_OS2_V21 = 0x0004
    OSMINORTYPE_POWER_PC = 0x0005
    OSMINORTYPE_MACINTOSH = 0x0006
    OSMINORTYPE_NATIVE_XSERVER = 0x0007
    OSMINORTYPE_PSEUDO_XSERVER = 0x0008
    OSMINORTYPE_WINDOWS_RT = 0x0009


class GeneralExtraFlag:
    FASTPATH_OUTPUT_SUPPORTED = 0x0001
    NO_BITMAP_COMPRESSION_HDR = 0x0400
    LONG_CREDENTIALS_SUPPORTED = 0x0004
    AUTORECONNECT_SUPPORTED = 0x0008
    ENC_SALTED_CHECKSUM = 0x0010


class OrderFlag:
    NEGOTIATEORDERSUPPORT = 0x0002
    ZEROBOUNDSDELTASSUPPORT = 0x0008
    COLORINDEXSUPPORT = 0x0020
    SOLIDPATTERNBRUSHONLY = 0x0040
    ORDERFLAGS_EXTRA_FLAGS = 0x0080


class Order(IntEnum):
    TS_NEG_DSTBLT_INDEX = 0x00
    TS_NEG_PATBLT_INDEX = 0x01
    TS_NEG_SCRBLT_INDEX = 0x02
    TS_NEG_MEMBLT_INDEX = 0x03
    TS_NEG_MEM3BLT_INDEX = 0x04
    TS_NEG_DRAWNINEGRID_INDEX = 0x07
    TS_NEG_LINETO_INDEX = 0x08
    TS_NEG_MULTI_DRAWNINEGRID_INDEX = 0x09
    TS_NEG_SAVEBITMAP_INDEX = 0x0B
    TS_NEG_MULTIDSTBLT_INDEX = 0x0F
    TS_NEG_MULTIPATBLT_INDEX = 0x10
    TS_NEG_MULTISCRBLT_INDEX = 0x11
    TS_NEG_MULTIOPAQUERECT_INDEX = 0x12
    TS_NEG_FAST_INDEX_INDEX = 0x13
    TS_NEG_POLYGON_SC_INDEX = 0x14
    TS_NEG_POLYGON_CB_INDEX = 0x15
    TS_NEG_POLYLINE_INDEX = 0x16
    TS_NEG_FAST_GLYPH_INDEX = 0x18
    TS_NEG_ELLIPSE_SC_INDEX = 0x19
    TS_NEG_ELLIPSE_CB_INDEX = 0x1A
    TS_NEG_INDEX_INDEX = 0x1B


class OrderEx:
    ORDERFLAGS_EX_CACHE_BITMAP_REV3_SUPPORT = 0x0002
    ORDERFLAGS_EX_ALTSEC_FRAME_MARKER_SUPPORT = 0x0004


class InputFlags:
    INPUT_FLAG_SCANCODES = 0x0001
    INPUT_FLAG_MOUSEX = 0x0004
    INPUT_FLAG_FASTPATH_INPUT = 0x0008
    INPUT_FLAG_UNICODE = 0x0010
    INPUT_FLAG_FASTPATH_INPUT2 = 0x0020
    INPUT_FLAG_UNUSED1 = 0x0040
    INPUT_FLAG_UNUSED2 = 0x0080
    TS_INPUT_FLAG_MOUSE_HWHEEL = 0x0100


class BrushSupport(IntEnum):
    BRUSH_DEFAULT = 0x00000000
    BRUSH_COLOR_8x8 = 0x00000001
    BRUSH_COLOR_FULL = 0x00000002


class GlyphSupport(IntEnum):
    GLYPH_SUPPORT_NONE = 0x0000
    GLYPH_SUPPORT_PARTIAL = 0x0001
    GLYPH_SUPPORT_FULL = 0x0002
    GLYPH_SUPPORT_ENCODE = 0x0003


class OffscreenSupportLevel(IntEnum):
    FALSE = 0x00000000
    TRUE = 0x00000001


class VirtualChannelCompressionFlag:
    VCCAPS_NO_COMPR = 0x00000000
    VCCAPS_COMPR_SC = 0x00000001
    VCCAPS_COMPR_CS_8K = 0x00000002


class SoundFlag:
    NONE = 0x0000
    SOUND_BEEPS_FLAG = 0x0001


class ErrorInfo(IntEnum):
    ERRINFO_NONE = 0x00000000
    ERRINFO_RPC_INITIATED_DISCONNECT = 0x00000001
    ERRINFO_RPC_INITIATED_LOGOFF = 0x00000002
    ERRINFO_IDLE_TIMEOUT = 0x00000003
    ERRINFO_LOGON_TIMEOUT = 0x00000004
    ERRINFO_DISCONNECTED_BY_OTHERCONNECTION = 0x00000005
    ERRINFO_OUT_OF_MEMORY = 0x00000006
    ERRINFO_SERVER_DENIED_CONNECTION = 0x00000007
    ERRINFO_SERVER_INSUFFICIENT_PRIVILEGES = 0x00000009
    ERRINFO_SERVER_FRESH_CREDENTIALS_REQUIRED = 0x0000000A
    ERRINFO_RPC_INITIATED_DISCONNECT_BYUSER = 0x0000000B
    ERRINFO_LOGOFF_BY_USER = 0x0000000C
    ERRINFO_LICENSE_INTERNAL = 0x00000100
    ERRINFO_LICENSE_NO_LICENSE_SERVER = 0x00000101
    ERRINFO_LICENSE_NO_LICENSE = 0x00000102
    ERRINFO_LICENSE_BAD_CLIENT_MSG = 0x00000103
    ERRINFO_LICENSE_HWID_DOESNT_MATCH_LICENSE = 0x00000104
    ERRINFO_LICENSE_BAD_CLIENT_LICENSE = 0x00000105
    ERRINFO_LICENSE_CANT_FINISH_PROTOCOL = 0x00000106
    ERRINFO_LICENSE_CLIENT_ENDED_PROTOCOL = 0x00000107
    ERRINFO_LICENSE_BAD_CLIENT_ENCRYPTION = 0x00000108
    ERRINFO_LICENSE_CANT_UPGRADE_LICENSE = 0x00000109
    ERRINFO_LICENSE_NO_REMOTE_CONNECTIONS = 0x0000010A
    ERRINFO_CB_DESTINATION_NOT_FOUND = 0x0000400
    ERRINFO_CB_LOADING_DESTINATION = 0x0000402
    ERRINFO_CB_REDIRECTING_TO_DESTINATION = 0x0000404
    ERRINFO_CB_SESSION_ONLINE_VM_WAKE = 0x0000405
    ERRINFO_CB_SESSION_ONLINE_VM_BOOT = 0x0000406
    ERRINFO_CB_SESSION_ONLINE_VM_NO_DNS = 0x0000407
    ERRINFO_CB_DESTINATION_POOL_NOT_FREE = 0x0000408
    ERRINFO_CB_CONNECTION_CANCELLED = 0x0000409
    ERRINFO_CB_CONNECTION_ERROR_INVALID_SETTINGS = 0x0000410
    ERRINFO_CB_SESSION_ONLINE_VM_BOOT_TIMEOUT = 0x0000411
    ERRINFO_CB_SESSION_ONLINE_VM_SESSMON_FAILED = 0x0000412
    ERRINFO_UNKNOWNPDUTYPE2 = 0x000010C9
    ERRINFO_UNKNOWNPDUTYPE = 0x000010CA
    ERRINFO_DATAPDUSEQUENCE = 0x000010CB
    ERRINFO_CONTROLPDUSEQUENCE = 0x000010CD
    ERRINFO_INVALIDCONTROLPDUACTION = 0x000010CE
    ERRINFO_INVALIDINPUTPDUTYPE = 0x000010CF
    ERRINFO_INVALIDINPUTPDUMOUSE = 0x000010D0
    ERRINFO_INVALIDREFRESHRECTPDU = 0x000010D1
    ERRINFO_CREATEUSERDATAFAILED = 0x000010D2
    ERRINFO_CONNECTFAILED = 0x000010D3
    ERRINFO_CONFIRMACTIVEWRONGSHAREID = 0x000010D4
    ERRINFO_CONFIRMACTIVEWRONGORIGINATOR = 0x000010D5
    ERRINFO_PERSISTENTKEYPDUBADLENGTH = 0x000010DA
    ERRINFO_PERSISTENTKEYPDUILLEGALFIRST = 0x000010DB
    ERRINFO_PERSISTENTKEYPDUTOOMANYTOTALKEYS = 0x000010DC
    ERRINFO_PERSISTENTKEYPDUTOOMANYCACHEKEYS = 0x000010DD
    ERRINFO_INPUTPDUBADLENGTH = 0x000010DE
    ERRINFO_BITMAPCACHEERRORPDUBADLENGTH = 0x000010DF
    ERRINFO_SECURITYDATATOOSHORT = 0x000010E0
    ERRINFO_VCHANNELDATATOOSHORT = 0x000010E1
    ERRINFO_SHAREDATATOOSHORT = 0x000010E2
    ERRINFO_BADSUPRESSOUTPUTPDU = 0x000010E3
    ERRINFO_CONFIRMACTIVEPDUTOOSHORT = 0x000010E5
    ERRINFO_CAPABILITYSETTOOSMALL = 0x000010E7
    ERRINFO_CAPABILITYSETTOOLARGE = 0x000010E8
    ERRINFO_NOCURSORCACHE = 0x000010E9
    ERRINFO_BADCAPABILITIES = 0x000010EA
    ERRINFO_VIRTUALCHANNELDECOMPRESSIONERR = 0x000010EC
    ERRINFO_INVALIDVCCOMPRESSIONTYPE = 0x000010ED
    ERRINFO_INVALIDCHANNELID = 0x000010EF
    ERRINFO_VCHANNELSTOOMANY = 0x000010F0
    ERRINFO_REMOTEAPPSNOTENABLED = 0x000010F3
    ERRINFO_CACHECAPNOTSET = 0x000010F4
    ERRINFO_BITMAPCACHEERRORPDUBADLENGTH2 = 0x000010F5
    ERRINFO_OFFSCRCACHEERRORPDUBADLENGTH = 0x000010F6
    ERRINFO_DNGCACHEERRORPDUBADLENGTH = 0x000010F7
    ERRINFO_GDIPLUSPDUBADLENGTH = 0x000010F8
    ERRINFO_SECURITYDATATOOSHORT2 = 0x00001111
    ERRINFO_SECURITYDATATOOSHORT3 = 0x00001112
    ERRINFO_SECURITYDATATOOSHORT4 = 0x00001113
    ERRINFO_SECURITYDATATOOSHORT5 = 0x00001114
    ERRINFO_SECURITYDATATOOSHORT6 = 0x00001115
    ERRINFO_SECURITYDATATOOSHORT7 = 0x00001116
    ERRINFO_SECURITYDATATOOSHORT8 = 0x00001117
    ERRINFO_SECURITYDATATOOSHORT9 = 0x00001118
    ERRINFO_SECURITYDATATOOSHORT10 = 0x00001119
    ERRINFO_SECURITYDATATOOSHORT11 = 0x0000111A
    ERRINFO_SECURITYDATATOOSHORT12 = 0x0000111B
    ERRINFO_SECURITYDATATOOSHORT13 = 0x0000111C
    ERRINFO_SECURITYDATATOOSHORT14 = 0x0000111D
    ERRINFO_SECURITYDATATOOSHORT15 = 0x0000111E
    ERRINFO_SECURITYDATATOOSHORT16 = 0x0000111F
    ERRINFO_SECURITYDATATOOSHORT17 = 0x00001120
    ERRINFO_SECURITYDATATOOSHORT18 = 0x00001121
    ERRINFO_SECURITYDATATOOSHORT19 = 0x00001122
    ERRINFO_SECURITYDATATOOSHORT20 = 0x00001123
    ERRINFO_SECURITYDATATOOSHORT21 = 0x00001124
    ERRINFO_SECURITYDATATOOSHORT22 = 0x00001125
    ERRINFO_SECURITYDATATOOSHORT23 = 0x00001126
    ERRINFO_BADMONITORDATA = 0x00001129
    ERRINFO_VCDECOMPRESSEDREASSEMBLEFAILED = 0x0000112A
    ERRINFO_VCDATATOOLONG = 0x0000112B
    ERRINFO_BAD_FRAME_ACK_DATA = 0x0000112C
    ERRINFO_GRAPHICSMODENOTSUPPORTED = 0x0000112D
    ERRINFO_GRAPHICSSUBSYSTEMRESETFAILED = 0x0000112E
    ERRINFO_GRAPHICSSUBSYSTEMFAILED = 0x0000112F
    ERRINFO_TIMEZONEKEYNAMELENGTHTOOSHORT = 0x00001130
    ERRINFO_TIMEZONEKEYNAMELENGTHTOOLONG = 0x00001131
    ERRINFO_DYNAMICDSTDISABLEDFIELDMISSING = 0x00001132
    ERRINFO_VCDECODINGERROR = 0x00001133
    ERRINFO_UPDATESESSIONKEYFAILED = 0x00001191
    ERRINFO_DECRYPTFAILED = 0x00001192
    ERRINFO_ENCRYPTFAILED = 0x00001193
    ERRINFO_ENCPKGMISMATCH = 0x00001194
    ERRINFO_DECRYPTFAILED2 = 0x00001195


class InputEventType(IntEnum):
    """
    Slow-path input message type
    See: http://msdn.microsoft.com/en-us/library/cc240583.aspx
    """
    INPUT_EVENT_SYNC = 0x0000
    INPUT_EVENT_UNUSED = 0x0002
    INPUT_EVENT_SCANCODE = 0x0004
    INPUT_EVENT_UNICODE = 0x0005
    INPUT_EVENT_MOUSE = 0x8001
    INPUT_EVENT_MOUSEX = 0x8002


class SynchronizeFlag(IntEnum):
    TS_SYNC_SCROLL_LOCK = 0x00000001
    TS_SYNC_NUM_LOCK = 0x00000002
    TS_SYNC_CAPS_LOCK = 0x00000004
    TS_SYNC_KANA_LOCK = 0x00000008


class KeyboardFlag(IntEnum):
    KBDFLAGS_EXTENDED = 0x0100
    KBDFLAGS_DOWN = 0x4000
    KBDFLAGS_RELEASE = 0x8000


class PointerFlag(IntEnum):
    PTRFLAGS_WHEEL_NEGATIVE = 0x0100
    PTRFLAGS_WHEEL = 0x0200
    PTRFLAGS_HWHEEL = 0x0400
    WheelRotationMask = 0x01FF

    PTRFLAGS_MOVE = 0x0800

    PTRFLAGS_BUTTON1 = 0x1000
    PTRFLAGS_BUTTON2 = 0x2000
    PTRFLAGS_BUTTON3 = 0x4000
    PTRFLAGS_DOWN = 0x8000

    PTRXFLAGS_BUTTON1 = 0x0001
    PTRXFLAGS_BUTTON2 = 0x0002


class PointerEventType(IntEnum):
    TS_PTRMSGTYPE_SYSTEM = 0x0001
    TS_PTRMSGTYPE_POSITION = 0x0003
    TS_PTRMSGTYPE_COLOR = 0x0006
    TS_PTRMSGTYPE_CACHED = 0x0007
    TS_PTRMSGTYPE_POINTER = 0x0008


class RDPPlayerMessageType(IntEnum):
    """
    Types of events that we can encounter when replaying a RDP connection.
    """

    FAST_PATH_INPUT = 1  # Ex: scancode, mouse
    FAST_PATH_OUTPUT = 2  # Ex: image
    CLIENT_INFO = 3  # Creds on connection
    SLOW_PATH_PDU = 4  # For slow-path PDUs
    CONNECTION_CLOSE = 5  # To advertise the end of the connection
    CLIPBOARD_DATA = 6  # To collect clipboard data


class ChannelOption(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc240513.aspx
    """

    CHANNEL_OPTION_INITIALIZED = 0x80000000
    CHANNEL_OPTION_ENCRYPT_RDP = 0x40000000
    CHANNEL_OPTION_ENCRYPT_SC = 0x20000000
    CHANNEL_OPTION_ENCRYPT_CS = 0x10000000
    CHANNEL_OPTION_PRI_HIGH = 0x08000000
    CHANNEL_OPTION_PRI_MED = 0x04000000
    CHANNEL_OPTION_PRI_LOW = 0x02000000
    CHANNEL_OPTION_COMPRESS_RDP = 0x00800000
    CHANNEL_OPTION_COMPRESS = 0x00400000
    CHANNEL_OPTION_SHOW_PROTOCOL = 0x00200000
    REMOTE_CONTROL_PERSISTENT = 0x00100000


class DrawingOrderControlFlags(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc241574.aspx
    """
    TS_STANDARD = 0b00000001
    TS_SECONDARY = 0b00000010


class RdpVersion(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc240517.aspx
    """
    RDP_4_0 = 0x00080001
    RDP_5_TO_8_1 = 0x00080004

class BitmapFlags(IntEnum):
    """
    https://msdn.microsoft.com/en-us/library/cc240612.aspx
    """
    BITMAP_COMPRESSION = 0x0001
    NO_BITMAP_COMPRESSION_HDR = 0x0400