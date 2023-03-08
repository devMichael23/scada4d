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

levelLogInfo_t = 10
levelLogDebug_t = 20
levelLogWarning_t = 30
levelLogError_t = 40
levelLogCritical_t = 50