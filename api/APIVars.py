from api.APIImports import *
from api.APISCADAVars import SCADAVar

NoSecurity = [ua.SecurityPolicyType.NoSecurity]
EventNotifier = ua.AttributeIds.EventNotifier
SubscribeToEvents = ua.EventNotifier.SubscribeToEvents

double_t = ua.VariantType.Double
bool_t = ua.VariantType.Boolean
int64_t = ua.VariantType.Int64

serverValues_t = dict[str, SCADAVar]

true_t = 0.1
false_t = 0.00

manager_d = "manager"
currentTemp_d = "currentTemp"
hiTemp_d = "hiTemp"
hiHiTemp_d = "hiHiTemp"
loTemp_d = "loTemp"
loLoTemp_d = "loLoTemp"
isServerHarmed_d = "isServerHarmed"
failureProbability_d = "failureProbability"
refrigerantActive_d = "refrigerantActive"
isOnCoolingWithServer_d = "isOnCoolingWithServer"