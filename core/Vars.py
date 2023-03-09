import asyncio
from asyncua import ua

from core.SCADAVars import SCADAVar

varNoSecurity = [ua.SecurityPolicyType.NoSecurity]
varEventNotifier = ua.AttributeIds.EventNotifier
varSubscribeToEvents = ua.EventNotifier.SubscribeToEvents

cancelledException_t = asyncio.CancelledError

double_t = ua.VariantType.Double
bool_t = ua.VariantType.Boolean
int64_t = ua.VariantType.Int64

scadaVars_t = dict[str, SCADAVar]

true_t = True
false_t = False

idCore = "core"
idCurrentTemp = "currentTemp"
idHiTemp = "hiTemp"
idHiHiTemp = "hiHiTemp"
idLoTemp = "loTemp"
idLoLoTemp = "loLoTemp"
idIsServerHarmed = "isServerHarmed"
idFailureProbability = "failureProbability"
idRefrigerantActive = "refrigerantActive"
idIsOnCoolingWithServer = "isOnCoolingWithServer"

valCurrentTemp = 50
valHiTemp = 70
valHiHiTemp = 90
valLoTemp = 40
valLoLoTemp = 25
valIsServerHarmed = false_t
valFailureProbability = 10
valRefrigerantActive = false_t
valIsOnCoolingWithServer = false_t

levelLogInfo_t = 10
levelLogDebug_t = 20
levelLogWarning_t = 30
levelLogError_t = 40
levelLogCritical_t = 50
levelLogAll_t = levelLogCritical_t

timeToChangeTemp = 0.1
timeToGetFailureProbability = 10
timeWaitBeforeServerHarmed = 3