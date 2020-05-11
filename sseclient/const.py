"""Constants for the Crownstone Cloud lib"""
from datetime import timedelta

# URLs
EVENT_BASE_URL = "https://events.crownstone.rocks/sse?accessToken="
LOGIN_URL = "https://cloud.crownstone.rocks/api/users/login"

# SSE client
EVENT_CLIENT_STOP = "client_stop"
RECONNECTION_TIME = timedelta(seconds=5)
MAX_CONNECT_RETRY = 5

# SSE System events
EVENT_SYSTEM = "system"
EVENT_SYSTEM_TOKEN_EXPIRED = 'TOKEN_EXPIRED'
EVENT_SYSTEM_NO_ACCESS_TOKEN = "NO_ACCESS_TOKEN"
EVENT_SYSTEM_NO_CONNECTION = "NO_CONNECTION"
EVENT_SYSTEM_STREAM_START = "STREAM_START"
EVENT_SYSTEM_STREAM_CLOSE = "STREAM_CLOSE"

# SSE dataChange events
EVENT_DATA_CHANGE = "data_change"
EVENT_DATA_CHANGE_CROWNSTONE = "stones"
EVENT_DATA_CHANGE_SPHERES = "spheres"
EVENT_DATA_CHANGE_USERS = "users"
EVENT_DATA_CHANGE_LOCATIONS = "locations"

# dataChange operations
OPERATION_CREATE = "create"
OPERATION_DELETE = "delete"
OPERATION_UPDATE = "update"

# SwitchState update events
EVENT_SWITCH_STATE_UPDATE = "switchStateUpdate"

# SSE command events
EVENT_COMMAND = "command"
EVENT_COMMAND_SWITCH_CROWNSTONE = "switchCrownstone"

# SSE presence events
EVENT_PRESENCE_ENTER_SPHERE = "enterSphere"
EVENT_PRESENCE_EXIT_SPHERE = "exitSphere"
EVENT_PRESENCE_ENTER_LOCATION = "enterLocation"
EVENT_PRESENCE_EXIT_LOCATION = "exitLocation"

# lists for iteration
system_events = [
    EVENT_SYSTEM_TOKEN_EXPIRED,
    EVENT_SYSTEM_NO_ACCESS_TOKEN,
    EVENT_SYSTEM_NO_CONNECTION,
    EVENT_SYSTEM_STREAM_START,
    EVENT_SYSTEM_STREAM_CLOSE
]

presence_events = [
    EVENT_PRESENCE_ENTER_SPHERE,
    EVENT_PRESENCE_EXIT_SPHERE,
    EVENT_PRESENCE_ENTER_LOCATION,
    EVENT_PRESENCE_EXIT_LOCATION
]

data_change_events = [
    EVENT_DATA_CHANGE_USERS,
    EVENT_DATA_CHANGE_SPHERES,
    EVENT_DATA_CHANGE_CROWNSTONE,
    EVENT_DATA_CHANGE_LOCATIONS,
]

command_events = [
    EVENT_COMMAND_SWITCH_CROWNSTONE
]

operations = [
    OPERATION_UPDATE,
    OPERATION_CREATE,
    OPERATION_DELETE
]

