class FaustianFork:
    def __init__(self):
        self.states = ["init", "commit", "fork", "branching", "merge_rebase"]

    def describe(self, stage):
        descriptions = {
            "init": "Joined Johns Hopkins as faculty. Entry into institutional neighborhood.",
            "commit": "Signed contract. Identity tied to the institution.",
            "fork": "Established Ukubona LLC. Now a vendor, not an employee.",
            "branching": "Spinning variants—interns, clients, universities.",
            "merge_rebase": "Merge innovations back or rebase a new academy."
        }
        return descriptions.get(stage, "Unknown stage")

fork = FaustianFork()
for stage in fork.states:
    print(f"{stage.upper()}: {fork.describe(stage)}")
