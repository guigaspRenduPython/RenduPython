import GameStateManager
import PlayerClass
import EnemyType
import ItemType
import BranchingPaths

PlayerClass.PlayerClass.getInfoFromFile()
EnemyType.EnemyType.getInfoFromFile()
ItemType.ItemType.getInfoFromFile()
BranchingPaths.BranchingPaths.SetupBranches()

gms = GameStateManager.GameStateManager()

gms.GameUpdate()