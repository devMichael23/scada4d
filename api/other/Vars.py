from imports.General import *
from api.other.SCADAVars import SCADAVar

varNoSecurity = [ua.SecurityPolicyType.NoSecurity]
varEventNotifier = ua.AttributeIds.EventNotifier
varSubscribeToEvents = ua.EventNotifier.SubscribeToEvents

double_t = ua.VariantType.Double
bool_t = ua.VariantType.Boolean
int64_t = ua.VariantType.Int64

scadaVars_t = dict[str, SCADAVar]

true_t = True
false_t = False

idManager = "manager"
idCurrentTemp = "currentTemp"
idHiTemp = "hiTemp"
idHiHiTemp = "hiHiTemp"
idLoTemp = "loTemp"
idLoLoTemp = "loLoTemp"
idIsServerHarmed = "isServerHarmed"
idFailureProbability = "failureProbability"
idRefrigerantActive = "refrigerantActive"
idIsOnCoolingWithServer = "isOnCoolingWithServer"