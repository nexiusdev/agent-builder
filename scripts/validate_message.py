"""Offline envelope linting only. Not an authorization or transport service."""
import json,sys
TYPES={'request','assignment','acknowledgement','progress','result','question','dissent','escalation','cancellation'}
STATES={'queued','delivered','acknowledged','accepted','running','result_submitted','verified','closed','rejected','blocked','failed','cancellation_requested','cancelled'}
def validate(data):
 if not isinstance(data,dict): return ['Message must be an object']
 errors=[]
 for key in ['message_id','sender_agent_id','recipient_agent_id','workflow_id','run_id','scope','plan_version','idempotency_key','expected_outcome','summary']:
  if not isinstance(data.get(key),str) or not data[key].strip(): errors.append('Missing/non-string '+key)
 if data.get('type') not in TYPES: errors.append('Unknown type')
 if data.get('state') not in STATES: errors.append('Unknown state')
 if not isinstance(data.get('evidence_refs'),list) or not all(isinstance(x,str) and x.strip() for x in data.get('evidence_refs',[])): errors.append('Invalid evidence_refs')
 return errors
if __name__=='__main__':
 try: errors=validate(json.load(open(sys.argv[1])))
 except (OSError,ValueError,IndexError) as exc: errors=[str(exc)]
 print('\n'.join(errors) if errors else 'Envelope valid; delivery, authority and evidence remain unverified.')
 sys.exit(bool(errors))
