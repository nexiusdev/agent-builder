"""Offline deliverable-contract checks, not identity or authorization verification."""
import json,sys
STATES={'planned','draft','in_review','changes_requested','accepted','released','delivered','superseded','withdrawn'}
def validate(data):
 if not isinstance(data,dict): return ['Deliverable must be an object']
 errors=[]
 for key in ['deliverable_id','version','title','owner_agent_id','format','acceptance_owner','handoff_workflow_id']:
  if not isinstance(data.get(key),str) or not data[key].strip(): errors.append('Missing/non-string '+key)
 for key in ['consumer_ids','acceptance_criteria']:
  if not isinstance(data.get(key),list) or not data[key] or not all(isinstance(x,str) and x.strip() for x in data[key]): errors.append('Invalid '+key)
 if not isinstance(data.get('evidence_refs'),list): errors.append('Invalid evidence_refs')
 if data.get('state') not in STATES: errors.append('Unknown state')
 if data.get('access') not in {'private','internal','restricted','public'}: errors.append('Unknown access classification')
 for key in ['artifact_ref','review_record','delivery_record']:
  value=data.get(key)
  if value is not None and (not isinstance(value,str) or not value.strip()): errors.append('Invalid '+key)
 if data.get('state') in {'accepted','released','delivered'}:
  for key in ['artifact_ref','review_record']:
   if not data.get(key): errors.append('Required for claimed acceptance: '+key)
 if data.get('state')=='delivered' and not data.get('delivery_record'): errors.append('Delivery evidence reference required')
 return errors
if __name__=='__main__':
 try: errors=validate(json.load(open(sys.argv[1])))
 except (OSError,ValueError,IndexError) as exc: errors=[str(exc)]
 print('\n'.join(errors) if errors else 'Contract structure valid; content, authority and delivery remain unverified.')
 sys.exit(bool(errors))
