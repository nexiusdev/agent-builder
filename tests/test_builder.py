import unittest,tempfile,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import builder
class Tests(unittest.TestCase):
 def test_init(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'new';builder.init(p,'Example');self.assertEqual(builder.validate(p),[])
   self.assertFalse(json.loads((p/'project.json').read_text())['external_actions'])
 def test_no_overwrite(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);(p/'keep').write_text('safe')
   with self.assertRaises(FileExistsError):builder.init(p,'Example')
   self.assertEqual((p/'keep').read_text(),'safe')
 def test_missing(self):
  with tempfile.TemporaryDirectory() as t:self.assertTrue(builder.validate(t))
 def test_skills(self):
  for stage in json.loads((builder.ROOT/'config/stages.json').read_text()):
   self.assertIn('description:',(builder.ROOT/'.agents/skills'/stage['id']/'SKILL.md').read_text())
if __name__=='__main__':unittest.main()

class Records(unittest.TestCase):
 def test_upgrade_preserves(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Test');f=p/'registry/agents.json';f.write_text('[{"agent_id":"a"}]');builder.upgrade(p);self.assertEqual(json.loads(f.read_text())[0]['agent_id'],'a')
 def test_events_and_references(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Test')
   with self.assertRaises(ValueError):builder.event(p,'r','w','a','started','x')
   (p/'registry/agents.json').write_text('[{"agent_id":"a"}]');(p/'workflows/catalog.json').write_text('[{"workflow_id":"w"}]')
   a=builder.event(p,'r','w','a','started','x');b=builder.event(p,'r','w','a','succeeded','y');self.assertNotEqual(a,b);self.assertEqual(len(list((p/'runs/events').glob('*.json'))),2)
   with self.assertRaises(ValueError):builder.event(p,'r','w','a','invented','x')

class IndividualCommunication(unittest.TestCase):
 def test_scaffold_contract(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Single agent')
   c=json.loads((p/'docs/communication-contract.json').read_text())
   self.assertEqual(c['outbound_recipients'],[])
   self.assertEqual(c['authority'],'No external communication authorized')
 def test_upgrade_keeps_contract(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Single agent');f=p/'docs/communication-contract.json'
   f.write_text('{"owner":"preserve-me"}');builder.upgrade(p)
   self.assertEqual(json.loads(f.read_text()),{'owner':'preserve-me'})
