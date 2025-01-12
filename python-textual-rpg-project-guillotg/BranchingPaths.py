import random

class BranchingPaths:
    branches = {"branch1":list(), "branch2":list(), "branch3":list()}

    @staticmethod
    def SetupBranches():
        BranchingPaths.branches["branch1"].append("combat")
        BranchingPaths.branches["branch2"].append("combat")
        BranchingPaths.branches["branch3"].append("combat")

        i = 0
        while i < 3:
            for b in BranchingPaths.branches:
                randomChoice = random.randint(0, 100)
                if randomChoice <= 65:
                    BranchingPaths.branches[b].append("combat")
                elif randomChoice <= 90:
                    BranchingPaths.branches[b].append("treasure")
                else:
                    BranchingPaths.branches[b].append("rest")
            i += 1
    
        while i < 6:
            for b in BranchingPaths.branches:
                randomChoice = random.randint(0, 100)
                if randomChoice <= 35:
                    BranchingPaths.branches[b].append("combat")
                elif randomChoice <= 45:
                    BranchingPaths.branches[b].append("elite")
                elif randomChoice <= 60:
                    BranchingPaths.branches[b].append("branch")
                elif randomChoice <= 85:
                    BranchingPaths.branches[b].append("treasure")
                else:
                    BranchingPaths.branches[b].append("shop")
            i += 1

        for b in BranchingPaths.branches:
            BranchingPaths.branches[b].append("shop")
        i += 1

        for b in BranchingPaths.branches:
            BranchingPaths.branches[b].append("rest")
        i += 1

        for b in BranchingPaths.branches:
            BranchingPaths.branches[b].append("boss")

    @staticmethod
    def NextStage(currentStage, currentBranch):
        return BranchingPaths.branches[currentBranch][currentStage + 1]