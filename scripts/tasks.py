"""Local single-file task updates with lock and optimistic revision check."""
import json,os,argparse
from pathlib import Path
from datetime import datetime,timezone
STATES={'todo','in_progress','blocked','waiting','done','cancelled'}
def update(project,task_id,title,owner,status,expected_revision):
 p=Path(project);cfg=json.loads((p/'docs/task-tracking.json').read_text())
 if cfg['mode']!='local': raise ValueError('Builtin tracker requires its own verified adapter; no writes performed')
 target=p/'tasks/todo.json';lock=p/'tasks/.write.lock'
 fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
 tmp=None
 try:
  data=json.loads(target.read_text())
  if data['revision']!=expected_revision: raise ValueError('Revision conflict; reread before updating')
  if status not in STATES or not all(isinstance(x,str) and x.strip() for x in [task_id,title,owner]): raise ValueError('Invalid task fields')
  entry=next((x for x in data['tasks'] if x['task_id']==task_id),None)
  if entry is None: entry={'task_id':task_id};data['tasks'].append(entry)
  entry.update(title=title,owner=owner,status=status,updated=datetime.now(timezone.utc).isoformat())
  data['revision']+=1
  tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');os.replace(tmp,target)
  return data['revision']
 finally:
  if tmp and tmp.exists(): tmp.unlink()
  os.close(fd);lock.unlink()
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('project')
 for field in ['task-id','title','owner','status']:a.add_argument('--'+field,required=True)
 a.add_argument('--expected-revision',type=int,required=True);x=a.parse_args()
 print(update(x.project,x.task_id,x.title,x.owner,x.status,x.expected_revision))
