import unittest,tempfile,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import builder,tasks
class Tasks(unittest.TestCase):
 def test_scaffold_and_update(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Test');self.assertEqual(tasks.update(p,'T1','Test','owner','todo',0),1)
   with self.assertRaises(ValueError): tasks.update(p,'T1','Test','owner','done',0)
   self.assertEqual(json.loads((p/'tasks/todo.json').read_text())['revision'],1)
 def test_upgrade_preserves(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Test');tasks.update(p,'T1','Test','owner','todo',0);builder.upgrade(p)
   self.assertEqual(len(json.loads((p/'tasks/todo.json').read_text())['tasks']),1)
 def test_builtin_not_claimed(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Test');(p/'docs/task-tracking.json').write_text('{"mode":"builtin"}')
   with self.assertRaises(ValueError): tasks.update(p,'T1','Test','owner','todo',0)
 def test_lock_conflict(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'p';builder.init(p,'Test');(p/'tasks/.write.lock').touch()
   with self.assertRaises(FileExistsError): tasks.update(p,'T1','Test','owner','todo',0)
   self.assertTrue((p/'tasks/.write.lock').exists())
