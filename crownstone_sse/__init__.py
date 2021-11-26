"""Init file for Crownstone SSE."""
from crownstone_sse.async_client import CrownstoneSSEAsync
from crownstone_sse.client import CrownstoneSSE

# include all possible event types in the top level
from crownstone_sse.const import (
    EVENT_ABILITY_CHANGE,
    EVENT_ABILITY_CHANGE_DIMMING,
    EVENT_ABILITY_CHANGE_SWITCHCRAFT,
    EVENT_ABILITY_CHANGE_TAP_TO_TOGGLE,
    EVENT_COMMAND,
    EVENT_COMMAND_SWITCH_MULTIPLE_CROWNSTONES,
    EVENT_DATA_CHANGE,
    EVENT_DATA_CHANGE_CROWNSTONE,
    EVENT_DATA_CHANGE_LOCATIONS,
    EVENT_DATA_CHANGE_SPHERES,
    EVENT_DATA_CHANGE_USERS,
    EVENT_PING,
    EVENT_PRESENCE,
    EVENT_PRESENCE_ENTER_LOCATION,
    EVENT_PRESENCE_ENTER_SPHERE,
    EVENT_PRESENCE_EXIT_LOCATION,
    EVENT_PRESENCE_EXIT_SPHERE,
    EVENT_SWITCH_STATE_UPDATE,
    EVENT_SWITCH_STATE_UPDATE_CROWNSTONE,
    EVENT_SYSTEM,
    EVENT_SYSTEM_NO_ACCESS_TOKEN,
    EVENT_SYSTEM_NO_CONNECTION,
    EVENT_SYSTEM_STREAM_CLOSED,
    EVENT_SYSTEM_STREAM_START,
    EVENT_SYSTEM_TOKEN_EXPIRED,
    OPERATION_CREATE,
    OPERATION_DELETE,
    OPERATION_UPDATE,
)
from crownstone_sse.util.eventbus import EventBus

__version__ = "2.0.3-git"
