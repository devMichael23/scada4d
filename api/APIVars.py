from api.APIImports import *

NoSecurity = [ua.SecurityPolicyType.NoSecurity]
EventNotifier = ua.AttributeIds.EventNotifier
SubscribeToEvents = ua.EventNotifier.SubscribeToEvents

double_t = ua.VariantType.Double
bool_t = ua.VariantType.Boolean
int64_t = ua.VariantType.Int64

true_t = 0.1
false_t = 0.00